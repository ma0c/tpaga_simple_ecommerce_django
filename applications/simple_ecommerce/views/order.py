import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django.conf import LazySettings
from django.contrib.sites.shortcuts import get_current_site
from django import http
from django.contrib import messages


from base import views as base_views

from tpaga import (
    models as tpaga_models,
    tpaga,
    exceptions as tpaga_exceptions
)

from .. import (
    conf,
    forms,
    mixins,
    models,
    utils
)


settings = LazySettings()
logger = logging.Logger(__name__)


class List(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseListView):
    """
    List all Orders
    """
    queryset = models.Order.objects.all()
    permission_required = (
        'simple_ecommerce.manage_order'
    )
    template_name = "simple_ecommerce/order/list.html"

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.ORDER_DETAIL_URL_NAME
        context['refund_url_name'] = conf.ORDER_REFUND_URL_NAME
        context['delivered_name'] = conf.ORDER_DELIVERED

        if self.request.user.has_perm("simple_ecommerce.add_order"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.ORDER_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Order
    """
    model = models.Order
    permission_required = (
        'simple_ecommerce.add_order'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ORDER_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Order
    """
    model = models.Order

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("inventory.change_provider"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.ORDER_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("inventory.delete_provider"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.ORDER_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Order
    """
    model = models.Order
    fields = '__all__'
    permission_required = (
        'simple_ecommerce.change_order'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ORDER_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Order
    """
    model = models.Order
    permission_required = (
        'simple_ecommerce.delete_order'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ORDER_LIST_URL_NAME)


class Checkout(mixins.OrderOwnership, Detail):
    template_name = "simple_ecommerce/order/checkout.html"
    context_object_name = "order"


    def get_context_data(self, **kwargs):
        context = super(Checkout, self).get_context_data(**kwargs)
        order = self.get_object()

        current_site = get_current_site(self.request)

        use_https = self.request.is_secure()
        # For some reason use_https is always False :(
        protocol = "https" if use_https else "https"

        tpaga_order = tpaga_models.TPagaOrder(
            cost=order.total_value,
            purchase_details_url="{}://{}{}".format(
                protocol,
                current_site.domain,
                reverse_lazy(
                    conf.ORDER_CONFIRM_URL_NAME,
                    kwargs={
                        "slug": order.slug
                    }
                )
            ),
            order_id=order.id,
            terminal_id="1",
            purchase_description=",".join(item.item.name for item in order.orderitem_set.all()),
            user_ip_address=utils.get_client_ip(self.request)
        )

        request = tpaga.PaymentRequest()
        request.set_order(tpaga_order)

        try:
            response = request.send()

            context['payment_url'] = response.get("tpaga_payment_url", "")
            order.payment_token = response['token']
            order.save()
            if settings.DEBUG:
                import pprint
                pprint.pprint(tpaga_order.to_dict())
                pprint.pprint(response)
        except tpaga_exceptions.TPagaException as tpaga_ex:
            logger.error(tpaga_ex)

        return context


class Confirm(mixins.OrderOwnership, Detail):
    template_name = "simple_ecommerce/order/confirm.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super(Confirm, self).get_context_data(**kwargs)

        order = self.get_object()

        request = tpaga.PaymentStatus()
        request.set_token(order.payment_token)
        print(order.payment_token)
        try:
            response = request.send()
            if settings.DEBUG:
                import pprint
                pprint.pprint(response)
            order.status = response['status']
            order.save()
            print(response['status'])
            print(order.status)
        except tpaga_exceptions.TPagaException as tpaga_ex:
            messages.add_message(
                self.request,
                messages.ERROR,
                str(tpaga_ex)
            )
            logger.error(tpaga_ex)

        return context


class Refund(PermissionRequiredMixin, Detail):
    template_name = "simple_ecommerce/order/refund.html"
    context_object_name = "order"
    permission_required = (
        'simple_ecommerce.manage_order'
    )

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status != "delivered":
            messages.add_message(
                request,
                messages.ERROR,
                conf.ORDER_CANT_BE_REFUND
            )
            return http.HttpResponseRedirect(reverse_lazy(conf.ORDER_LIST_URL_NAME))
        return super(Refund, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Refund, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.ORDER_DETAIL_URL_NAME

        return context

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        request = tpaga.PaymentRefund()
        request.set_token(order.payment_token)
        try:
            response = request.send()
            order.status = response['status']
            if settings.DEBUG:
                import pprint
                pprint.pprint(response)
            order.save()
        except tpaga_exceptions.TPagaException as tpaga_ex:
            messages.add_message(
                self.request,
                messages.ERROR,
                str(tpaga_ex)
            )
            logger.error(tpaga_ex)
        return http.HttpResponseRedirect(reverse_lazy(conf.ORDER_LIST_URL_NAME))

class ProtectedDetail(PermissionRequiredMixin, Detail):
    permission_required = (
        'simple_ecommerce.manage_order'
    )

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy

from base import views as base_views

from applications.authentication.mixins import SuperAdminRequiredMixin

from .. import (
    models,
    forms,
    conf
)


class List(SuperAdminRequiredMixin, base_views.BaseListView):
    """
    List all Items
    """
    queryset = models.Item.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        if self.request.user.has_perm("simple_ecommerce.add_item"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.ITEM_CREATE_URL_NAME
            )
        
        return context


class Create(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Item
    """
    model = models.Item
    permission_required = (
        'simple_ecommerce.add_item'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ITEM_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(SuperAdminRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Item
    """
    model = models.Item

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("inventory.change_provider"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.ITEM_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("inventory.delete_provider"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.ITEM_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Item
    """
    model = models.Item
    fields = '__all__'
    permission_required = (
        'simple_ecommerce.change_item'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ITEM_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Item
    """
    model = models.Item
    permission_required = (
        'simple_ecommerce.delete_item'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ITEM_LIST_URL_NAME)

import random

from django.views import generic
from django import http
from django.urls import reverse_lazy

from .. import (
    forms,
    models,
    conf
)



class Index(generic.FormView):
    form_class = forms.SingleItemOrder
    template_name = "simple_ecommerce/main/index.html"
    random_item = None

    def get_random_item(self):
        if self.random_item is None:
            all_items = models.Item.objects.all()
            self.random_item = all_items[int(random.random() * len(all_items))]
        return self.random_item

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['random_item'] = self.get_random_item()

        print(context)

        return context

    def get_initial(self):
        return {
            'item': self.get_random_item()
        }


    def form_valid(self, form):
        item = form.cleaned_data["item"]
        quantity = form.cleaned_data["quantity"]
        new_order = models.Order.objects.create()
        new_item_order = models.OrderItem.objects.create(
            order=new_order,
            item=item,
            quantity=quantity,
        )
        return http.HttpResponseRedirect(
            reverse_lazy(
                conf.ORDER_CHECKOUT_URL_NAME,
                kwargs={
                    "slug": new_order.slug
                }
            )
        )


    def form_invalid(self, form):
        print("Form INVALID")
        return super(Index, self).form_invalid(form=form)

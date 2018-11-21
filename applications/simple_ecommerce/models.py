from django.db import models
from django.contrib.auth import models as auth_models

from base import models as base_models

class Item(base_models.FullSlugBaseModel):
    value = models.FloatField()


    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.name, self.value)


class Order(base_models.FullSlugBaseModel):

    ORDER_STATUSES = (
        ('created', 'CREATED'),
        ('paid', 'PAID'),
        ('delivered', 'DELIVERED'),
        ('reverted', 'REVERTED'),
    )

    user = models.ForeignKey(
        auth_models.User,
        on_delete=models.CASCADE,
        null=True
    )
    total_value = models.FloatField(default=0)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUSES
    )
    payment_token = models.TextField(default="")

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

    def update_total_cost(self):
        self.total_value = sum([item.total_value for item in self.orderitem_set.all()])

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.user, int(self.total_value), self.status)


class OrderItem(base_models.FullBaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_value = models.FloatField()


    def __init__(self, *args, **kwargs):
        super(OrderItem, self).__init__(*args, **kwargs)

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None
         ):
        self.total_value = self.item.value * self.quantity
        super(OrderItem, self).save(force_insert, force_update, using, update_fields)
        self.order.update_total_cost()
        self.order.save()

import random

from . import (
    models,
)


def create_n_items(n):
    """
from applications.simple_ecommerce import utils
utils.create_n_items(10)
    :param n:
    :return:
    """
    total_objects = models.Item.objects.all().count()
    for i in range(n):
        models.Item.objects.create(
            name="Randomly generated object {}".format(i+total_objects),
            value=random.random() * 1000000
        )


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
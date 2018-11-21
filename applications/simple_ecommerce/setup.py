from base import setup as base_setup

from . import (
    conf,
    models,
    utils
)

def setup():
    base_setup.configure_groups_and_permissions(
        conf.PERMISSIONS,
        conf.GROUPS
    )

    if models.Item.objects.all().count() == 0:
        print("Creating some random items")
        utils.create_n_items(10)

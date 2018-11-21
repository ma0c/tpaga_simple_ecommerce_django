from applications.simple_ecommerce import (
    setup as simple_ecommerce_setup,
)
from django.contrib.sites import models as site_models


from base import conf

def setup():
    """
from tpaga_simple_ecommerce_django import setup
setup.setup()
    :return: 
    """
    print("Configuring sites")
    if not site_models.Site.objects.filter(name="localhost"):
        print("Creating default site")
        site_models.Site.objects.create(
            domain="localhost",
            name="localhost"
        )
    print(conf.CONFIGURING_APPLICATION.format("Simple e-commerce"))
    simple_ecommerce_setup.setup()


if __name__ == "__main__":
    setup()
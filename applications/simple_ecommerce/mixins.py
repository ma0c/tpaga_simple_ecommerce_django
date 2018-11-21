from django import http
from django.urls import reverse_lazy
from django.template.loader import get_template

from . import (
    conf
)

class OrderOwnership(object):
    def dispatch(self, request, *args, **kwargs):
        login_required_response = super(OrderOwnership, self).dispatch(request, *args, **kwargs)
        # If the user is redirect to login, continue
        if login_required_response.status_code == 302:
            return login_required_response
        self.object = self.get_object()
        if self.object.user is None:
            self.object.user = request.user
            # As we change the slug, we need to redirect to new url
            self.object.slug = self.object.generate_valid_random_slug()
            self.object.save()
            return http.HttpResponseRedirect(
                reverse_lazy(
                    conf.ORDER_CHECKOUT_URL_NAME,
                    kwargs={
                        "slug": self.object.slug
                    }
                )
            )
        if self.object.user != request.user:
            return http.HttpResponseForbidden(get_template("403.html").render())

        return login_required_response
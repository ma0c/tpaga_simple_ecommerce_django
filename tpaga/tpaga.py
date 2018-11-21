import requests
import base64

from tpaga import (
    exceptions,
    conf,
    utils
)

class PaymentRequest(object):
    """
    Create a Payment request and get a response with a deeplink to pay with TPaga


```python
from tpaga import models, tpaga

order = models.TPagaOrder(
    cost="12000",
    purchase_details_url="https://contraslash.com/asdf",
    order_id=4,
    terminal_id="1",
    purchase_description="my first purchase",
    user_ip_address="186.112.65.210"
)

request = tpaga.PaymentRequest()
request.set_order(order)
response = request.send()

print(response)
````
    """
    _order = None
    def set_order(self, order):
        self._order = order

    def validate(self):
        if self._order is None:
            raise exceptions.MissconfiguredParameter("Order can't be None")
        if self._order.cost == 0:
            raise exceptions.MissconfiguredParameter("cost can't be 0")
        if not self._order.order_id :
            raise exceptions.MissconfiguredParameter("order_id must be set")
        if not self._order.purchase_details_url :
            raise exceptions.MissconfiguredParameter("purchase_details_url must be set")
        if not self._order.terminal_id :
            raise exceptions.MissconfiguredParameter("terminal_id must be set")
        if not self._order.user_ip_address :
            raise exceptions.MissconfiguredParameter("user_ip_address must be set")

        return True


    def send(self):

        if self.validate():
            response = requests.post(
                "{base_url}{endpoint}/".format(
                    base_url=conf.TPAGA_BASE_URL,
                    endpoint=conf.TPAGA_CREATE_PAYMENT_REQUEST_ENDPOINT
                ),
                headers={
                    "Authorization": "Basic {}".format(
                        base64.b64encode(
                            "{}:{}".format(
                                conf.TPAGA_USERNAME,
                                conf.TPAGA_PASSWORD
                            ).encode()
                        ).decode()
                    ),
                    "Content-Type": "application/json"
                },
                json=self._order.to_dict()
            )
            return utils.raise_exeption_or_return_content(response)
        else:
            return None


class TokenBasedRequest(object):
    _token = ""

    def set_token(self, token):
        self._token = token


class PaymentStatus(TokenBasedRequest):
    """
    Check payment status of a TPaga's payment
```python
from tpaga import tpaga
request = tpaga.PaymentStatus()
request.set_token("pr-de6eecd9794c50d5249dba3984b471fc810f53dc58c53a980105b91f4669a7de00c9f1ff")
response = request.send()
```
    """

    def send(self):
        response = requests.get(
            "{base_url}{endpoint}/".format(
                base_url=conf.TPAGA_BASE_URL,
                endpoint=conf.TPAGA_PAYMENT_STATUS_REQUEST_ENDPOINT.format(self._token)
            ),
            headers={
                "Authorization": "Basic {}".format(
                    base64.b64encode(
                        "{}:{}".format(
                            conf.TPAGA_USERNAME,
                            conf.TPAGA_PASSWORD
                        ).encode()
                    ).decode()
                ),
                "Content-Type": "application/json"
            }
        )
        return utils.raise_exeption_or_return_content(response)



class ConfirmDelivery(TokenBasedRequest):
    """
    Confirm delivery  of a TPaga's payment
```python
from tpaga import tpaga
request = tpaga.ConfirmDelivery()
request.set_token("pr-8381a8e8f435732a1041d59d6dc9087a62c0aac38078959ea413551a60c7aed1ca77b0b5")
response = request.send()
```
        """
    def send(self):
        response = requests.post(
            "{base_url}{endpoint}/".format(
                base_url=conf.TPAGA_BASE_URL,
                endpoint=conf.TPAGA_CONFIRM_DELIVERY_PAYMENT_REQUEST_ENDPOINT
            ),
            headers={
                "Authorization": "Basic {}".format(
                    base64.b64encode(
                        "{}:{}".format(
                            conf.TPAGA_USERNAME,
                            conf.TPAGA_PASSWORD
                        ).encode()
                    ).decode()
                ),
                "Content-Type": "application/json"
            },
            json={
                "payment_request_token": self._token
            }
        )
        return utils.raise_exeption_or_return_content(response)


class PaymentRefund(TokenBasedRequest):
    """
        Refund payment of a TPaga's payment
```python
from tpaga import tpaga
request = tpaga.ValidatePayment()
request.set_token("pr-260465d949224022b831031c9ac5d654461a9bd7f3265c67147695fc579c0074")
response = request.send()
```
    """

    def send(self):

        response = requests.post(
            "{base_url}{endpoint}/".format(
                base_url=conf.TPAGA_BASE_URL,
                endpoint=conf.TPAGA_REFUND_REQUEST_ENDPOINT
            ),
            headers={
                "Authorization": "Basic {}".format(
                    base64.b64encode(
                        "{}:{}".format(
                            conf.TPAGA_USERNAME,
                            conf.TPAGA_PASSWORD
                        ).encode()
                    ).decode()
                ),
                "Content-Type": "application/json"
            },
            json={
                "payment_request_token": self._token
            }
        )
        return utils.raise_exeption_or_return_content(response)

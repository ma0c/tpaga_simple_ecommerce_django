import json
import uuid
import datetime

class SimpleObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = vars(obj)
            return self.default(d)
        return obj

class PlainObject(object):

    def to_dict(self):
        return {key[1:]: value for key, value in vars(self).items()}

    def to_json(self):
        return json.dumps(self.to_dict(), cls=SimpleObjectEncoder)

    def __repr__(self):
        return json.dumps(self.__dict__)

class TPagaOrder(PlainObject):
    """
    File generated automatically by python_simple_class_generator.py

from tpaga import models
models.TPagaOrder().to_json()
models.TPagaOrder(purchase_items=[models.TPagaProduct()]).to_json()
    """
    def __init__(self,
                 miniapp_user_token=None,
                 cost=0, purchase_details_url="", voucher_url="", idempotency_token="", order_id="",
                 terminal_id="", purchase_description="", purchase_items=list(), user_ip_address="", merchant_user_id=None, token="",
                 tpaga_payment_url="", status="", expires_at="", cancelled_at=None, checked_by_merchant_at=None, delivery_notification_at=None):
        self._miniapp_user_token = miniapp_user_token
        self._cost = int(cost)
        self._purchase_details_url = purchase_details_url
        self._voucher_url = voucher_url
        self._idempotency_token = idempotency_token if idempotency_token else str(uuid.uuid4())
        self._order_id = order_id
        self._terminal_id = terminal_id
        self._purchase_description = purchase_description
        self._purchase_items = purchase_items
        self._user_ip_address = user_ip_address
        self._merchant_user_id = merchant_user_id
        self._token = token
        self._tpaga_payment_url = tpaga_payment_url
        self._status = status
        self._expires_at = expires_at if expires_at else (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()
        self._cancelled_at = cancelled_at
        self._checked_by_merchant_at = checked_by_merchant_at
        self._delivery_notification_at = delivery_notification_at


    @property
    def miniapp_user_token(self):
        return self._miniapp_user_token


    @miniapp_user_token.setter
    def miniapp_user_token(self, value):
        self._miniapp_user_token = value


    @miniapp_user_token.deleter
    def miniapp_user_token(self):
        del self._miniapp_user_token


    @property
    def cost(self):
        return self._cost


    @cost.setter
    def cost(self, value):
        self._cost = value


    @cost.deleter
    def cost(self):
        del self._cost


    @property
    def purchase_details_url(self):
        return self._purchase_details_url


    @purchase_details_url.setter
    def purchase_details_url(self, value):
        self._purchase_details_url = value


    @purchase_details_url.deleter
    def purchase_details_url(self):
        del self._purchase_details_url


    @property
    def voucher_url(self):
        return self._voucher_url


    @voucher_url.setter
    def voucher_url(self, value):
        self._voucher_url = value


    @voucher_url.deleter
    def voucher_url(self):
        del self._voucher_url


    @property
    def idempotency_token(self):
        return self._idempotency_token


    @idempotency_token.setter
    def idempotency_token(self, value):
        self._idempotency_token = value


    @idempotency_token.deleter
    def idempotency_token(self):
        del self._idempotency_token


    @property
    def order_id(self):
        return self._order_id


    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    @order_id.deleter
    def order_id(self):
        del self._order_id


    @property
    def terminal_id(self):
        return self._terminal_id


    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value


    @terminal_id.deleter
    def terminal_id(self):
        del self._terminal_id


    @property
    def purchase_description(self):
        return self._purchase_description


    @purchase_description.setter
    def purchase_description(self, value):
        self._purchase_description = value


    @purchase_description.deleter
    def purchase_description(self):
        del self._purchase_description


    @property
    def purchase_items(self):
        return self._purchase_items


    @purchase_items.setter
    def purchase_items(self, value):
        self._purchase_items = value


    @purchase_items.deleter
    def purchase_items(self):
        del self._purchase_items


    @property
    def user_ip_address(self):
        return self._user_ip_address


    @user_ip_address.setter
    def user_ip_address(self, value):
        self._user_ip_address = value


    @user_ip_address.deleter
    def user_ip_address(self):
        del self._user_ip_address


    @property
    def merchant_user_id(self):
        return self._merchant_user_id


    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value


    @merchant_user_id.deleter
    def merchant_user_id(self):
        del self._merchant_user_id


    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, value):
        self._token = value


    @token.deleter
    def token(self):
        del self._token


    @property
    def tpaga_payment_url(self):
        return self._tpaga_payment_url


    @tpaga_payment_url.setter
    def tpaga_payment_url(self, value):
        self._tpaga_payment_url = value


    @tpaga_payment_url.deleter
    def tpaga_payment_url(self):
        del self._tpaga_payment_url


    @property
    def status(self):
        return self._status


    @status.setter
    def status(self, value):
        self._status = value


    @status.deleter
    def status(self):
        del self._status


    @property
    def expires_at(self):
        return self._expires_at


    @expires_at.setter
    def expires_at(self, value):
        self._expires_at = value


    @expires_at.deleter
    def expires_at(self):
        del self._expires_at


    @property
    def cancelled_at(self):
        return self._cancelled_at


    @cancelled_at.setter
    def cancelled_at(self, value):
        self._cancelled_at = value


    @cancelled_at.deleter
    def cancelled_at(self):
        del self._cancelled_at


    @property
    def checked_by_merchant_at(self):
        return self._checked_by_merchant_at


    @checked_by_merchant_at.setter
    def checked_by_merchant_at(self, value):
        self._checked_by_merchant_at = value


    @checked_by_merchant_at.deleter
    def checked_by_merchant_at(self):
        del self._checked_by_merchant_at


    @property
    def delivery_notification_at(self):
        return self._delivery_notification_at


    @delivery_notification_at.setter
    def delivery_notification_at(self, value):
        self._delivery_notification_at = value


    @delivery_notification_at.deleter
    def delivery_notification_at(self):
        del self._delivery_notification_at



class TPagaProduct(PlainObject):
    """
    File generated automatically by python_simple_class_generator.py

from tpaga import models
models.TPagaProduct().to_json()
    """
    def __init__(self, name="", value=""):
        self._name = name
        self._value = value


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        self._name = value


    @name.deleter
    def name(self):
        del self._name


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value


    @value.deleter
    def value(self):
        del self._value





import os


TPAGA_BASE_URL = "https://stag.wallet.tpaga.co/merchants/api/v1"
TPAGA_CREATE_PAYMENT_REQUEST_ENDPOINT = "/payment_requests/create"
TPAGA_PAYMENT_STATUS_REQUEST_ENDPOINT = "/payment_requests/{}/info"
TPAGA_CONFIRM_DELIVERY_PAYMENT_REQUEST_ENDPOINT = "/payment_requests/confirm_delivery"
TPAGA_REFUND_REQUEST_ENDPOINT = "/payment_requests/refund"
TPAGA_USERNAME = os.environ.get("TPAGA_USERNAME", "")
TPAGA_PASSWORD = os.environ.get("TPAGA_PASSWORD", "")
from . import (
    exceptions
)

def raise_exeption_or_return_content(response):
    if 400 <= response.status_code < 500:
        raise exceptions.HttpClientError("{} - {}".format(response.status_code, response.content.decode()))
    if response.status_code >= 500:
        raise exceptions.HttpServerError("{} - {}".format(response.status_code, response.content.decode()))
    return response.json()
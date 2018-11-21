class TPagaException(Exception):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value


class MissconfiguredParameter(TPagaException):
    pass


class HttpClientError(TPagaException):
    pass


class HttpServerError(TPagaException):
    pass
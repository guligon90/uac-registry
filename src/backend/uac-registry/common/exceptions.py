# Base imports
from typing import Optional, Union

# DRF imports
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status


DEFAULT_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
DEFAULT_CODE = 'INTERNAL_SERVER_ERROR'


class CustomAPIException(APIException):
    status_code = DEFAULT_STATUS
    default_code = DEFAULT_CODE

    def __init__(
        self,
        context: str,
        message: str,
        code: Optional[str] = None,
        status_code: Optional[int] = None
    ) -> None:
        if status_code is not None:
            self.status_code = status_code

        if code is not None:
            self.default_code = code

        self.detail = {
            'code': self.default_code,
            'context': context,
            'message': message,
            'status': self.status_code,
        }

        super().__init__(self)


def response_from_exception(
    context: str,
    exception: Union[APIException, Exception],
    status_code: Optional[int] = DEFAULT_STATUS
) -> Response:
    code = exception.__class__.__name__
    message = str(exception)
    status_code = exception.status_code if isinstance(exception, APIException) else status_code
    custom_exc = CustomAPIException(context, message, code, status_code)

    return Response(custom_exc.detail, status=custom_exc.status_code)

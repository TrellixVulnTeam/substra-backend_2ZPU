from rest_framework import response
from rest_framework import status


class AlreadyExistsError(Exception):
    """The asset was already created in the local representation"""

    pass


class ApiError(Exception):
    """Base error response returned by API."""

    status = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal server error."

    def __init__(self, message=None, data=None):
        message = message or self.message

        self.error = data or {}
        self.error["message"] = message

        super().__init__(message)

    def response(self):
        """Get HTTP Response from error instance."""
        return response.Response(self.error, status=self.status)


class BadRequestError(ApiError):
    status = status.HTTP_400_BAD_REQUEST
    message = "Bad request."


class AssetPermissionError(Exception):
    def __init__(self, message="Unauthorized"):
        super().__init__(self, message)

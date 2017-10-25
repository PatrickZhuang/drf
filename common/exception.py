from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):
    # Call REST framework's  default exception handler first
    # to get standard error response
    response = exception_handler(exception, context)

    # Now customize the response
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

from django.http import Http404
from sentry_sdk import capture_exception


class SentryCatchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            capture_exception(exception)
        elif isinstance(exception, Exception):
            capture_exception(exception)
        return None

import time
from django.utils.deprecation import MiddlewareMixin

class RequestTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request._start_time
        print(f"Request to {request.path} took {duration:.2f}s")
        return response
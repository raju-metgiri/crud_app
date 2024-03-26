import time
import uuid
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class TimingAndIdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()
        request._request_id = str(uuid.uuid4())

    def process_response(self, request, response):
        if not hasattr(request, '_start_time') or not hasattr(request, '_request_id'):
            return response

        request._end_time = time.time()
        time_taken = request._end_time - request._start_time

        response['X-Elapsed-Time'] = str(time_taken)
        response['X-Request-ID'] = request._request_id

        logger.info(f"Request ID: {request._request_id}, Time Taken: {time_taken}")

        return response
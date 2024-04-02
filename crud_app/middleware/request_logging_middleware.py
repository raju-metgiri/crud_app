import time
import uuid
import logging
import json
from bs4 import BeautifulSoup
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

        response_content = response.content.decode('utf-8')  # decode the response content

        soup = BeautifulSoup(response_content, 'html.parser')
        table = soup.find('table')  # find the first table in the HTML

        if not table:
            return response
        headers = [th.text for th in table.find_all('th')]  # get the table headers
        rows = table.find_all('tr')  # get the table rows

        data = []
        for row in rows[1:]:  # skip the first row because it contains the headers
            values = [td.text for td in row.find_all('td')]  # get the values in the row
            row_dict = dict(zip(headers, values))  # create a dictionary for the row
            data.append(row_dict)

        logger.info(f"Request ID: {request._request_id}, Time Taken: {time_taken}, Response Payload: {data}")

        return response
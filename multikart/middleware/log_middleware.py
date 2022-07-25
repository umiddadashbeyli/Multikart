from django.utils.deprecation import MiddlewareMixin
from datetime import datetime

import logging
import socket
import time
import json


class LoggerMiddleware(MiddlewareMixin):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


    def process_request(self, request):
        """Set Request Start Time to measure time taken to service request."""
        if request.method in ['GET','POST', 'PUT', 'PATCH']:
            request.req_body = request.body
            request.start_time = datetime.now()
            with open('logs.log' ,"a") as f:
                f.write(f'{request} , {request.start_time}')


    def process_response(self, request, response):
        """Log data using logger."""
        response.start_time = datetime.now()
        with open('logs.log' ,"a") as f:
                f.write(f'{response} , {response.start_time}\n')
        return response





# request_logger = logging.getLogger('django.request')


# class RequestLogMiddleware(MiddlewareMixin):
#     """Request Logging Middleware."""

#     def __init__(self, *args, **kwargs):
#             """Constructor method."""
#             super().__init__(*args, **kwargs)

#     def process_request(self, request):
#         """Set Request Start Time to measure time taken to service request."""
#         if request.method in ['POST', 'PUT', 'PATCH']:
#             request.req_body = request.body
#         if str(request.get_full_path()).startswith('/api/'):
#             request.start_time = time.time()

#     def extract_log_info(self, request, response=None, exception=None):
#         """Extract appropriate log info from requests/responses/exceptions."""
#         log_data = {
#             'remote_address': request.META['REMOTE_ADDR'],
#             'server_hostname': socket.gethostname(),
#             'request_method': request.method,
#             'request_path': request.get_full_path(),
#             'run_time': time.time() - request.start_time,
#         }
#         if request.method in ['PUT', 'POST', 'PATCH']:
#             log_data['request_body'] = json.loads(
#                 str(request.req_body, 'utf-8'))
#             if response:
#                 if response['content-type'] == 'application/json':
#                     response_body = response.content
#                     log_data['response_body'] = response_body
#         return log_data

#     def process_response(self, request, response):
#         """Log data using logger."""
#         if request.method != 'GET':
#             if str(request.get_full_path()).startswith('/api/'):
#                 log_data = self.extract_log_info(request=request,
#                                                  response=response)
#                 request_logger.debug(msg='', extra=log_data)
#         return response

#     def process_exception(self, request, exception):
#         """Log Exceptions."""
#         try:
#             raise exception
#         except Exception:
#             request_logger.exception(msg="Unhandled Exception")
#         return exception
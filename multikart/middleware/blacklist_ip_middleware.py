from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden


class BlackListMiddleware(MiddlewareMixin):
    IP_BLACK_LIST = [

    ]

    def process_request(self,request,*args,**kwargs):
        if request.META.get('REMOTE_ADDR') in self.IP_BLACK_LIST:
            return HttpResponseForbidden
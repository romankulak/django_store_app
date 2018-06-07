import json
import logging

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from .models import WebRequest

logger = logging.getLogger(__name__)

def dumps(value):
    return json.dumps(value,default=lambda o:None)


class WebRequestMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        try:
            self.save(request, response)
        except Exception as e:
            logging.error('Error saving request log', e)
        return response

    def save(self, request, response):
        if hasattr(request, 'user'):
            user = request.user if type(request.user) == User else None
        else:
            user = None

        meta = request.META.copy()
        meta.pop('QUERY_STRING',None)
        meta.pop('HTTP_COOKIE',None)
        remote_addr_fwd = None

        if 'HTTP_X_FORWARDED_FOR' in meta:
            remote_addr_fwd = meta['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
                meta.pop('HTTP_X_FORWARDED_FOR')

        post = None
        uri = request.build_absolute_uri()
        if request.POST and uri != '/login/':
            post = dumps(request.POST)

        WebRequest(
            host = request.get_host(),
            path = request.path,
            method = request.method,
            uri = request.build_absolute_uri(),
            status_code = response.status_code,
            user_agent = meta.pop('HTTP_USER_AGENT',None),
            remote_addr = meta.pop('REMOTE_ADDR',None),
            remote_addr_fwd = remote_addr_fwd,
            meta = None if not meta else dumps(meta),
            cookies = None if not request.COOKIES else dumps(request.COOKIES),
            get = None if not request.GET else dumps(request.GET),
            post = None if not request.POST else dumps(request.POST),
            body = request.body,
            is_secure = request.is_secure(),
            is_ajax = request.is_ajax(),
            user = user
        ).save()

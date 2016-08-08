import django
from django.utils.functional import SimpleLazyObject

from .utils import get_user_agent

super_class = object
if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
    super_class = MiddlewareMixin


class UserAgentMiddleware(super_class):
    # A middleware that adds a "user_agent" object to request
    def process_request(self, request):
        request.user_agent = SimpleLazyObject(lambda: get_user_agent(request))

from django.core.cache import cache
from django.template.defaultfilters import slugify
from django.utils.functional import SimpleLazyObject

from user_agents import parse


def get_user_agent_cached(ua_string):
    # Tries to get UserAgent objects from cache before constructing a UserAgent
    # from scratch because parsing regexes.yaml/json (ua-parser) is slow
    key = slugify(ua_string)
    user_agent = cache.get(key)
    if user_agent is None:
        user_agent = parse(ua_string)
        cache.set(key, user_agent)
    return user_agent


class UserAgentMiddleware(object):
    # A middleware that adds a "user_agent" object to request
    def process_request(self, request):
        request.user_agent = SimpleLazyObject(
            lambda: get_user_agent_cached(request.META['HTTP_USER_AGENT']))

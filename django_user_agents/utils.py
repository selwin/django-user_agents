from django.core.cache import cache
from django.template.defaultfilters import slugify

from user_agents import parse


def get_user_agent(request):
    # Tries to get UserAgent objects from cache before constructing a UserAgent
    # from scratch because parsing regexes.yaml/json (ua-parser) is slow
    ua_string = request.META.get('HTTP_USER_AGENT', '')
    key = slugify(ua_string)
    user_agent = cache.get(key)
    if user_agent is None:
        user_agent = parse(ua_string)
        cache.set(key, user_agent)
    return user_agent


def get_and_set_user_agent(request):
    # If request already has ``user_agent``, it will return that, otherwise
    # call get_user_agent and attach it to request so it can be reused  
    if hasattr(request, 'user_agent'):
        return request.user_agent

    request.user_agent = get_user_agent(request)
    return request.user_agent
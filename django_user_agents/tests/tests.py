from django.core.cache import cache, get_cache
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test.client import Client
from django.utils import unittest

from user_agents.parsers import parse, UserAgent


iphone_ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
ipad_ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'


class MiddlewareTest(unittest.TestCase):

    def test_middleware_assigns_user_agent(self):
        client = Client(HTTP_USER_AGENT=ipad_ua_string)
        response = client.get(reverse('user_agent_test'))
        self.assertIsInstance(response.context['user_agent'], UserAgent)

    def test_cache_is_set(self):
        client = Client(HTTP_USER_AGENT=iphone_ua_string)
        response = client.get(reverse('user_agent_test'))
        self.assertIsInstance(response.context['user_agent'], UserAgent)
        self.assertIsInstance(cache.get(slugify(iphone_ua_string)), UserAgent)

    def test_empty_user_agent_does_not_cause_error(self):
        client = Client()
        response = client.get(reverse('user_agent_test'))
        self.assertEqual(response.context['user_agent'].os.family, 'Other')

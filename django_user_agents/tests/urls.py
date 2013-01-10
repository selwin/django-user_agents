from django.conf.urls import patterns, url


urlpatterns = patterns('django_user_agents.tests.views',
    url(r'^user-agents/', 'test', name='user_agent_test'),
    url(r'^filters/', 'test_filters', name='user_agent_test_filters'),
)
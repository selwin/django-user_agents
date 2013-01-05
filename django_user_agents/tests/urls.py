from django.conf.urls import patterns, url


urlpatterns = patterns('django_user_agents.tests.views',
    url(r'^user-agents/', 'test', name='user_agent_test'),
)
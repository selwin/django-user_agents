import django
from django.conf.urls import url
from django_user_agents.tests import views


if django.VERSION >= (1, 8):
    urlpatterns = [
        url(r'^user-agents/', views.test, name='user_agent_test'),
        url(r'^filters/', views.test_filters, name='user_agent_test_filters'),
    ]
else:
    from django.conf.urls import patterns
    urlpatterns = patterns(
        'django_user_agents.tests.views',
        url(r'^user-agents/', 'test', name='user_agent_test'),
        url(r'^filters/', 'test_filters', name='user_agent_test_filters'),
    )

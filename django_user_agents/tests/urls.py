from django.conf.urls import url
from django_user_agents.tests import views


urlpatterns = [
    url(r'^user-agents/', views.test, name='user_agent_test'),
    url(r'^filters/', views.test_filters, name='user_agent_test_filters'),
]

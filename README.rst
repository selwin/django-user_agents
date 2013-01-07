Django User Agents
==================

A django package that allows easy identification of visitor's browser, OS and device information, 
including whether the visitor uses a mobile phone, tablet or a touch capable device. Under the hood,
it uses `user-agents <https://github.com/selwin/python-user-agents>`_.


How to Use
==========

1. Install ``django-user-agents``, you'll have to make sure that `user-agents`_ is installed first::

    pip install pyyaml ua-parser user-agents
    pip install django-user-agents

2. Configure ``settings.py``:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        # other middlewares...
        'django_user_agents.middleware.UserAgentMiddleware',
    )

    # Cache backend is optional, but recommended to speed up user agent parsing
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

3. ``UserAgentMiddleware`` will add a ``user_agent`` attribute to ``request``:

.. code-block:: python
    
    def my_view(request):

        # Let's assume that the visitor uses an iPhone...
        request.user_agent.is_mobile # returns True
        request.user_agent.is_tablet # returns False
        request.user_agent.is_touch_capable # returns True
        request.user_agent.is_pc # returns False
        request.user_agent.is_bot # returns False
        
        # Accessing user agent's browser attributes
        request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
        request.user_agent.browser.family  # returns 'Mobile Safari'
        request.user_agent.browser.version  # returns (5, 1)
        request.user_agent.browser.version_string   # returns '5.1'

        # Operating System properties
        request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
        request.user_agent.os.family  # returns 'iOS'
        request.user_agent.os.version  # returns (5, 1)
        request.user_agent.os.version_string  # returns '5.1'

        # Device properties
        request.user_agent.device  # returns Device(family='iPhone')
        request.user_agent.device.family  # returns 'iPhone'

You can find out more about user agent attributes at `here <https://github.com/selwin/python-user-agents>`_.


Running Tests
=============

.. code-block:: console

    `which django-admin.py` test django_user_agents --settings=django_user_agents.tests.settings --pythonpath=.


Changelog
=========

0.1.1
-----
* Fixed a ``KeyError`` exception in the case of empty ``HTTP_USER_AGENT``

0.1
---
* Initial release
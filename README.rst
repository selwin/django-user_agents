Django User Agents
==================

A django package that allows easy identification of visitor's browser, OS and device information,
including whether the visitor uses a mobile phone, tablet or a touch capable device. Under the hood,
it uses `user-agents <https://github.com/selwin/python-user-agents>`_.


Installation
============

1. Install ``django-user-agents``, you'll have to make sure that `user-agents`_ is installed first::

    pip install pyyaml ua-parser user-agents
    pip install django-user-agents

2. Configure ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        # Other apps...
        'django_user_agents',
    )

    # Cache backend is optional, but recommended to speed up user agent parsing
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

    # Name of cache backend to cache user agents. If it not specified default
    # cache alias will be used. Set to `None` to disable caching.
    USER_AGENTS_CACHE = 'default'
Usage
=====

Middleware
----------

Add ``UserAgentMiddleware`` in ``settings.py``:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        # other middlewares...
        'django_user_agents.middleware.UserAgentMiddleware',
    )

A ``user_agent`` attribute will now be added to ``request``, which you can use
in ``views.py``:

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

If you have ``django.core.context_processors.request`` enabled, ``user_agent``
will also be available in template through ``request``::

    {% if request.user_agent.is_mobile %}
        Do stuff here...
    {% endif %}


View Usage
----------

``django-user_agents`` comes with ``get_user_agent`` which takes a single
``request`` argument and returns a ``UserAgent`` instance. Example usage:

.. code-block:: python

    from django_user_agents.utils import get_user_agent

    def my_view(request):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            # Do stuff here...
        elif user_agent.is_tablet:
            # Do other stuff...


Template Usage
--------------

``django-user_agents`` comes with a few template filters:

* ``is_mobile``
* ``is_tablet``
* ``is_touch_capable``
* ``is_pc``
* ``is_bot``

You can use all of these like any other django template filters::

    {% load user_agents %}

    {% if request|is_mobile %}
        Mobile device stuff...
    {% endif %}

    {% if request|is_tablet %}
        Tablet stuff...
    {% endif %}

    {% if request|is_pc %}
        PC stuff...
    {% endif %}

    {% if request|is_touch_capable %}
        Touch capable device stuff...
    {% endif %}

    {% if request|is_bot %}
        Bot stuff...
    {% endif %}


You can find out more about user agent attributes at `here <https://github.com/selwin/python-user-agents>`_.


Running Tests
=============

.. code-block:: console

    `which django-admin.py` test django_user_agents --settings=django_user_agents.tests.settings --pythonpath=.


Changelog
=========

0.3.2
-----
* Added compatibility with Django 1.10. Thanks @grschafer and @dannyboscan!
* Added ``USER_AGENTS_CACHE`` option in ``settings.py``. Thanks @caxap!
* Fixes a crash that happens when parsing ``request`` objects without ``META``. Thanks @rafaelks!


0.3.1
-----
* Fixed a bug when request have no META attribute

0.3.0
-----
* Python 3, thanks to @hwkns!

0.2.2
-----
* Fixed a bug that causes cache set/read to fail when user agent is longer than 250 characters

0.2.1
-----
* Fixed packaging

0.2.0
-----
* Added template filters
* Added ``get_user_agent`` function in utils.py

0.1.1
-----
* Fixed a ``KeyError`` exception in the case of empty ``HTTP_USER_AGENT``

0.1
---
* Initial release

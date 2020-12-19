Development
===========

Python Version
--------------

This project is developed against python 3.7.

Requirements
------------

Requirements are specified in :file:`requirements/requirements.in` and
:file:`requirements/base-requirements.in` (for install requirements) and 
:file:`requirements/requirements-dev.in` (for development requirements). 
Requirements are pinned in :file:`requirements/requirements.txt` and 
:file:`requirements/requirements-dev.txt` to specific versions.

To change requirements, change the appropriate file, then use
:command:`pip-compile` from the `pip-tools`_ package::

    pip install pip-tools
    pip-compile requirements/requirements.in


To upgrade the requirements in a file, add the :kbd:`--upgrade` option::

    pip-compile --upgrade requirements/requirements.in

To install requirements needed for development, either run the
:command:`pip-sync` command from pip-tools::

    pip-sync requirements/*.txt

or use traditional pip to install the requirements files individually::

    pip install -r requirements/requirements.txt
    pip install -r requirements/requirements-dev.txt

.. _pip-tools: https://github.com/jazzband/pip-tools

Channel Layers
--------------

Deployments of this application require a Redis server as a channel message
backstore. Local development of a single instance of the application can
use a built-in local store, but it is recommended testing for deployment
is done using Redis.

To set the Channel Layers backstore, see the :file:`citrus/settings.py` and
under the `CHANNEL_LAYERS` object, set a default channel layer using::

    # For Local Memory
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },

    # For Redis Server
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('localhost', 6379)],
        },
    },

The best way to install Redis in development is via Docker. Download and
install Docker for your system, then run::

    docker run -p 6379:6379 -d redis:5

Django Basics
-------------

The base Django application can be run via the :file:`manage.py` script.
Run the script without any arguments to see available commands for Django.

To run the server locally (by default on Port 8000), run::

    python manage.py runserver

To see migrations applied to the Django database, run::

    python manage.py showmigrations

To apply unapplied migrations for the application or an app, run::

    python manage.py migrate [app]

Resources
---------

Django Documentation: https://www.djangoproject.com/

Channels Documentation: https://channels.readthedocs.io/en/stable/introduction.html

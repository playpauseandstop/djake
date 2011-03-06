=====
djake
=====

djake = Django + make where make is your manage.py script ran in activated
virtual environment.

Requirements
============

* `Python <http://www.python.org/>`_ 2.4 or higher
* `Django <http://www.djangoproject.com/>`_ 1.0 or higher

Installation
============

*On most UNIX-like systems, you'll probably need to run these commands as root
or using sudo.*

To install use::

    $ pip install djake

Or::

    $ easy_install djake

License
=======

``djake`` is licensed under the `BSD License
<http://github.com/playpauseandstop/djake/blob/master/LICENSE>`_.

Usage
=====

::

    $ cd /path/to/cloned-repo
    $ djake <TAB>
    $ djake syncdb --noinput
    $ djake test --failfast app

Or::

    $ djake -C /path/to/cloned-repo <TAB>
    $ djake -C /path/to/cloned-repo syncdb --noinput
    $ djake -C /path/to/cloned-repo test --failfast app

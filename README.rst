=====
djake
=====

djake = Django + make where make is your manage.py script ran in activated
virtual environment.

Requirements
============

* Unix-based OS
* `Django <http://www.djangoproject.com/>`_ 1.0 or higher

Installation
============

To install use::

    $ sudo make install

By default, ``djake`` installed to ``/usr/local``, but you should overwrite
this approach, by setting ``PREFIX`` environment var. For example, if you want
to install ``djake`` to home directory, execute::

    $ make PREFIX=~ install

To uninstall use::

    $ sudo make uninstall

Or if you use customized ``PREFIX``::

    $ make PREFIX=~ uninstall

License
=======

``djake`` is licensed under the `BSD License
<http://github.com/playpauseandstop/djake/blob/master/LICENSE>`_.

Usage
=====

::

    $ cd /path/to/django-project
    $ djake --help
    $ djake syncdb --noinput
    $ djake test --failfast app

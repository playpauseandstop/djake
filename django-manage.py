#!/usr/bin/env python

import os
import sys


__author__ = 'Igor Davydenko <playpauseandstop@gmail.com>'
__license__ = 'GNU General Public License v.3 or above'
__version__ = '0.1'

if __name__ == '__main__':
    dirname = os.getcwd()
    sys.path.append(dirname)

    childs = os.listdir(dirname)
    childs.sort()

    subdirs = []

    for name in childs:
        if name[0] == '.':
            continue

        if os.path.isdir(os.path.join(dirname, name)):
            subdirs.append(name)

    try:
        settings = 'settings'

        try:
            __import__(settings)
        except ImportError:
            settings = os.path.basename(dirname) + '.settings'

            try:
                __import__(settings)
            except ImportError:
                imported = False

                for subdir in subdirs:
                    settings = subdir + '.settings'

                    try:
                        __import__(settings)
                    except ImportError:
                        pass
                    else:
                        imported = True
                        break

                if not imported:
                    raise ImportError
    except ImportError:
        sys.stderr.write(
            "Error: Can't find the file 'settings.py' in the current work " \
            "directory %r and all subdirectories %r. It appears you've " \
            "customized things.\nYou'll have to run django-manage.py, " \
            "passing it your settings module.\n(If the file settings.py does " \
            "indeed exist, it's causing an ImportError somehow.)\n" % (
                dirname,
                subdirs,
            )
        )
        sys.exit(1)

    os.environ['DJANGO_SETTINGS_MODULE'] = settings

    try:
        from django.core.management import ManagementUtility
    except ImportError, e:
        sys.stderr.write(
            "Error: Can't load `django` library on current environment. " \
            "Please check your python system path and try again later.\n"
        )
        sys.exit(1)

    utility = ManagementUtility(sys.argv)
    utility.execute()

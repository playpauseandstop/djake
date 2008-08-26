#!/usr/bin/env python

import os, sys

if __name__ == '__main__':
    try:
        dirname = os.environ['PWD']
    except KeyError:
        import subprocess
        cmd = subprocess.Popen('cd', shell=True, stdout=subprocess.PIPE)
        dirname = cmd.communicate()[0].strip()
    sys.path.append(dirname)

    try:
        settings = 'settings'
        try:
            __import__(settings)
        except ImportError, e:
            settings = os.path.basename(dirname) + '.settings'
            __import__(settings)
    except ImportError, e:
        sys.stderr.write(
            "Error: Can't find the file 'settings.py' in the current work " +
            "directory %r. It appears you've customized things.\n" % dirname +
            "You'll have to run django-admin.py, passing it your settings " +
            "module.\n(If the file settings.py does indeed exist, it's " +
            "causing an ImportError somehow.)\n"
        )
        sys.exit(1)

    os.environ['DJANGO_SETTINGS_MODULE'] = settings

    try:
        from django.core.management import ProjectManagementUtility
    except ImportError, e:
        sys.stderr.write(
            "Error: Can't load 'django' library on current environment. " +
            "Please check your python system path and try again later.\n"
        )
        sys.exit(1)

    utility = ProjectManagementUtility(None, os.path.basename(dirname))
    utility.execute()
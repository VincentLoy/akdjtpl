# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "activeseed.settings.prod")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

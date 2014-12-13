# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# {{ project_name }}
# (c) 2014 ActivKonnect

from unipath import Path as _Path

DJANGO_ROOT = _Path(__file__).ancestor(2)
REPO_ROOT = DJANGO_ROOT.ancestor(1)

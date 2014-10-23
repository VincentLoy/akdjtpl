# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

from django.contrib.staticfiles.finders import FileSystemFinder, AppDirectoriesFinder, get_finders
from djangobower.finders import BowerFinder


class FinderDirs(object):
    def __init__(self, finder):
        self.finder = finder

    def list_paths(self):
        raise NotImplementedError


class FileSystemFinderDirs(FinderDirs):
    def list_paths(self):
        return (str(root) for prefix, root in self.finder.locations)


class AppDirectoriesFinderDirs(FinderDirs):
    def list_paths(self):
        return (str(self.finder.storages[app].location) for app in self.finder.apps)


def list_dirs():
    for finder in get_finders():
        if finder.__class__ in FINDERS_MAP:
            # noinspection PyCallingNonCallable
            for d in FINDERS_MAP[finder.__class__](finder).list_paths():
                yield d


FINDERS_MAP = {
    FileSystemFinder: FileSystemFinderDirs,
    AppDirectoriesFinder: AppDirectoriesFinderDirs,
    BowerFinder: FileSystemFinderDirs,
}
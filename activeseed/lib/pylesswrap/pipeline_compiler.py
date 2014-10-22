# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

from pipeline.compilers import CompilerBase
from activeseed.lib.pylesswrap.less import Less


files_cache = {}


class PyLessWrapCompiler(CompilerBase):
    output_extension = 'css'

    def __init__(self, *args, **kwargs):
        super(PyLessWrapCompiler, self).__init__(*args, **kwargs)
        self.less = Less(files_cache)  # TODO include paths and less binary

    def match_file(self, filename):
        return filename.lower().endswith('.less')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if outdated or force:
            self.less.compile(infile, outfile)

    def is_outdated(self, infile, outfile):
        try:
            return self.less.mtime(self.storage.path(infile)) \
                > self.storage.modified_time(outfile).timestamp()
        except (OSError, NotImplementedError):
            return True

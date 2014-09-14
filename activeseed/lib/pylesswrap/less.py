# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

import subprocess
import re
from os import path


COLOR_STRIP = re.compile(r"\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]")


def execute_command(args, cwd='.'):
    """
    Executes the given command in the given working dir, and returns a tuple with the content of
    stdout, stderr and the return code.

    :param args: list of arguments (including the command name)
    :param cwd: current working dir to work into
    :return:
    """

    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd=cwd,
    )

    out, err = process.communicate()
    ret = process.poll()

    return COLOR_STRIP.sub('', out), COLOR_STRIP.sub('', err), ret


class LessError(Exception):
    pass


class Less(object):
    def __init__(self, cache, include_paths=None, less_bin='lessc'):
        self.include_paths = include_paths if include_paths is not None else []
        self.less_bin = less_bin
        self.cache = cache

    def execute_command(self, args, infile):
        return execute_command(
            [
                self.less_bin,
                '--include-path={}'.format(path.pathsep.join(self.include_paths))
            ] + args,
            path.realpath(path.dirname(infile))
        )

    def compile(self, infile, outfile):
        pass

    def mtime(self, infile):
        pass

    def dependencies(self, infile):
        out, err, ret = self.execute_command(['-M', infile, 'output'], infile)

        if ret:
            raise LessError('Invalid input file "{}".\nReason:\n{}'.format(infile, err))

        yield infile, path.getmtime(infile)

        files = out.split(' ')[1:]

        i = 0
        while i < len(files):
            for j in range(i, len(files)):
                file_name = ' '.join(files[i:j + 1])

                try:
                    yield file_name, path.getmtime(file_name)
                    i = j + 1
                    break
                except OSError:
                    pass
            else:
                i += 1

    @property
    def command(self):
        return None


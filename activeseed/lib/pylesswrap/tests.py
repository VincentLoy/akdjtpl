# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

from unittest import TestCase
from os import path
import os
from shutil import rmtree
from tempfile import mkdtemp
from activeseed.lib.pylesswrap.less import execute_command, Less, LessError


TESTS_DIR = path.dirname(__file__)
ASSETS_DIR = path.join(TESTS_DIR, 'assets')


class TestExecuteCommand(TestCase):
    def test_execute_command_normal(self):
        self.assertEqual(('bonjour\n', '', 0), execute_command(['echo', 'bonjour']))

    def test_execute_command_error(self):
        self.assertEqual(('', '', 1), execute_command(['false']))


class TestLessWrapper(TestCase):
    def test_list_dependencies(self):
        less = Less({}, [path.join(ASSETS_DIR, 'b')])

        files = [
            path.join(ASSETS_DIR, 'a', 'test.less'),
            path.join(ASSETS_DIR, 'a', 'without_space.less'),
            path.join(ASSETS_DIR, 'b', 'with space.less'),
        ]

        self.assertEqual(
            set((x, path.getmtime(x)) for x in files),
            set(less.dependencies(files[0]))
        )

    def test_fail_on_invalid_file(self):
        less = Less({}, [path.join(ASSETS_DIR, 'b')])

        with self.assertRaises(LessError):
            list(less.dependencies(path.join(ASSETS_DIR, 'a', 'invalid.txt')))

    def test_fail_on_missing_file(self):
        less = Less({}, [path.join(ASSETS_DIR, 'b')])

        with self.assertRaises(LessError):
            list(less.dependencies(path.join(ASSETS_DIR, 'missing.less')))

    def test_mtime(self):
        class FailError(Exception):
            pass

        # noinspection PyUnusedLocal
        def fail(*args, **kwargs):
            raise FailError

        less = Less({}, [])
        file_name = path.join(ASSETS_DIR, 'a', 'without_space.less')
        mtime = path.getmtime(file_name)

        self.assertEqual(mtime, less.mtime(file_name))

        os.utime(file_name, (path.getatime(file_name), mtime + 1))
        self.assertEqual(mtime + 1, less.mtime(file_name))

        less.dependencies = fail
        self.assertEqual(mtime + 1, less.mtime(file_name))

        with self.assertRaises(FailError):
            os.utime(file_name, (path.getatime(file_name), mtime + 2))
            less.mtime(file_name)

    def test_compile(self):
        less = Less({}, [path.join(ASSETS_DIR, 'b')])

        out_dir = mkdtemp()

        try:
            out_file = path.join(out_dir, 'out.css')
            less.compile(path.join(ASSETS_DIR, 'a', 'a.less'), out_file)

            expected = """* {
  color: red;
}
"""

            with open(out_file, 'r') as f:
                self.assertEqual(expected, f.read())
        finally:
            rmtree(out_dir)

    def test_compile_invalid(self):
        less = Less({}, [path.join(ASSETS_DIR, 'b')])

        out_dir = mkdtemp()

        try:
            out_file = path.join(out_dir, 'out.css')

            with self.assertRaises(LessError):
                less.compile(path.join(ASSETS_DIR, 'a', 'invalid.txt'), out_file)
        finally:
            rmtree(out_dir)

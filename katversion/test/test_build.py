"""Tests for katversion build helpers."""

import unittest

from katversion import build


class TestBuildHelpers(unittest.TestCase):

    def test_setup_versioning_sets_version_and_commands(self):
        kwargs = build.setup_versioning(path='.')
        self.assertIn('version', kwargs)
        self.assertIn('cmdclass', kwargs)
        self.assertIn('build_py', kwargs['cmdclass'])
        self.assertIn('sdist', kwargs['cmdclass'])

    def test_setup_versioning_preserves_existing_cmdclass(self):
        class ExistingBuildPy(object):
            pass

        kwargs = build.setup_versioning(existing_cmdclass={'build_py': ExistingBuildPy}, path='.')
        self.assertTrue(issubclass(kwargs['cmdclass']['build_py'], ExistingBuildPy))

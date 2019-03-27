#!/usr/bin/env python
# -*- coding: utf-8 -*-


from HtmlTestRunner import HTMLTestRunner
import unittest
from unittest import TestLoader, TestSuite


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))

    example_tests = TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite = TestSuite([example_tests])
    runner = HTMLTestRunner(combine_reports=True,output='example_suite')
    runner.run(suite)
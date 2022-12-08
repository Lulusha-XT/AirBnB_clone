#!/usr/bin/python3
"""Module for test classes"""

import inspect

import pep8





class TestClassDocumentation():

    """Class that allow us to test multiples classes"""



    def __init__(self, tests, _class):

        """Constructor"""

        self.tests = tests

        self.name = _class



        # Get all the methods of class @name

        self.functions = inspect.getmembers(self.name, inspect.isfunction)



    def documentation(self):

        """Test documentation of the module, class and methods"""

        with self.tests.subTest(msg='Testing methods'):

            for f in self.functions:

                with self.tests.subTest(msg='Documentation method {}'

                                            .format(f[0])):



                    doc = f[1].__doc__

                    self.tests.assertGreaterEqual(len(doc), 1)



        with self.tests.subTest(msg='Testing class'):

            doc = self.name.__doc__

            self.tests.assertGreaterEqual(len(doc), 1)



    def pep8(self, files):

        """Test linter pep8 over the files"""

        pep8style = pep8.StyleGuide(quiet=True)

        result = pep8style.check_files(files)

        self.tests.assertEqual(result.total_errors, 0,

                               'Found code style errors (and warnings)."')

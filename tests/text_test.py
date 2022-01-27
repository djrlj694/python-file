"""
text_test.py - A module for testing the `TextFile` class.
"""
import os
import unittest
from pathlib import Path

from file import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 23, 2022'
__modified_date__ = 'Jan 26, 2022'


# =========================================================================== #
# CONSTANTS
# =========================================================================== #


# -- Filesystem -- #

HOME = Path(os.getenv('HOME', default='.')).resolve()
PREFIX = Path(os.getenv('PREFIX', default='.')).resolve()

ETC = PREFIX / 'etc'

PARENT1 = HOME
PARENT2 = ETC / 'content'

NAME1 = '.bash_profile'
PATH1A = PARENT1 / NAME1
PATH1B = Path(os.path.expandvars('${HOME}/' + NAME1))

NAME2 = 'sample_hello.txt'
PATH2 = PARENT2 / NAME2


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestTextFile(unittest.TestCase):

    def test_TextFile_1(self):
        """
        Tests creating a `TextFile` object from a text file's name and parent
        directory path.
        """

        # Create objects to be tested.
        file = TextFile(NAME1, parent=PARENT1)

        # Test assertions.
        self.assertEqual(
            # Actual
            file.path,
            # Expected
            PATH1A,
        )
        self.assertEqual(
            # Actual
            file.path,
            # Expected
            PATH1B,
        )

    def test_TextFile_1a(self):
        """
        Tests creating a `TextFile` object from a text file's path.
        """

        # Create objects to be tested.
        file = TextFile(path=PATH1A)

        # Test assertions.
        self.assertEqual(
            # Actual
            file.path,
            # Expected
            PATH1A,
        )

    def test_TextFile_1b(self):
        """
        Tests creating a `TextFile` object from a text file's path.
        """

        # Create objects to be tested.
        file = TextFile(path=PATH1B)

        # Test assertions.
        self.assertEqual(
            # Actual
            file.path,
            # Expected
            PATH1B,
        )
        self.assertEqual(
            # Actual
            file.path,
            # Expected
            PATH1A,
        )

    def test_list_TextFile(self):
        """
        Tests rendering a `TextFile` object as a list.
        """

        # Create objects to be tested.
        file = TextFile(path=PATH2)
        file.read()

        # Test assertions.
        self.assertEqual(
            # Actual
            list(file)[0],
            # Expected
            'Hello!',
        )


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()

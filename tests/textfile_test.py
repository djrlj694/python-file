"""
textfile_test.py - A module for testing the `TextFile` class.
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
__modified_date__ = 'Jan 23, 2022'


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

    def test_TextFile_init(self):
        """
        Tests creating a `TextFile` object.
        """

        # Create objects to be tested.
        file1 = TextFile(NAME1, parent=PARENT1)
        file1a = TextFile(path=PATH1A)
        file1b = TextFile(path=PATH1B)

        # Test assertions.
        self.assertEqual(
            # Actual
            file1.path,
            # Expected
            PATH1A,
        )
        self.assertEqual(
            # Actual
            file1a.path,
            # Expected
            PATH1A,
        )
        self.assertEqual(
            # Actual
            file1b.path,
            # Expected
            PATH1A,
        )

    def test_TextFile_list(self):
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

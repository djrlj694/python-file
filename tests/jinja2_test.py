"""
jinja2_test.py - A module for testing the `Jinja2File` class.
"""
import os
import unittest
from pathlib import Path

from file import Jinja2File


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

PREFIX = Path(os.getenv('PREFIX', default='.')).resolve()

ETC = PREFIX / 'etc'
PARENT = ETC / 'content'

NAME1 = 'sample_hello.txt.jinja2'
PATH1 = PARENT / NAME1

NAME2 = 'sample_email_body.md.jinja2'
PATH2 = PARENT / NAME2


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestJinja2File(unittest.TestCase):

    def test_Jinja2File(self):
        """
        Tests the `Jinja2File` class.
        """

        # Create objects to be tested.
        file1 = Jinja2File(path=PATH1)
        file2 = Jinja2File(path=PATH2)

        # Test assertions.
        self.assertEqual(
            # Actual
            file1.render(name='John'),
            # Expected
            'Hello, John!',
        )
        self.assertEqual(
            # Actual
            file2.render(
                is_new=False,
                receiver_name='John',
                sender_name='The File Team',
            ).split('\n')[0],
            # Expected
            'Hello again, John!',
        )


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()

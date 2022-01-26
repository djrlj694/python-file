"""
markdownfile_test.py - A module for testing the `MarkdownFile` class.
"""
import os
import unittest
from pathlib import Path

from file import MarkdownFile


# =========================================================================== #
# METADATA
# =========================================================================== #

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 26, 2022'
__modified_date__ = 'Jan 26, 2022'


# =========================================================================== #
# CONSTANTS
# =========================================================================== #


# -- Filesystem -- #

PREFIX = Path(os.getenv('PREFIX', default='.')).resolve()

ETC = PREFIX / 'etc'
PARENT = ETC / 'content'

NAME = 'sample_email_body.md'
PATH = PARENT / NAME


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestMarkdownFile(unittest.TestCase):

    def test_MarkdownFile(self):
        """
        Test the `MarkdownFile` class.
        """

        # Create objects to be tested.
        file = MarkdownFile(path=PATH)

        # Test assertions.
        self.assertEqual(
            # Actual
            file.to_html().split('\n')[0],
            # Expected
            '<p>Hello!</p>',
        )
        self.assertEqual(
            # Actual
            file.to_xhtml().split('\n')[0],
            # Expected
            '<p>Hello!</p>',
        )


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()

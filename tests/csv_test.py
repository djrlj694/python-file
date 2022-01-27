"""
csv_test.py - A module for testing the `CSVFile` class.
"""
import os
import unittest
from pathlib import Path

from file import CSVFile


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

PARENT = ETC / 'data'

NAME = 'sample_3x3_header.csv'
PATH = PARENT / NAME


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestCSVFile(unittest.TestCase):

    def test_list_CSVFile(self):
        """
        Tests the `CSVFile` class.
        """

        # Create objects to be tested.
        file = CSVFile(path=PATH, delimiter='|')

        # Test assertions.
        self.assertEqual(
            # Actual
            list(file)[0],
            # Expected
            ['Col_A', 'Col_B', 'Col_C'],
        )


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()

"""
yaml_test.py - A module for testing the `YAMLFile` class.
"""
import os
import unittest
from pathlib import Path

from file import YAMLFile


# =========================================================================== #
# METADATA
# =========================================================================== #

__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 24, 2022'
__modified_date__ = 'Jan 26, 2022'


# =========================================================================== #
# CONSTANTS
# =========================================================================== #


# -- Filesystem -- #

PREFIX = Path(os.getenv('PREFIX', default='.')).resolve()

ETC = PREFIX / 'etc'
PARENT = ETC / 'settings'

NAME = 'sample_hello.yaml'
PATH = PARENT / NAME


# =========================================================================== #
# CLASSES
# =========================================================================== #


class TestYAMLFile(unittest.TestCase):

    def test_YAMLFile(self):
        """
        Tests the `YAMLFile` class.
        """

        # Create objects to be tested.
        file = YAMLFile(path=PATH)

        # Test assertions.
        self.assertEqual(
            # Actual
            file.parse()['environments']['production']['target'],
            # Expected
            'DBPROD',
        )


# =========================================================================== #
# MAIN EXECUTION
# =========================================================================== #


# -- Main Execution -- #

# If this module is in the main module, call the main() function.
if __name__ == '__main__':
    unittest.main()

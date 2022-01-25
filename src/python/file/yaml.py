"""
yaml.py - A module defining a class (`YAMLFile`) to model a YAML file
(`*.yaml`).
"""
from typing import Any

import yaml

from .text import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 24, 2022'
__modified_date__ = 'Jan 24, 2022'


# =========================================================================== #
# CLASSES
# =========================================================================== #


class YAMLFile(TextFile):
    """
    An object class modeling a YAML file.

    Attributes
    ----------
    `path` : `str`
        The file's pathname
    `text` : `str`
        The file's raw textual content

    Methods
    -------
    `parse()`
        Parses the first YAML document in the string and produces a
        corresponding Python object.
    """

    # -- Output Methods -- #

    def parse(self) -> Any:
        """
        Parses the first YAML document in the string and produces a
        corresponding Python object.

        Returns
        -------
        `Any`
            The Python object
        """

        # Read the file.
        if self.text == '':
            self.read()

        # Return the object.
        return yaml.load(self.text, Loader=yaml.Loader)

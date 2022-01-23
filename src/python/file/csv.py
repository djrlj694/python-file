"""
csv.py - A module defining a class (`CSVFile`) to model a delimited data file
(e.g., `*.csv`)
"""
import csv
from collections.abc import Iterator
from dataclasses import dataclass

import pandas as pd

from .text import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 23, 2022'
__modified_date__ = 'Jan 23, 2022'


# =========================================================================== #
# CLASSES
# =========================================================================== #


@dataclass
class CSVFile(TextFile):
    """
    An object class modeling a CSV file.

    Attributes
    ----------
    `path` : `Path`
        The file's pathname
    `delimiter` : `str`
        The file's field delimiter

    Methods
    -------
    `to_df(*args, **kwargs)`
        Renders a data frame representation of the file.
    """

    # -- Instance Attributes -- #

    delimiter: str = ','

    # -- Magic Methods -- #

    def __iter__(self) -> Iterator:
        """
        Renders an iterator representation of the file.

        Returns
        -------
        `Iterator`
            The iterator representation
        """

        # Check if the file exists.
        self._open(mode='r')

        # Set an empty list for storing the file's lines of content.
        records = []

        # Read & parse the CSV file, or fail & exit the program.
        try:
            with self.path.open(mode='r') as fid:
                reader = csv.reader(fid, delimiter=self.delimiter)
                records = list(reader)
        except Exception as e:
            exit(e)

        # Yield the iterator representation.
        yield from records

    # -- Output Methods -- #

    def to_df(self, *args, **kwargs) -> pd.DataFrame:
        """
        Renders a data frame representation of the file.

        Returns
        -------
        `pd.DataFrame`
            The data frame representation.
        """

        # Return the DataFrame.
        return pd.read_csv(self.path, sep=self.delimiter, *args, **kwargs)

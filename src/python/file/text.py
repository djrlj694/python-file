"""
text.py - A module defining a class (`TextFile`) to model a text file.
"""
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from .base import BaseFile


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
class TextFile(BaseFile):
    """
    An object class modeling a text file.

    Attributes
    ----------
    `path` : `Path`
        The file's pathname

    Methods
    -------
    `read()`
        Reads the file's raw textual content.
    """

    # -- Instance Attributes -- #

    text: str = ''

    # -- Magic Methods -- #

    def __init__(
        self,
        name: str = '',
        parent: Union[str, Path] = '',
        path: Union[str, Path] = '',
        text: str = '',
    ):
        """
        Parameters
        ----------
        `name` : `str`
            The file's name
        `parent` : `Union[str, Path]`
            The file's parent directory pathname
        `path` : `Union[str, Path]`
            The file's pathname
        `text` : `str`
            The file's raw textual content
        """
        super().__init__(name, parent, path)
        self.text = text

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
        lines = []

        # Read the file's content, or fail & exit the program.
        try:
            with self.path.open(mode='r') as fid:
                lines = [line.rstrip('\n') for line in fid]
        except Exception as e:
            self._exit(e)

        # Yield the iterator representation.
        yield from lines

    # -- Input Methods

    def read(self):
        """
        Reads the file's raw textual content.
        """

        # Check if the file exists.
        self._open(mode='r')

        # Set the object's `text` attribute.
        self.text = self.path.read_text()

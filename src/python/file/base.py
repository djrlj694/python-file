"""
base.py - A module defining an abstract base class (`BaseFile`) from which to
subclass concrete object classes to model files of various types.
"""
import os
import sys
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Union


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


@dataclass  # type: ignore
class BaseFile(ABC):
    """
    An abstract base class modeling a file.

    Attributes
    ----------
    `path` : `Path`
        The file's pathname

    Methods
    ----------
    `read()`
        Reads the file.
    """

    # -- Instance Attributes -- #

    path: Path = Path('.')

    # -- Magic Methods -- #

    @abstractmethod
    def __init__(
        self,
        name: str = '',
        parent: Union[str, Path] = '',
        path: Union[str, Path] = '',
    ):
        """
        The constructor of the `BaseFile` class.

        Parameters
        ----------
        `name` : `str`
            The file's name
        `parent` : `Union[str, Path]`
            The file's parent directory pathname
        `path` : `Union[str, Path]`
            The file's pathname
        """

        # Expand embedded environment variables (i.e., replace each w/ the
        # value it respectively represents).
        expandname = os.path.expandvars(name)
        expandparent = os.path.expandvars(str(parent))
        expandpath = os.path.expandvars(str(path))

        # Set the file's absolute (i.e., normalized) path.
        if path == '':
            self.path = Path(expandparent).resolve() / expandname
        else:
            self.path = Path(expandpath).resolve()

    def __str__(self) -> str:
        """
        Renders a string representation of the file: its pathname.

        Returns
        -------
        `str`
            The string representation.
        """

        # Return the string representation.
        return str(self.path)

    # -- Input Methods -- #

    @abstractmethod
    def read(self):
        """
        Reads the file.

        Raises
        ------
        NotImplementedError
            If logic for reading the file is not specified.
        """

        raise NotImplementedError

    # -- Internal Instance Methods -- #

    def _open(self, mode: str = 'r'):
        """
        Exits if a file or its parent directory can't be opened.

        Parameters
        ----------
        `mode` : `str`
            Specifies whether a file is to be read (`r`) or written (`w`)
        """

        # Set the path to test.
        path = self.path
        if mode == 'w':
            path = path.parent

        # Read the file's content, or fail & exit the program.
        try:
            path.resolve(strict=True)
        except FileNotFoundError as e:
            self._exit(e)
        except OSError as e:
            self._exit(e)
        except Exception as e:
            self._exit(e)

    # -- Internal Static Methods -- #

    @staticmethod
    def _exit(e: Exception):
        """
        Prints an exception and exits.
        """

        print(f'{type(e).__name__}:', e)
        sys.exit(1)

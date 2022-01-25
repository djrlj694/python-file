"""
jinja2.py - A module defining a class (`Jinja2File`) to model a Jinja2 template
file (`*.jinja2`).
"""
from jinja2 import Template

from .text import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 23, 2022'
__modified_date__ = 'Jan 24, 2022'


# =========================================================================== #
# CLASSES
# =========================================================================== #


class Jinja2File(TextFile):
    """
    An object class modeling a Jinja2 template file.

    Attributes
    ----------
    `path` : `Path`
        The file's pathname
    `text` : `str`
        The file's raw textual content

    Methods
    -------
    `read()`
        Reads the file's raw textual content.
    `render()`
        Renders the file's template as a Unicode string.
    """

    # -- Output Methods -- #

    def render(self, *args, **kwargs) -> str:
        """
        Renders the template file as a Unicode string.

        Returns
        -------
        `str`
            The unicode string
        """

        # Read the file.
        if self.text == '':
            self.read()

        # Create a Jinja2 template.
        template = Template(self.text)

        # Return the Unicode string.
        return template.render(*args, **kwargs)

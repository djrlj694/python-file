"""
markdown.py - A module defining a class (`MarkdownFile`) to model a Markdown
file (`*.md`).
"""
from markdown import markdown

from .text import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 26, 2022'
__modified_date__ = 'Jan 26, 2022'


# =========================================================================== #
# CLASSES
# =========================================================================== #


class MarkdownFile(TextFile):
    """
    An object class modeling a Markdown file.

    Attributes
    ----------
    `path` : `str`
        The file's pathname
    `text` : `str`
        The file's raw textual content

    Methods
    -------
    `render()`
        Renders HTML or XHTML as a Unicode string.
    `to_html()`
        Renders HTML as a Unicode string.
    `to_xhtml()`
        Renders XHTML as a Unicode string.
    """

    # -- Class Attributes -- #

    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.smarty',
        'markdown.extensions.tables',
    ]

    # -- Output Methods -- #

    def render(self, **kwargs) -> str:
        """
        Renders HTML or XHTML as a Unicode string.

        Returns
        -------
        `str`
            The Unicode string
        """

        # Read the file.
        if self.text == '':
            self.read()

        # Copy the key-word arguments.
        new_kwargs = kwargs

        # Set the Markdown extensions.
        new_kwargs['extensions'] = kwargs.get(
            'extensions',
            MarkdownFile.extensions,
        )

        # Return the Unicode string.
        return markdown(self.text, **new_kwargs)

    def to_html(self, **kwargs) -> str:
        """
        Renders HTML as a Unicode string.

        Returns
        -------
        `str`
            The Unicode string
        """

        # Return the Unicode string.
        return self.render(output_format='html', **kwargs)

    def to_xhtml(self, **kwargs) -> str:
        """
        Renders XHTML as a Unicode string.

        Returns
        -------
        `str`
            The Unicode string
        """

        # Return the Unicode string.
        return self.render(output_format='xhtml', **kwargs)

# File

A Python package for working across various file types with greater ease and
consistency.

## Introduction

File is a software project that is premised on the possibility of easier, more
consistent file access and management when writing and testingPython modules,
packages, and [command-line interface (CLI)][CLI] applications. It seeks to provide a
common [application programming interface (API)][API] for working with files,
regardless of the underlying file type.

## Getting Started

### System Requirements

File supports 3 major operating systems:

* [Linux][Linux]
* [macOS][macOS]
* [Windows][Windows]

[Bash][GNU Bash] scripts included for running Python executables can indirectly support
Windows if used with Microsoft's native [Windows Subsystem for Linux (WSL)][WSL] or a
3rd-party emulator like Git BASH (part of [Git for Windows][Git for Windows]).

To use or test File, the following software must first be installed on your
system:

* [Python][Python] 3.9.7 or higher
* [GNU Bash][GNU Bash] 3.2.57 or higher

In addition, this project has multiple 3rd-party Python package dependencies:

* [Jinja2][jinja] 2.11.3 or higher
* [Markdown][markdown] 3.3.6 or higher
* [Pandas][pandas] 1.3.4 or higher
* [YAML][yaml] 0.2.5 or higher

These packages come preloaded with the [Anaconda][Anaconda] distribution of
Python.

Lastly, for the purpose of [continuous integration/development (CI/CD)][CICD], the
optional installation of the following toolchain is encouraged:

* [Git][Git] 2.32.0 or higher
* [GitFlow][GitFlow] 0.4.1 or higher
* [pre-commit][pre-commit] v2.16.0 or higher

### Installation

File currently is not setup for installation as a Python package, let alone
registered to a Python package repository like [Python Package Index (PyPI)][PyPI],
though that is the project's ultimate goal. So, in the mean time, to install
File as a software project for experimentation or contributing to Files, run the
following command:

```shell
$ git clone https://github.com/djrlj694/python-file.git
```


### Usage

TODO: Usage instructions for this project are pending.

## Files

Files in this project are organized as follows:

```shell
.
├── .dockerignore
├── .editorconfig
├── .env
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── README.md
├── REFERENCES.md
├── bin/
│   ├── debug.sh
│   └── test.sh
├── docker-compose.yml
├── docks/
├── etc/
│   ├── content/
│   │   ├── debug_custom.txt.tmpl
│   │   ├── debug_path.txt.tmpl
│   │   ├── debug_set.txt.tmpl
│   │   ├── debug_standard.txt.tmpl
│   │   ├── sample_email_body.html
│   │   ├── sample_email_body.md
│   │   ├── sample_email_body.md.jinja2
│   │   ├── sample_email_body.txt
│   │   ├── sample_hello.txt
│   │   ├── sample_hello.txt.jinja2
│   │   └── sample_hello.txt.tmpl
│   ├── data/
│   │   ├── sample_3x3_header.csv
│   │   └── sample_3x3_noheader.csv
│   └── settings/
│       ├── sample_hello.json
│       └── sample_hello.yaml
├── src/
│   ├── bash/
│   │   ├── functions.sh
│   │   ├── sources.sh
│   │   └── variables.env
│   └── python/
│       └── file/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── csv.py
│       │   ├── jinja2.py
│       │   ├── markdown.py
│       │   ├── text.py
│       │   └── yaml.py
└── tests/
    ├── csv_test.py
    ├── jinja2_test.py
    ├── markdown_test.py
    ├── text_test.py
    └── yaml_test.py
```

## Builds and Testing

[Unit tests][unit test] are included in the directory `tests`. Individual unit tests of
tests of related Python functions, class properties and methods, etc are
organized into test suites, where each test suite represents a Python module
following the naming convention `<MODULE>_test.py`, where `<MODULE>` is the
the aforementioned Python module being tested. For example:

* `text_test.py` tests class properties/methods in Python module `text.py`.

It should be noted that File does not offer 100% [test coverage][test coverage].
That said, File strives to offer reasonable enough test coverage.


## Documentation

Documentation for SHS App is this README itself, plus those listed in the
subsections that follow.

#### Community Health

* [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
* [`CONTRIBUTING.md`](CONTRIBUTING.md)

### Other

* [`REFERENCES.md`](REFERENCES.md)

## Known Issues

Currently, there are no known issues.

## References

API documentation, tutorials, and other online references and made portions of
File possible. See [REFERENCES.md](REFERENCES.md) for a list of some.

[Anaconda]: https://www.anaconda.com
[API]: https://en.wikipedia.org/wiki/API
[CICD]: https://en.wikipedia.org/wiki/CI/CD
[CLI]: https://en.wikipedia.org/wiki/Command-line_interface
[Git]: https://git-scm.com/
[Git for Windows]: https://gitforwindows.org
[GitFlow]: https://github.com/nvie/gitflow
[GNU Bash]: https://www.gnu.org/software/bash/
[GNU Make]: https://www.gnu.org/software/make/
[jinja]: https://jinja.palletsprojects.com
[Linux]: https://www.linuxfoundation.org
[macOS]: https://www.apple.com/macos/
[markdown]: https://github.com/Python-Markdown/markdown
[pre-commit]: https://github.com/pre-commit/pre-commit
[pandas]: https://pandas.pydata.org
[Python]: https://www.python.org
[PyPI]: https://pypi.org
[test coverage]: https://en.wikipedia.org/wiki/Code_coverage
[unit test]: hhttps://en.wikipedia.org/wiki/Unit_testing
[Windows]: https://www.microsoft.com/en-us/windows
[WSL]: https://docs.microsoft.com/en-us/windows/wsl/about
[yaml]: http://pyyaml.org/wiki/LibYAML

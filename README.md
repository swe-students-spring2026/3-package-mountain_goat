[![Python package tests](https://github.com/swe-students-spring2026/3-package-mountain_goat/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-mountain_goat/actions/workflows/ci.yml)

The package is available on PyPI here:

[PASTE_PYPI_LINK_HERE](PASTE_PYPI_LINK_HERE)

barkpy is a lighthearted Python package that adds dog-themed humor to everyday developer life.

This package includes functions that can:

- turn a normal request into a dramatic puppy-eyes request
- suggest a zoomie break based on how long you have been sitting
- rewrite urgent ticket titles in dog-alert language
- generate encouragement for a developer
- help choose one option from a list

## How to install and use this package

Try installing and using your package in a separate Python project.

1. Create a `pipenv`-managed virtual environment and install the latest version of your package: `pipenv install barkpy`
2. Activate the virtual environment: `pipenv shell`
3. Create a Python program file that imports your package, e.g.

```python
from barkpy import (
    puppy_eyes_translator,
    zoomie_timer,
    mailman_alert,
    good_boy_generator,
    paw_selector,
)

### Functions and Exact Examples

```python
from barkpy import puppy_eyes_translator

message = puppy_eyes_translator("Can you review my PR?", 7)
print(message)

*whimper* Can *tilts head* you review my *big round eyes* PR? *sad tail thump* *tiny puppy sigh*


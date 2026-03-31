# 🐶 barkpy — The Developer's Best Friend

[![Python package tests](https://github.com/swe-students-spring2026/3-package-mountain_goat/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-mountain_goat/actions/workflows/ci.yml)

**barkpy** is a lighthearted Python package that brings dog-themed joy to everyday developer life. Feeling burnt out after a rough debugging session? Let barkpy shower you with encouragement, suggest a zoomie break, and help you make hard technical decisions — the way only a good dog can.

📦 **Available on PyPI:** [https://pypi.org/project/barkpy/0.1.0/](https://pypi.org/project/barkpy/0.1.0/)

---

## 🦴 Features

| Function | What it does |
|---|---|
| `good_boy_generator` | Gives you a massive ego boost based on how rough your day was |
| `zoomie_timer` | Calculates the perfect high-intensity break after sitting too long |
| `mailman_alert` | Translates scary Jira tickets into dog barks |
| `paw_selector` | Sniffs out the best option from a list of choices |
| `puppy_eyes_translator` | Rewrites your PR review requests so teammates can't say no |

---

## 🚀 Installation

Install barkpy via pip:

```bash
pip install barkpy
```

Or inside a pipenv-managed project:

```bash
pipenv install barkpy
```

---

## 📖 Usage

### Import the package

```python
from barkpy import (
    good_boy_generator,
    zoomie_timer,
    mailman_alert,
    paw_selector,
    puppy_eyes_translator,
)
```

---

### `good_boy_generator(name, roughness)`

Provides a massive ego boost to a developer based on how rough their day has been. Higher roughness levels increase encouragement repetitions and belly rubs.

**Arguments:**
- `name` (str) — the developer's name
- `roughness` (int, 1–10) — how rough the day was

```python
from barkpy import good_boy_generator

result = good_boy_generator("Riley", 3)
print(result)
# Who's a good developer?! Who's a good developer?! Who's a good developer?!
# You are, Riley, you are!
# *wag wag* *scritch* *scritch* *scritch*
# Have a treat! 🦴
```

---

### `zoomie_timer(sitting_hours, has_backyard)`

Calculates the perfect zoomie break based on how long you've been sitting. Suggests backyard sprints or indoor spins depending on your living situation.

**Arguments:**
- `sitting_hours` (float) — how long you've been sitting (must be > 0)
- `has_backyard` (bool) — whether you have a backyard

```python
from barkpy import zoomie_timer

result = zoomie_timer(3.5, False)
print(result)
# You've been sitting for 3.5 hours! Time for 3 spins in the kitchen and a quick bark at the mailman. *zooms down the hallway* 🐾

result = zoomie_timer(2.0, True)
print(result)
# You've been sitting for 2.0 hours! Time for 4 wind sprints around the backyard! *zooms at full speed* 🐾
```

---

### `mailman_alert(ticket_title, annoyance_level)`

Translates scary Jira tickets or deadline emails into dog barks to make them less intimidating. Higher annoyance levels produce louder, more aggressive barking.

**Arguments:**
- `ticket_title` (str) — the ticket or email subject line
- `annoyance_level` (int, 1–5) — how alarming it is

```python
from barkpy import mailman_alert

result = mailman_alert("Server is down", 5)
print(result)
# BARK BARK! *snarl* Server is down *protective growl*
```

---

### `paw_selector(options, favorite_toy)`

Helps you make a difficult technical decision by sniffing out the best option, with a scent-based justification involving your favorite toy.

**Arguments:**
- `options` (list of str) — the options to choose from (must not be empty)
- `favorite_toy` (str) — your dog's favorite toy, used in the justification

```python
from barkpy import paw_selector

result = paw_selector(["React", "Vue", "Svelte"], "Squeaky Ball")
print(result)
# The paws have spoken! We pick 'Svelte' because it smells like your Squeaky Ball! *tail wag* 🐾
```

---

### `puppy_eyes_translator(request_text, sadness_multiplier)`

Converts a help request into an irresistible puppy-eyes version so teammates can't say no to your pull request.

**Arguments:**
- `request_text` (str) — the request to transform (must not be empty)
- `sadness_multiplier` (int, 1–10) — how sad and desperate the message should sound

```python
from barkpy import puppy_eyes_translator

result = puppy_eyes_translator("Can you review my PR?", 7)
print(result)
# *whimper* Can you *tilts head* review my *big round eyes* PR? *sad tail thump* *tiny puppy sigh*

result = puppy_eyes_translator("Can you review my PR?", 4)
print(result)
# *whimper* Can you *tilts head* review my *big round eyes* PR?
```

---

## 🐾 Example Program

See [`example.py`](./example.py) for a complete program that demonstrates all five functions.

---

## 🛠️ Contributing

Follow these steps to set up the project locally and contribute.

### 1. Clone the repository

```bash
git clone https://github.com/swe-students-spring2026/3-package-mountain_goat.git
cd 3-package-mountain_goat
```

### 2. Install pipenv (if you don't have it)

```bash
pip install pipenv
```

### 3. Set up the virtual environment and install dependencies

```bash
pipenv --python $(which python3)
pipenv install --dev
pipenv install -e .
```

### 4. Activate the virtual environment

```bash
pipenv shell
```

### 5. Run the tests

```bash
pipenv run pytest
```

### 6. Build the package

```bash
pipenv run python -m build
```

### 7. Upload to PyPI (maintainers only)

```bash
pipenv run twine upload dist/*
```

---

## 🔄 Developer Workflow

All code changes must be made in a feature branch — never directly on `main`.

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes, then commit
git add .
git commit -m "Add your feature"
git push origin feature/your-feature-name
```

Then open a pull request on GitHub. A teammate must review and approve before merging. The GitHub Actions CI will automatically run tests on Python 3.12 and 3.13 when a PR is opened.

---

## ⚙️ CI/CD

This project uses GitHub Actions to run tests on every pull request to `main` across two Python versions (3.12 and 3.13). See [`.github/workflows/ci.yml`](./.github/workflows/ci.yml).

There are no environment variables or secret configuration files required to run this project.

---

## 👥 Team

- [Carolina](https://github.com/CarolLee04) — `good_boy_generator`
- [Sean Kim](https://github.com/seankimh) — `zoomie_timer`
- [Inoo Jung](https://github.com/ij2298-oss) — `mailman_alert`
- [Tae Kim](https://github.com/thk224) — `paw_selector`
- [Yi Lai](https://github.com/laiEEEEEEE) — `puppy_eyes_translator`
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains historical HP plotter art from 1970 created at York University. The artwork consists of Lissajous curves plotted using mathematical procedures on a standalone HP plotter device. Each plot was created by connecting successive points on Lissajous curves separated by large delta values, creating "string" art with interesting secondary curve intersections.

## Repository Structure

- `scanned-images/` - Contains scanned original paper plots from an Epson FastFoto FF-680W scanner
  - Each plot has two versions: verbatim copy (`FastFoto_XXXX.jpg`) and enhanced version (`FastFoto_XXXX_a.jpg`)
  - Images numbered from 0025 to 0040

## Development Environment

- **IDE**: PyCharm project named `yorku-hp-plotter-art-1070`
- **Python Version**: Python 3.12
- **Runtime**: Jupyter notebooks on Google Colab

## Coding Standards

- **Docstring Style**: Use Google-style docstrings for all functions and classes
- **Type Hints**: Always include type hints in Python code
  - Function signatures must have type hints for parameters and return values
  - Variables in function bodies should have inline type hints when first introduced (e.g., `x: np.ndarray = np.cos(t)`)
  - Use separate type hint declarations when variables are declared without immediate assignment
- **Testing**: Use pytest as the testing framework
  - Tests are located in a top-level `tests/` directory
  - Test directory structure mirrors source structure
  - Each source file has a corresponding test directory
  - Each function has its own test file (e.g., `tests/lissajou/plot/test_angle_list.py`)
  - Do NOT include `__init__.py` files in test directories (not needed for pytest)

## Future Development Plans

According to the README, the author plans to:
- Recreate the mathematical procedures in Python programs
- Parameterize each plot with three parameters: two frequencies and delta
- Give plots meaningful titles

## License

The project uses the MIT License.

## Current State

This is currently an archival repository containing only scanned images and documentation. No code or build system exists yet. Future development will involve Python implementation of the Lissajous curve mathematics.
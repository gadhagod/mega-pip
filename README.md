# Mega-Pip
Python packaging and distribution made easy.

### Installation

    pip3 install mega-pip

### Commands
- `publish`: Publish python package
  - `-p`/`--pypi`: Publish to pypi (default).
  - `-t`/`--testpypi`: Publish to testpypi.
- `reset`: Remove `dist`, `build`, and `*.egg_info` directories.

### Instructions
1. Make a [setup.py](https://github.com/navdeep-G/setup.py) file.
2. Run `mp publish`.
3. To reset, run `mp reset`.
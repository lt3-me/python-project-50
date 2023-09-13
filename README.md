### Hexlet tests and linter status:
[![Actions Status](https://github.com/lt3-me/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/lt3-me/python-project-50/actions)
[![Github Actions Status](https://github.com/lt3-me/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/lt3-me/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/37a8e55a56ea1adc55ba/maintainability)](https://codeclimate.com/github/lt3-me/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/37a8e55a56ea1adc55ba/test_coverage)](https://codeclimate.com/github/lt3-me/python-project-50/test_coverage)

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement" |

# gendiff

### Description

Compares two configuration files and shows a difference.

**How to use:**

*$ gendiff (-f format_name) first_file second_file*

**Available output formats**: stylish, plain, json *(default: stylish, when format (-f) unspecified)*

**Available file formats**: .json, .yaml (.yml)

### Example for json files

[![asciicast](https://asciinema.org/a/f3HNKOu6MIBMaSFoJVIDdQHvy.svg)](https://asciinema.org/a/f3HNKOu6MIBMaSFoJVIDdQHvy)

### Example for yaml files

[![asciicast](https://asciinema.org/a/DC1KXHQqMxhjBVbruO7cZ4ZxZ.svg)](https://asciinema.org/a/DC1KXHQqMxhjBVbruO7cZ4ZxZ)

### Using stylish formatter (default)

[![asciicast](https://asciinema.org/a/NHjQ2mV4IvbyMWCIKmOzUDx19.svg)](https://asciinema.org/a/NHjQ2mV4IvbyMWCIKmOzUDx19)

### Using plain formatter

[![asciicast](https://asciinema.org/a/f16fwTbKiohK7vBHKlodNg9za.svg)](https://asciinema.org/a/f16fwTbKiohK7vBHKlodNg9za)

### Using json formatter

[![asciicast](https://asciinema.org/a/F60bg7AXeuMDQpwCAxWXNzBD5.svg)](https://asciinema.org/a/F60bg7AXeuMDQpwCAxWXNzBD5)
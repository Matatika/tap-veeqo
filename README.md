# tap-veeqo

`tap-veeqo` is a Singer tap for Veeqo.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMatatika%2Ftap-veeqo%2Fmaster%2Fpyproject.toml&query=tool.poetry.dependencies.python&label=python)](https://docs.python.org/3/)
[![Singer SDK version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMatatika%2Ftap-veeqo%2Fmaster%2Fpoetry.lock&query=package%5B%3F(%40.name%3D%3D'singer-sdk')%5D.version&label=singer-sdk)](https://sdk.meltano.com/en/latest/)
[![License](https://img.shields.io/github/license/Matatika/tap-veeqo)](https://github.com/Matatika/tap-veeqo/blob/main/LICENSE)
[![Code style](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fruff%2Fmain%2Fassets%2Fbadge%2Fformat.json)](https://docs.astral.sh/ruff/)

## Overview

`tap-veeqo` extracts raw data from the [Veeqo API](https://developer.veeqo.com/docs) for the following resources:

- [Orders](https://developer.veeqo.com/docs#/reference/orders)
- [Products](https://developer.veeqo.com/docs#/reference/products)
- [Purchase Orders](https://developer.veeqo.com/docs#/reference/purchase-orders)
- [Suppliers](https://developer.veeqo.com/docs#/reference/suppliers)
- [Warehouses](https://developer.veeqo.com/docs#/reference/warehouses)
- [Customers](https://developer.veeqo.com/docs#/reference/customers)
- [Stores](https://developer.veeqo.com/docs#/reference/stores)
- [Delivery Methods](https://developer.veeqo.com/docs#/reference/delivery-methods)
- [Tags](https://developer.veeqo.com/docs#/reference/tags)
- Employees
- Product Brands
- Product Tags
- Sellables

## Installation

```bash
# pip
pip install git+https://github.com/Matatika/tap-veeqo

# pipx
pipx install git+https://github.com/Matatika/tap-veeqo

# poetry
poetry add git+https://github.com/Matatika/tap-veeqo
```

## Configuration

### Accepted Config Options

| Name      | Required | Default | Description       |
| --------- | -------- | ------- | ----------------- |
| `api_key` | Yes      |         | Your user API key |

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-veeqo --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

Before using `tap-veeqo`, you will need to [generate an API key](https://developer.veeqo.com/docs#/introduction/authentication/generating-your-api-keys) for the Veeqo user you want to authenticate as.

#### User roles

There is currently no documentation on how [Veeqo user roles](https://help.veeqo.com/en/articles/6969529-users-overview#h_78cc6b5a1d) affect API access. This tap was developed and tested using a test user with the `Admin` role, for which all resources are accessible - your milage may vary with other roles.

## Usage

You can easily run `tap-veeqo` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-veeqo --version
tap-veeqo --help
tap-veeqo --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_veeqo/tests` subfolder and
then run:

```bash
poetry run pytest
```

You can also test the `tap-veeqo` CLI interface directly using `poetry run`:

```bash
poetry run tap-veeqo --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-veeqo
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-veeqo --version
# OR run a test `elt` pipeline:
meltano elt tap-veeqo target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.

# Tabular Model Definition Language (TMDL) Formatter
![GitHub Actions](https://github.com/rterluun/precommit-tmdl-formatter/actions/workflows/build_validation.yaml/badge.svg)

## Introduction
This is a pre-commit hook that formats Tabular Model Definition Language (TMDL) files.

## Installation and Usage

### Installation
_precommit-tmdl-formatter_ can be installed using pip. It requires Python 3.11 or higher.

```bash
pip install git+https://github.com/rterluun/precommit-tmdl-formatter
```

If you want to install a specific version, you can specify the version tag:

```bash
pip install git+https://github.com/rterluun/precommit-tmdl-formatter@v0.2.0-rc1
```

### Usage
Add the following to your `.pre-commit-config.yaml` in the root of your repository:

```yaml
---
repos:
  - repo: https://github.com/rterluun/precommit-tmdl-formatter
    rev: master
    hooks:
      - id: tmdl_format_measures
      - id: tmdl_format_column_names
        args: ['--quote-columns --ignore-columns-starting-with=xi_']
```

Enable the pre-commit hook by running:

```bash
pip install pre-commit
cd /path/to/your/repo
pre-commit install
```

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

### Usage
Add the following to your `.pre-commit-config.yaml` in the root of your repository:

```yaml
---
repos:
  - repo: https://github.com/rterluun/precommit-tmdl-formatter
    rev: master
    hooks:
      - id: tmdl_format_measures
```

Enable the pre-commit hook by running:

```bash
pip install pre-commit
cd /path/to/your/repo
pre-commit install
```

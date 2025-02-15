# Tabular Model Definition Language (TMDL) Formatter
![GitHub Actions](https://github.com/rterluun/precommit-tmdl-formatter/actions/workflows/build_validation.yaml/badge.svg)

## 
This is a pre-commit hook that formats Tabular Model Definition Language (TMDL) files.


```yaml
---
repos:
  - repo: https://github.com/rterluun/precommit-tmdl-formatter
    rev: master
    hooks:
      - id: tmdl_formatter
```

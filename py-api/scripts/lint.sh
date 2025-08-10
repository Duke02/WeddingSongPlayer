#!/usr/bin/env bash

uv run pylint "$(git ls-files '*.py')"

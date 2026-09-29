#!/bin/sh
# Publish only the static website, preserving source and publication history.
set -eu
cd "$(dirname "$0")/.."
python3 scripts/check_site.py
if [ -n "$(git status --porcelain)" ]; then
  echo 'Commit your changes before publishing.' >&2
  exit 1
fi
git push origin main
git subtree push --prefix dist origin gh-pages

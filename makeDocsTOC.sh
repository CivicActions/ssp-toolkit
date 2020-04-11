#!/usr/bin/env bash

# Generate docs/controls.md (table of contents for controls/*.md)
# Requires: https://github.com/ekalinin/github-markdown-toc v0.5+

TMP=$(mktemp)

cd docs

DATE=`date "+%Y.%m.%d at %H%M"`

echo "# GNET Controls (compiled: ${DATE})" > controls.md

gh-md-toc controls/* | sed '/^           /d' | sed '/^   \*/d' | sed 's/^      //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' >> controls.md

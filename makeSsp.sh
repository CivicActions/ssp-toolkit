#!/usr/bin/env bash

# Make a SSP doc with a table of contents
# Requires: https://github.com/ekalinin/github-markdown-toc

./recombineControls.py -d > /tmp/ssp.md

mkdir -p outputs

gh-md-toc /tmp/ssp.md|sed '/^         /d' | sed 's/^   //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' > outputs/ssp.md

echo "" >> outputs/ssp.md

cat /tmp/ssp.md >> outputs/ssp.md

#!/usr/bin/env bash

# Make a SSP doc with a table of contents
# Requires: https://github.com/ekalinin/github-markdown-toc

# Add '-d' option for full RMF description.
./recombineControls.py > /tmp/ssp.md

mkdir -p outputs

gh-md-toc /tmp/ssp.md|sed '/^         /d' | sed 's/^   //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' > docs/ssp.md

echo "" >> docs/ssp.md

cat /tmp/ssp.md >> docs/ssp.md

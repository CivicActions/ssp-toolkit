#!/usr/bin/env bash

# Generate separate files for each family of controls and a table of contents.
# Requires: https://github.com/ekalinin/github-markdown-toc

# Add '-d' option for full RMF description.
./recombineControls.py -s docs/controls

cd docs

DATE=`date "+%Y.%m.%d at %H%M"`

echo "# LINCS Controls (compiled: ${DATE})" > controls.md

gh-md-toc controls/* | sed '/^         /d' | sed 's/^   //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' >> controls.md

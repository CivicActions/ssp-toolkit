#!/usr/bin/env bash

# Make a SSP doc with a table of contents
# Requires: https://github.com/ekalinin/github-markdown-toc v0.5+
#      and: https://github.com/GovReady/hyperGRC

# This is dependant on location of hypergrc
export PYTHONPATH=../../govready/hypergrc/

TMP=$(mktemp)

# Add '-d' option for full RMF description.
python3 -m hypergrc.ssp . > $TMP

mkdir -p docs

gh-md-toc $TMP | sed '/^         /d' | sed 's/^   //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' > docs/ssp.md

echo "" >> docs/ssp.md

cat $TMP >> docs/ssp.md

/bin/rm $TMP

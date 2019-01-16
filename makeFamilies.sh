#!/usr/bin/env bash

# Generate separate files for each family of controls and a table of contents.
# Requires: https://github.com/ekalinin/github-markdown-toc v0.5+
#      and: https://github.com/GovReady/hyperGRC

# This is dependant on location of hypergrc
export PYTHONPATH=../../govready/hypergrc/

TMP=$(mktemp)

# Add '-d' option for full RMF description.
python3 -m hypergrc.ssp . > $TMP
FAMILIES=$(egrep '^## ' $TMP | cut -d' ' -f2 | cut -d: -f1)

mkdir -p docs/controls

for FAM in $FAMILIES; do
  python3 -m hypergrc.ssp -d --family $FAM . > docs/controls/${FAM}.md
done

cd docs

DATE=`date "+%Y.%m.%d at %H%M"`

echo "# LINCS Controls (compiled: ${DATE})" > controls.md

#../gh-md-toc controls/* | sed '/^         /d' | sed 's/^   //' | \
#  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' >> controls.md

gh-md-toc controls/* | sed '/^           /d' | sed '/^   \*/d' | sed 's/^      //' | \
  sed 's/^\(Created by \[gh-md-toc\].*$\)/<!-- \1 -->/' >> controls.md

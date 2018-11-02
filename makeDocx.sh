#!/usr/bin/env bash

mkdir -p docx

for i in docs/controls/*.md; do
  b=$(basename -s .md $i)
  d="docx/${b}.docx"
  echo "pandoc -t docx $i"
  pandoc -t docx $i -o $d
done

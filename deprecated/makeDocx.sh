#!/usr/bin/env bash

mkdir -p docx

for i in docs/controls/*.md; do
  b=$(basename -s .md $i)
  d="docx/${b}.docx"
  echo -n "${b} "
  pandoc -t docx $i -o $d
done
echo "Done!"

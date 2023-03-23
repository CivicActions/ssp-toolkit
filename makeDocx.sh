#!/usr/bin/env bash

# Generate docx/* files for all appendices and frontmatter

TMP=$(mktemp)

cd appendices

for MD in *.md; do
  BASE=$(basename $MD .md)
  OUT="docx/${BASE}.docx"
  echo "Creating $OUT"
  pandoc -t docx --reference-doc=../assets/custom-reference.docx $MD -o ../${OUT}
done

cd ../frontmatter
MD=front-matter.md
BASE=$(basename $MD .md)
OUT="docx/${BASE}.docx"
echo "Creating $OUT"
pandoc -t docx --reference-doc=../assets/custom-reference.docx $MD -o ../${OUT}

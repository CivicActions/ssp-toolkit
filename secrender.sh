#!/usr/bin/env bash

# Requires https://github.com/CivicActions/secrender

# Fill template jinja2 files with values from configuration.yaml file.
# Output to file path after stripping the initial "templates/" directory.

for template in $(find templates -type f); do
  # strip initial "templates/" directory name from file
  file="${template#templates/}"
  # strip optional ".j2" extension
  ext=${template##*.}
  [[ $ext == "j2" ]] && file="${file%.*}"
  # make directory for secrendered file
  dir=$(dirname $file)
  mkdir -p $dir
  # do the work (use local secrender for efficiency)
  secrender.py --in configuration.yaml --template $template --output $file
  # docker run -v $PWD:/src drydockcloud/ci-secrender \
  #        --in configuration.yaml --template $template --output $file
  echo -n '.'
done
echo "done!"

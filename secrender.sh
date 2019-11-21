#!/usr/bin/env bash

# Requires https://github.com/CivicActions/secrender (add_output_option branch)

# Fill template jinja2 files with values from configuration.yaml file and
# output to components directory

for template in $(find templates -type f); do
  component=${template/templates/components}
  comp_dir=$(dirname $component)
  mkdir -p $comp_dir
  secrender.py --in configuration.yaml --template $template --output $component
  echo -n '.'
done
echo "done!"

# dockerized version:
# docker run -v $PWD:/src drydockcloud/ci-secrender --in configuration.yaml --template templates/Contractor/AC-ACCESS_CONTROL.yaml 

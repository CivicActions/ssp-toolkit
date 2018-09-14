#!/usr/bin/env python3
import os, os.path, sys, csv, re
from collections import OrderedDict
import rtyaml

'''
Read CSV file of controls and output a few columns.
CSV is better than TSV because newlines *within* cell text values
are preserved and quoted in CSV but they are eliminated in TSV.
'''

# Ensure an argument was passed.
if len(sys.argv) < 2:
  print("Usage:", sys.argv[0], "exported_controls.tsv")
  sys.exit()

# Ensure the passed argument is a file that exists.
fn_tsv = sys.argv[1]
if not os.path.exists(fn_tsv):
  print("Can't find file:", fn_tsv)
  sys.exit()

# Format long text with word wrap and prefix.
def formatImplementation(prefix, text):
  if not prefix[0] == '#':
    text = '\'' + text + '\''
  return textwrap.indent(
    textwrap.fill(text, width=80), prefix, lambda line: True)

# Open and parse the /.tsv file and write Low controls to yaml files.
controls = { }
with open(fn_tsv, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    # Skip non-Low controls.
    if row['Low'] != 'Yes':
      continue

    # Split the control implementation statement on keywords that
    # we recognize that give us separate text for different components
    # and for different "parts" of controls.
    cur_part = None
    cur_component = None
    parts_text = [ ]
    for line in row['Control Implementation Statement'].split("\n"):
      if line == "CivicActions/HDG":
        cur_component = "CivicActions-HDG"
      elif line == "HHS Responsibility:":
        cur_component = "HHS"
      elif line == "Acquia (ACE)":
        cur_component = "Acquia-ACE"
        continue
      elif re.match("Part [a-z]", line):
        cur_part = line
        cur_component = None
      else:
        key = (cur_part, cur_component)
        if len(parts_text) == 0 or parts_text[-1][0] != key:
          parts_text.append([key, ""])
        parts_text[-1][1] += line + "\n"

    # Create separate control entries for each component.
    for (part, component), text in parts_text:
      # If there was no text for this component, don't write anything.
      if not text.strip():
        continue

      # The first time we see a (component, control family) pair, create a dict to
      # hold its full name and the controls within it.
      control_family = row['Family of Control'].rstrip("-") # take off trailing dash
      key = (component, control_family)
      if key not in controls:
        controls[key] = {
          "name": row['Family'],
          "controls": [],
        }

      # Add this row as a control to its control family.
      # Use an OrderedDict to hold the keys so that when we output
      # it to disk we get the same order on each run.
      def cleanup_text(s):
        # In order for YAML flow-style strings, i.e. "key: >" followed
        # by lines of text, to work, the string must end with a newline,
        # so we'll strip trailing whitespace and then add back a newline
        # to ensure all entries do. The string must also not have spaces
        # immediately before the newline, which are usually mistakes anyway,
        # so we'll just remove those.
        s = s.rstrip() + "\n"
        s = re.sub(r"\s+\n", "\n", s)
        return s
      control = OrderedDict([
        ('control_key', row['Control']),
        ('control_key_part', part.strip() if part else None),
        ('control_name', row['Control Name']),
        ('standard_key', 'NIST-800-53'),
        ('covered_by', []),
        ('security_control_type', row['Security Control Type']),
        ('implementation_status', row['Control Status']),
        ('narrative', cleanup_text(text)),
        ('control_description', cleanup_text(row['Control Description'])),
      ])
      controls[key]["controls"].append(control)

# Write out the controls by control family.
for (component, control_family), control_family_data in controls.items():
  # Construct a file name for the component-control family file.
  fn_yaml = os.path.join(
    'components',
    component or "Other",
    control_family + "-" + control_family_data["name"].replace(" ", "_") + '.yaml'
  )

  # Make directory.
  os.makedirs(os.path.dirname(fn_yaml), exist_ok=True)

  # Write out.
  with open(fn_yaml, 'w') as yaml_file:
    doc = OrderedDict([
      ("name", component),
      ("family", control_family_data["name"]),
      ("documentation_complete", False),
      ("schema_version", "3.0.0"),
      ("satisfies", control_family_data["controls"])
    ])
    rtyaml.dump(doc, yaml_file)

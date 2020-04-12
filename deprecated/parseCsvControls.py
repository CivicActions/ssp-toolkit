#!/usr/bin/env python3
import os, os.path, sys, csv, re
from collections import OrderedDict
import rtyaml

'''
Read CSV file of controls and output a few columns into YAML files
in a modified OpenControl format where we break out the control
implementations into separate YAML files by family.

CSV is better than TSV because newlines *within* cell text values
are preserved and quoted in CSV but they are eliminated in TSV.
'''

# Ensure an argument was passed.
if len(sys.argv) < 2:
  print("Usage:", sys.argv[0], "exported_controls.csv")
  sys.exit()

# Ensure the passed argument is a file that exists.
fn_tsv = sys.argv[1]
if not os.path.exists(fn_tsv):
  print("Can't find file:", fn_tsv)
  sys.exit()

def cleanup_text(s):
  # In order for YAML flow-style strings, i.e. "key: >" followed
  # by lines of text, to work, the string must end with a newline,
  # so we'll strip trailing whitespace and then add back a newline
  # to ensure all entries do. The string must also not have spaces
  # immediately before the newline, which are usually mistakes anyway,
  # so we'll just remove those.
  s = s.rstrip() + "\n"
  s = re.sub(r"[ \t]+\n", "\n", s)
  return s

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
      if line == "CivicActions/Project":
        cur_component = "CivicActions"
      elif line == "Project Responsibility:":
        cur_component = "Project"
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
    components = set(component for ((part, component), text) in parts_text)
    for component in components:
      # The first time we see a (component, control family) pair, create a dict to
      # hold its full name and the controls within it.
      control_family = row['Family of Control'].rstrip("-") # take off trailing dash
      control_family_dir = control_family + "-" + row["Family"].replace(" ", "_") + '.yaml'
      key = (component or "Other", control_family_dir)
      if key not in controls:
        controls[key] = []

      # Add a record for this control.
      # Use an OrderedDict to hold the keys so that when we output
      # it to disk we get the same order on each run.
      control = OrderedDict([
        # OpenControl fields
        ('control_key', row['Control'].replace("-0", "-")), # convert e.g. AC-01 to just the canonical form AC-1
        ('standard_key', 'NIST SP 800-53 Revision 4'),
        ('covered_by', []),
        ('narrative', []),

        # Other fields that might be handy.
        ('control_name', row['Control Name']),
        ('security_control_type', row['Security Control Type']),
        ('implementation_status', row['Control Status']),
        ('control_description', cleanup_text(row['Control Description'])),
      ])
      controls[key].append(control)

      # Add all of the parts for this control & component pair into the narrative.
      for (part, _), text in parts_text:
        if _ != component: continue
        if not text.strip(): continue
        n = OrderedDict()
        if part and part.strip():
          n["key"] = part.strip()
        n["text"] = cleanup_text(text)
        control["narrative"].append(n)

# Write out the component.yaml files.
components = set(component_dir for (component_dir, control_family_fn) in controls.keys())
for component_dir in components:
  # Construct a file name for the component.yaml file.
  fn_yaml = os.path.join(
    'components',
    component_dir,
    "component.yaml"
  )

  # Make directory.
  os.makedirs(os.path.dirname(fn_yaml), exist_ok=True)

  # Write out.
  with open(fn_yaml, 'w') as yaml_file:
    doc = OrderedDict([
      ("name", component_dir),
      ("schema_version", "3.0.0"),
      ("satisfies", [
        # OpenControl requires a list of controls, but in our extension we list
        # YAML filenames that contain controls by family.
        control_family_fn for (_, control_family_fn) in controls.keys()
           if _ == component_dir
      ])
    ])
    rtyaml.dump(doc, yaml_file)

# Write out the controls by control family and component.
for (component_dir, control_family_fn), control_family_data in controls.items():
  # Construct a file name for the component-control family file.
  fn_yaml = os.path.join(
    'components',
    component_dir,
    control_family_fn
  )

  # Write out.
  with open(fn_yaml, 'w') as yaml_file:
    doc = OrderedDict([
      ("schema_version", "3.0.0"),
      ("satisfies", control_family_data)
    ])
    rtyaml.dump(doc, yaml_file)

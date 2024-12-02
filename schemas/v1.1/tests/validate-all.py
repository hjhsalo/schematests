#!/usr/bin/env python3

""" EUDAT Core metadata schema validation test script

    This script validates all metadata examples with the EUDAT Core metadata schema definition.

"""

import os
import sys
import xmlschema

# EUDAT_SCHEMA_VERSION = '1.0'
EXAMPLES_FOLDER = 'examples'

for level in ['core', 'extended']:
    # schema = "eudat-%s-%s.xsd" % (level, EUDAT_SCHEMA_VERSION)
    schema = f"eudat-{level}.xsd"

    if not os.path.exists(schema):
        print('skipping schema %s' % schema)
        continue

    print("schema %s:" % schema)

    # load schema
    schemadoc = xmlschema.XMLSchema11(schema)

    # load examples
    for f in sorted(os.listdir(EXAMPLES_FOLDER)):
        if not f.endswith(".xml"):
            continue
        if level != "extended" and not f.startswith(level):
            continue

        sys.stdout.write("validating %s" % f)

        schemadoc.validate("%s/%s" % (EXAMPLES_FOLDER, f))

        sys.stdout.write("\rvalidating %s .. OK\n" % f)

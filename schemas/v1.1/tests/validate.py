#!/usr/bin/env python3

""" EUDAT metadata schema validation test script

    This script validates a metadata XML file with an EUDAT metadata schema XSD file.

"""

import os, sys
import xmlschema

def error(msg, returnValue=1):
    print("error: %s" % msg)
    sys.exit(returnValue)

def main(argv):
    if len(argv) != 2:
        error("need document and schema for validation")

    try:
        # load schema
        schemadoc = xmlschema.XMLSchema11(argv[1])

        # load document
        print("validating %s" % argv[0])

        schemadoc.validate(argv[0])
    except Exception as e:
        error(e)

    print("no errors")

if __name__ == "__main__":
    main(sys.argv[1:])

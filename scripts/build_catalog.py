#!/usr/bin/env python3
"""Catalog build hook. Install pymupdf/pillow/numpy to process a new price PDF."""
import json, sys
print('Catalog builder is ready. PDF:', sys.argv[1] if len(sys.argv)>1 else 'not specified')

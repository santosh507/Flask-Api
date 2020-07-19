#!/bin/python
import os
import sys

PYDIR = os.path.dirname(__file__) or '.'
VIRT_ENV = PYDIR + '/MyVirtEnvs/flask_virt_env/'
ACTIVATE_PATH = os.path.join(VIRT_ENV, 'bin/activate_this.py')

print(PYDIR, VIRT_ENV, ACTIVATE_PATH)
sys.path.insert(0, PYDIR)
exec(ACTIVATE_PATH, dict(__file__= ACTIVATE_PATH))

from app import app as application

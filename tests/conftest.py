"""Configuration file for the test suite"""

import os
import sys

# set the system path to contain the previous directory
# because it is the root directory that contains the
# directory for the package, sub-packages, and modules
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")

import matplotlib.pyplot as plt
import numpy as np
import h5py
import copy
from pyebsdindex import ebsd_pattern, ebsd_index, pcopt, tripletlib
from pyebsdindex.EBSDImage import IPFcolor
from pathlib import *
import os

test_lib=tripletlib.triplib(libType="generic",phaseName='Mg',dataPath=Path('/home/mz071159/kikuchipy/PyEBSDIndex'))
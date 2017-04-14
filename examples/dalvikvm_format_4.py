#!/usr/bin/env python

from __future__ import print_function
import sys

PATH_INSTALL = "./"
sys.path.append(PATH_INSTALL)

from anguard.core.bytecodes import dvm
from anguard.core.analysis import analysis
from anguard.decompiler import decompiler
from anguard.util import read

TEST = "examples/android/TestsAnguard/bin/classes.dex"

j = dvm.DalvikVMFormat(read(TEST, binary=False))
jx = analysis.VMAnalysis(j)

#d = decompiler.DecompilerDex2Jad( j )
#d = decompiler.DecompilerDed( j )
d = decompiler.DecompilerDAD(j, jx)

j.set_decompiler(d)

# SHOW METHODS
for i in j.get_methods():
    if i.get_name() == "onCreate":
        print(i.get_class_name(), i.get_name())
        i.source()

#    if i.get_name() == "testWhileTrue":
#        i.source()
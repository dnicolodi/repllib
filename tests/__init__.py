import os
import sys
from test.support import requires
from test.support.import_helper import import_module

if sys.platform != "win32":
    # On non-Windows platforms, testing pyrepl currently requires that the
    # 'curses' resource be given on the regrtest command line using the -u
    # option.  Additionally, we need to attempt to import curses and readline.
    requires("curses")
    curses = import_module("curses")

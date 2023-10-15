import cx_Freeze
import sys
import os
base = None

if sys.platform == "win32":
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"F:\program file\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"F:\program file\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Clock.py", base=base, icon="clock.ico")]


cx_Freeze.setup(
    name = "Digital Clock",
    options = {"build_exe_installer": {"packages":["tkinter","os"], "include_files":["clock.ico", 'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
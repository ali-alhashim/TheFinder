from cx_Freeze import setup, Executable
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.
    

executables = [Executable("TheFinder.py", base=base, icon="Treetog-I-Search.ico")]

packages = ["idna"]

options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "TheFinder",
    options = options,
    version = "1.0",
    description = 'for Backup',
    executables = executables

)
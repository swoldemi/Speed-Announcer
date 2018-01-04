import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys", "queue", "idna"], "excludes": ["tkinter"]}

setup(  name = "Speed Announcer",
        version = "0.12",
        description = "A program to post my internet speed to Twitter",
        options = {"build_exe": build_exe_options},
        executables = [Executable("src/PostSpeed.py")])
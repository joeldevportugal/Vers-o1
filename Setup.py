import sys
from cx_Freeze import setup, Executable

# Dependências
build_exe_options = {"packages": ["tkinter", "pyperclip", "threading"], "include_files": ["C:\\Users\\HP\\Desktop\\Python tkinter\\Selector versões\\Versão 1\\Icon\\icon.ico"]}

# Executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Selector de Cores Versão1",
    version = "1.0",
    description = "Selector cores para defenir cores Hexadecimal",
    options = {"Versão1_exe": build_exe_options},
    executables = [Executable("Versão1.py", base=base, icon="C:\\Users\\HP\\Desktop\\Python tkinter\\Selector versões\\Versão 1\\Icon\\icon.ico")]
)

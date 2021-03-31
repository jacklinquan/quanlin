# Setup a Python study environment on Windows

:material-tag-multiple: :
`powershell` `python` `virtual environment` `thonny`


## PowerShell

- Download PowerShell zip file (e.g. `PowerShell-7.1.2-win-x64.zip`) from:
https://github.com/PowerShell/PowerShell/releases

- Unzip it to a folder (e.g. `PATH_TO_POWERSHELL = C:\venvs\PowerShell-7.1.2-win-x64`)

- Make a shortcut of `pwsh.exe` and set a start folder


## Python

- Install Python (e.g. `v3.7.8`) from:
https://www.python.org/downloads

- Run PowerShell and check Python version and `pip` version, upgrade `pip` if needed:
``` powershell
python --version
pip --version
```


## Virtual environment for study

- Use `venv` module to make a virtual environmnet and `cd` to it:
(e.g. `PATH_TO_VENV = C:\venvs\venv37_thonny`)
``` powershell
python -m venv PATH_TO_VENV
cd PATH_TO_VENV
```

- Make a `.bat` file (e.g. `powershell.bat`) for easy startup:
(e.g. `PATH_TO_POWERSHELL = C:\venvs\PowerShell-7.1.2-win-x64`)
``` batch
start PATH_TO_POWERSHELL\pwsh.exe -NoExit PATH_TO_VENV\Scripts\Activate.ps1
```


## Thonny

- Run `powershell.bat` and in the virtual environment use `pip` to install Thonny:
``` powershell
pip install thonny
```

- Make a `.bat` file (e.g. `thonny.bat`) for easy Thonny startup:
``` batch
start PATH_TO_VENV\Scripts\pythonw.exe -m thonny
```

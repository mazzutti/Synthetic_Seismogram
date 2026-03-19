# Synthetic_Seismogram
In reflection seismology, synthetic seismogram is based on convolution theory. Seismograms are very important tool for seismic interpretation where they work as a bridge between well and surface seismic data. In this post, I have tried to show how we can implement this task in some lines of code with real data in python. 
You may read some point about it here: https://towardsdatascience.com/generating-synthetic-seismogram-in-python-519f23f07894

## Windows: VS Code + Python — Step-by-step

Follow these steps to set up and run the project on Windows using Visual Studio Code.

1. Install Visual Studio Code
	- Download VS Code for Windows from https://code.visualstudio.com/ and run the installer.

2. Install the Python extension (ms-python)
	- Open VS Code, go to the Extensions view (Ctrl+Shift+X), search for "Python" by Microsoft, and install it.

3. Clone this repository
	- Open a terminal (PowerShell or Command Prompt) and run:

```powershell
git clone https://github.com/mazzutti/Synthetic_Seismogram.git
cd Synthetic_Seismogram
```

You can also use the SSH URL if you have SSH keys configured:

```powershell
git clone git@github.com:mazzutti/Synthetic_Seismogram.git
cd Synthetic_Seismogram
```

4. Create and activate the virtual environment, and install dependencies
	- From the repository root run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or
.\.venv\Scripts\activate.bat   # Command Prompt
python create_venv_and_install.py
```

The `create_venv_and_install.py` script will install the required packages listed for this project.

5. Configure VS Code to use the created virtual environment
	- Open the project folder in VS Code (`File > Open Folder...`).
	- Open the Command Palette (Ctrl+Shift+P) and run `Python: Select Interpreter`.
	- Choose the interpreter from the `.venv` folder (it will look like `.venv\Scripts\python.exe`).

5.a (optional) Configure interpreter in workspace settings
	- To make the workspace always use the created `.venv`, add a workspace setting file at `.vscode/settings.json` with the interpreter path.
	- Example for Windows (use backslashes):

```json
{
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}
```
	- Example for macOS / Linux (use forward slashes):

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python"
}
```
	- After adding the file, reload the window (`Developer: Reload Window`) or re-open the folder.

	- Notes:
	  - Recent versions of the Python extension prefer `python.defaultInterpreterPath` for workspace defaults. If your extension version still shows `python.pythonPath`, you can set that key instead for backward compatibility.
	  - You can also set the interpreter from the Command Palette with `Python: Select Interpreter` which will write the appropriate workspace setting automatically.

6. Open and run the notebook
	- Open `Synthetic_Seismogram.ipynb` in VS Code.
	- In the top-right of the notebook editor, use the kernel selector to choose the Python interpreter from the `.venv` you created.
	- Run cells using the run buttons or `Run All` to execute the notebook.

Notes
- If PowerShell blocks script execution, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in an elevated PowerShell first.
- If you prefer conda, create and activate a conda env and then select its interpreter in VS Code instead of `.venv`.


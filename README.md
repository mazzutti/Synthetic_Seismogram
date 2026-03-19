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

6.a Debugging and setting breakpoints inside notebook cells
	- Ensure the Python extension is installed and the notebook kernel is set to the `.venv` interpreter.
	- To set a breakpoint: open the code cell, click in the left gutter next to the line where you want execution to stop. A red dot indicates the breakpoint.
	- Start a debugging session for a cell by clicking the cell's "Debug Cell" button (the debug/butterfly icon) or right-click the cell and choose `Debug Cell`.
	- Use the Debug toolbar (Step Over / Step Into / Continue / Restart / Stop) and the Debug Console to inspect variables and walk through execution.
	- Alternatively, use "Run by Line" for quick step-through execution without breakpoints (click the Run By Line icon in the cell toolbar).
	- If you prefer an inline approach, add `import pdb; pdb.set_trace()` inside a cell — execution will drop to the debugger when that line runs (useful when remote debugging or the VS Code UI isn't available).
	- Notes:
	  - Debugging support depends on the Python extension and the selected kernel; if the debug buttons do not appear, update the extension and ensure the kernel is an interpreter from a local environment (not a remote kernel).
	  - You can also right-click a notebook cell and choose `Run Current Cell in Interactive Window`, then use the Interactive Window's debug controls.

Notes
- If PowerShell blocks script execution, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in an elevated PowerShell first.
 - If PowerShell blocks script execution, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in an elevated PowerShell first.
 - If you prefer conda, create and activate a conda environment and then select its interpreter in VS Code instead of `.venv`.
	- Example:

```powershell
conda create -n synthetic_seis python=3.10 -y
conda activate synthetic_seis
```

	- Install project requirements inside the conda env. Two common options:

	  1. Install using `pip` from the provided `requirements.txt`:

```powershell
pip install -r requirements.txt
```

	  2. Prefer conda packages where available (faster, binary builds), then fall back to `pip`:

```powershell
conda install numpy scipy matplotlib -y   # install common packages via conda
pip install -r requirements.txt          # install remaining packages via pip
```

	- After installing, open VS Code and use `Python: Select Interpreter` to choose the conda environment's interpreter (it will show as `conda: synthetic_seis` or point to the env path).


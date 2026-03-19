# Synthetic_Seismogram

In reflection seismology, a **synthetic seismogram** is based on convolution theory. Seismograms are a very important tool for seismic interpretation, acting as a bridge between well logs and surface seismic data.

In this repository, I demonstrate how to implement this task in a few lines of Python code using real data.

> [!TIP]
> You can read more about the theory and implementation here: [Generating Synthetic Seismogram in Python](https://towardsdatascience.com/generating-synthetic-seismogram-in-python-519f23f07894)

## 🛠 Windows: VS Code + Python — Step-by-step

Follow these steps to set up and run the project on Windows using Visual Studio Code.

### 1. Install Visual Studio Code

* Download VS Code for Windows from [code.visualstudio.com](https://code.visualstudio.com/) and run the installer.

### 2. Install the Python Extension

* Open VS Code, go to the **Extensions** view (`Ctrl+Shift+X`), search for **"Python"** by Microsoft, and install it.

### 3. Clone this Repository

Open a terminal (PowerShell or Command Prompt) and run:

```powershell
git clone [https://github.com/mazzutti/Synthetic_Seismogram.git](https://github.com/mazzutti/Synthetic_Seismogram.git)
cd Synthetic_Seismogram
```

*Note: You can also use the SSH URL if you have SSH keys configured:*
`git clone git@github.com:mazzutti/Synthetic_Seismogram.git`

### 4. Create and Activate Virtual Environment

From the repository root, run:

```powershell
# Create environment
python -m venv .venv

# Activate environment (PowerShell)
.\.venv\Scripts\Activate.ps1   

# OR Activate environment (Command Prompt)
.\.venv\Scripts\activate.bat   

# Install dependencies
python create_venv_and_install.py
```

The `create_venv_and_install.py` script will install the required packages listed for this project.

### 5. Configure VS Code Interpreter

* Open the project folder in VS Code (`File > Open Folder...`).
* Open the **Command Palette** (`Ctrl+Shift+P`) and run `Python: Select Interpreter`.
* Choose the interpreter from the `.venv` folder (it will look like `.venv\Scripts\python.exe`).

#### 5.a (Optional) Workspace Settings

To force the workspace to always use the created `.venv`, add a file at `.vscode/settings.json`:

**Windows:**

```json
{
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}
```

**macOS / Linux:**

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python"
}
```

### 6. Open and Run the Notebook

* Open `Synthetic_Seismogram.ipynb` in VS Code.
* In the top-right of the notebook editor, use the **Kernel Selector** to choose the Python interpreter from the `.venv` you created.
* Run cells using the play buttons or **Run All**.

#### 6.a Debugging inside Notebook Cells

* **Breakpoints:** Click in the left gutter next to a line number to set a red dot.
* **Debug Cell:** Click the "Debug Cell" button (butterfly icon) or right-click the cell and choose `Debug Cell`.
* **Run by Line:** Use the "Run by Line" icon in the cell toolbar for quick step-through.

## 📝 Notes

* **Execution Policy:** If PowerShell blocks script execution, run:
  `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in an elevated PowerShell first.

* **Conda Alternative:** If you prefer Conda, create and activate an environment, then select its interpreter in VS Code:

```powershell
conda create -n synthetic_seis python=3.10 -y
conda activate synthetic_seis

# Option 1: Install via pip
pip install -r requirements.txt

# Option 2: Mixed install (Faster binary builds)
conda install numpy scipy matplotlib -y
pip install -r requirements.txt
```

* After installing, use `Python: Select Interpreter` to choose the Conda environment (it will show as `conda: synthetic_seis`).
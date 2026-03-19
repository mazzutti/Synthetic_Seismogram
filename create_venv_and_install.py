#!/usr/bin/env python3
"""Create a virtual environment and install requirements.

Usage examples:
  python3 create_venv_and_install.py            # create .venv and install
  python3 create_venv_and_install.py --env env  # create ./env
  python3 create_venv_and_install.py --dry-run  # print actions but don't execute
"""

import argparse
import os
import shutil
import subprocess
import sys


def run(cmd, dry_run=False):
    print("+ "+" ".join(cmd))
    if not dry_run:
        subprocess.check_call(cmd)


def pip_executable(env_dir):
    if os.name == "nt":
        return os.path.join(env_dir, "Scripts", "pip.exe")
    return os.path.join(env_dir, "bin", "pip")


def python_executable(env_dir):
    if os.name == "nt":
        return os.path.join(env_dir, "Scripts", "python.exe")
    return os.path.join(env_dir, "bin", "python")

def main():
    p = argparse.ArgumentParser(description="Create venv and install requirements")
    p.add_argument("--env", default=".venv", help="virtualenv directory (default: .venv)")
    p.add_argument("--requirements", default="requirements.txt", help="requirements file")
    p.add_argument("--recreate", action="store_true", help="remove and recreate the venv if it exists")
    p.add_argument("--dry-run", action="store_true", dest="dry_run", help="show commands without running them")
    args = p.parse_args()

    env_dir = args.env
    req_file = args.requirements

    if not os.path.isfile(req_file):
        print(f"ERROR: requirements file not found: {req_file}")
        sys.exit(1)

    if os.path.exists(env_dir):
        if args.recreate:
            print(f"Removing existing venv: {env_dir}")
            if not args.dry_run:
                shutil.rmtree(env_dir)
            print(f"Creating virtual environment: {env_dir}")
            run([sys.executable, "-m", "venv", env_dir], dry_run=args.dry_run)
        else:
            print(f"Using existing venv: {env_dir}")
    else:
        print(f"Creating virtual environment: {env_dir}")
        run([sys.executable, "-m", "venv", env_dir], dry_run=args.dry_run)

    pip_path = pip_executable(env_dir)

    print("Upgrading pip and ensuring setuptools (compatible) inside venv")
    run([pip_path, "install", "--upgrade", "pip", "setuptools<70.0.0", "wheel"], dry_run=args.dry_run)

    print(f"Installing from {req_file}")
    run([pip_path, "install", "-r", req_file], dry_run=args.dry_run)

    print("Registering the virtual environment as a Jupyter kernel...")
    python_path = python_executable(env_dir)
    run([python_path, "-m", "ipykernel", "install", "--user", "--name", "synthetic-seismogram", "--display-name", "Python (.venv Synthetic Seismogram)"], dry_run=args.dry_run)

    print("Done. To activate the venv in this shell:")
    if os.name == "nt":
        print(f"  {env_dir}\\Scripts\\activate")
    else:
        print(f"  source {env_dir}/bin/activate")


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as e:
        print("Command failed:", e)
        sys.exit(e.returncode)

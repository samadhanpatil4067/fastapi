import importlib
import subprocess
import sys
import re

def install_missing_modules(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    # Find imports
    modules = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_]+)', code, re.MULTILINE)

    for module in set(modules):
        try:
            importlib.import_module(module)
            print(f"{module} already installed ✅")
        except ImportError:
            print(f"{module} not found, installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# # Example usage
# install_missing_modules("your_script.py")

import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(sys.version)
print(sys.platform)
print(sys.executable)
print(ROOT_DIR)
print(os.path.dirname(sys.modules['__main__'].__file__))

response = subprocess.run(sys.executable + " --version1", shell=True, cwd=ROOT_DIR, check=True)
print(response.returncode)

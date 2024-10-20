import sys
import os

# Get the absolute path to the root directory (KARPENKO1)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the root directory to the sys.path
sys.path.insert(0, project_root)

# Now import the module
from myprojects.module2 import deep_translate

# Test the function
print(deep_translate("Привіт, світ!", "en"))
# content of conftest.py
import sys

collect_ignore = ["setup.py"]
if sys.version_info[0] > 2:
   collect_ignore.append("pkg/module_py2.py")

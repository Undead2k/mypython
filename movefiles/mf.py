import os
import shutil
import sys

start = sys.argv[1]

result = [shutil.move(str(root) + "\\" + x, start) for root, subdir, file in os.walk(start) if file for x in file]





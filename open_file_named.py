import pathlib
import re
import os
import subprocess
EDITOR = os.environ.get('EDITOR', 'vim')

start_path = input()
regex = input()
def find_file_named(path):
    list_dir = os.listdir(path)
    for i in list_dir:
        if(os.path.isfile(path + "/" + i)):
            if re.search(regex, i):
               subprocess.call([EDITOR, path + "/" + i])
        else:
            find_file_named(path + "/" + i)

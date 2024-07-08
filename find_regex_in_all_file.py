import pathlib
import re
import os

start_path = input()
regex = input()
def find_regex_in_all_file(path, regex):
    list_dir = os.listdir(path)
    for i in list_dir:
        if(os.path.isfile(path + "/" + i)):
            with open(path + "/" + i, encoding = "ISO-8859-1") as file:
                if(not file.name.endswith(".class")):
                    for line in file:
                        if re.search(regex, line):
                            print(i)
                            break
                        else:
                            continue
                else:
                    continue
        else:
            find_regex_in_all_file(path + "/" + i, regex)
    return
find_regex_in_all_file(start_path, regex)

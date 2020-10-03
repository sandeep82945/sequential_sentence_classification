
from shutil import copyfile
import os

git_dir = os.path.join("git", "allennlp")
allen_dir = os.path.join("src", "allennlp")

f = open("filelist.txt")
file_contents = f.read()
contents_split = file_contents.splitlines()
f.close()

for file in contents_split:
    
    src = os.path.join(git_dir, file) 
    if file != "" and os.path.exists(src):
        dest = os.path.join(allen_dir, file)
        copyfile(src, dest)


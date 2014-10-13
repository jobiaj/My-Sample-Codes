import sys
import re
import os
import shutil
import commands
def get_special_paths(dir_name):
	paths = []
	files = os.listdir(dir_name)
	for i in files:
		special = re.search(r'__(\w+\w+)__',i)
		if special:
			paths.append(os.path.abspath(i))

	return paths

print get_special_paths('/home/jobi/Recursive/google-python-exercises/copyspecial')

def copy_to(paths,dirr):
	paths = get_special_paths(dirr)
	if not os.path.exists(dirr):
		os.mkdir(dirr)
	for path in paths:
		shutil.copy(path,os.path.abspath(dirr))
	
def zip_to(paths,dirr):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


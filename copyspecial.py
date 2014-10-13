import sys
import re
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


def copy_to(path,directory):
	efile=get_special_path(path)
	if not os.path.exists(directory):
		os.mkdir(directory)
	for each_file in efile:
		shutil.copy(each_file,os.path.abspath(directory))

def zip_to(path,zippath):
	efile = get_special_path(path)
	for each_file in efile:
		cmd = 'zip -j'+' '+ zippath+' '+ each_file
		asd=commands.getstatusoutput(cmd)
 

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  print args
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
#    del args[0:2]
    path=args[2]
    copy_to(path,todir)
    del args[0:2]
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    path=args[2]
    zip_to(path,tozip)
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()

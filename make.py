import os
import sys

import posixpath

"""

Usage python make.py <source_directory> <apidoc_target> <html build target>

<apidoc_target> and <html build target> are optional arguments

"""

command = list()
arg_length = len(sys.argv)

if arg_length < 2:
    raise ValueError("Please specify the source directory")
source_directory = sys.argv[1]
if arg_length >= 3:
    apidoc_directory = sys.argv[2]
else:
    apidoc_directory = './apidoc'

if arg_length == 4:
    html_directory = sys.argv[3]
else:
    html_directory = './_build'

package_list = ['pyiron', 'pyiron_vasp', 'pyiron_base', 'pyiron_atomistics', 'pyiron_lammps']

command.append("make clean")
for pkg in package_list:
    directory = posixpath.join(source_directory, pkg)
    command.append("sphinx-apidoc -f -o {} {}".format(apidoc_directory, directory))

# command.append("make html")

#command.append('sphinx-build -b html ./ {}'.format(html_directory))

command.append('make html')

for i in range(len(command)):
    os.system(command[i])

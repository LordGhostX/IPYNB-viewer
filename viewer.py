from nbconvert import HTMLExporter
from random import randint
import os
import sys
import nbformat
import tempfile
import webbrowser

__author__ = "LordGhostX"
__version__ = "1.0.0"


tmpdir = tempfile.gettempdir()
ipynbdir = os.path.join(tmpdir, "ipynbdir")
if not os.path.isdir(ipynbdir):
    os.mkdir(ipynbdir)

def print_help():
    print ("""usage: ipynbv [ipynb file]
IPYNB (Jupyter Notebook) File Viewer
Instantly view IPYNB (Jupyter Notebook) files without having to fire up Anaconda or Jupyter.

additional arguments:
    -h, --help  show this help message and exit
    --version   show program's version number and exit""")


def create_html(filename):
    while True:
        file_name = filename.split(".")
        htmlfile = os.path.join(ipynbdir, file_name[0] + "-" + str(randint(45448, 58595859)) + ".html")
        if not os.path.exists(htmlfile):
            break
    nb = nbformat.read(filename, as_version=4)
    html_exporter = HTMLExporter()
    # html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(nb)
    print(resources)
    with open(htmlfile, "w") as f:
        f.write(body)
        f.close()
    return htmlfile

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print_help()
        elif sys.argv[1] == "--version":
            print("IPYNB Viewer", __version__)
        else:
            nbfile = sys.argv[1]
            htmlfile = create_html(nbfile)
            w = webbrowser.open_new_tab(htmlfile)
    else:
        print_help()

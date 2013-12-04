
import glob
import os
import vim

from tessera import GitTessera
from vim import current, buffers
from ConfigParser import ConfigParser

class tessera:
    def __init__(self, directory = "."):
        self.directory = directory
        config = ConfigParser()
        src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "vimtessera.config")
        config.read(src)
        self.te = GitTessera(config)

    def list(self):
        self.files = self.te.ls()
        self.index = 0
        vim.command(":e " + vim.eval("tempname()"))
        _display(self.files)
        vim.command(":nmap <Enter> :py tessera.open()<Enter>")

    def next(self):
        vim.command(":e %s" % self.files[self.index])
        self.index += 1

    def open(self):
        (row, col) = vim.current.window.cursor
        vim.command(":e %s" % self.files[ row - (len(_headline) + 1) ].filename)
        vim.command(":set nomodifiable")
        vim.command(":nmap q :bd<Enter>")


def _highlight():
    vim.command(":hi def TEid ctermfg=darkblue")
    vim.command(":hi def TEtitle ctermfg=darkgreen")
    vim.command(":syn match TEid '^[^ ]\+'")
    vim.command(":syn match TEtitle ' .\+$'")

_headline = [ "# Welcome to vim-tessera",
              "# ",
              "# place the cursor over a Tessera and press enter to open it",
              "# "
            ]

def _display(files):
    """ displays the {files} Tesserae in the current buffer
    """
    del vim.current.buffer[0:len(vim.current.buffer)]
    vim.current.buffer[0:len(_headline)] = _headline
    for t in files:
        ident = t.ident()
        vim.current.buffer.append("%s %s" % ( ident['ident'], ident['title'] ) )
    vim.command(":w")
    vim.command(":set nomodifiable")
    _highlight()


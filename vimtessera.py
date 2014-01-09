
import glob
import os
import vim

from tessera import GitTessera, Tessera, TesseraConfig
from dulwich.errors import NotGitRepository
from vim import current, buffers
from ConfigParser import ConfigParser

class tessera:
    def __init__(self, directory = "."):
        self._tesserae = os.path.relpath(os.path.join(directory, ".tesserae"))
        config = TesseraConfig(os.path.join(self._tesserae, "config"))
        try:
          self.te = GitTessera(config)
        except NotGitRepository:
          self.te = None
        self.t = None

    def list(self):
        if not self.te:
          return
        self.files = self.te.ls()
        self.index = 0
        vim.command(":e " + vim.eval("tempname()"))
        _display(self.files)
        vim.command(":nmap <Enter> :py tessera.open()<Enter>")

    def next(self):
        if not self.te:
          return
        vim.command(":e %s" % self.files[self.index])
        self.index += 1

    def open(self):
        if not self.te:
          return
        (row, col) = vim.current.window.cursor
        vim.command(":e %s" % self.files[ row - (len(_headline) + 1) ].filename)
        vim.command(":set nomodifiable")
        vim.command(":nmap q :bd<Enter>")

    def create(self, title):
        if not self.te:
          return
        Tessera._tesserae = self._tesserae
        self.t = self.te.create() if title is "" else self.te.create(title)
        vim.command(":e " + self.t.filename)

    def commit(self):
        if not self.te:
          return
        if self.t is None:
            return
        vim.command(":w")
        self.te.commit(self.t)

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
    vim.command(":set modifiable")
    del vim.current.buffer[0:len(vim.current.buffer)]
    vim.current.buffer[0:len(_headline)] = _headline
    for t in files:
        ident = t.ident()
        vim.current.buffer.append("%s %s" % ( ident['ident'], ident['title'] ) )
    vim.command(":w")
    vim.command(":set nomodifiable")
    _highlight()


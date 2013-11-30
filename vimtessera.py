
import glob
import vim
from tessera import GitTessera
from vim import current, buffers

def _highlight():
    vim.command(":hi def TEid ctermfg=darkblue")
    vim.command(":hi def TEtitle ctermfg=darkgreen")
    vim.command(":syn match TEid '^[^ ]\+'")
    vim.command(":syn match TEtitle ' .\+$'")

class tessera:
    def __init__(self, directory = "."):
        self.directory = directory
        self.te = GitTessera()

    def list(self):
        self.files = self.te.ls()
        self.index = 0
        vim.command(":e " + vim.eval("tempname()"))
        for t in self.files:
            ident = t.ident()
            vim.current.buffer.append("%s %s" % ( ident['ident'], ident['title'] ) )
        vim.command(":w")
        vim.command(":set nomodifiable")
        _highlight()
        vim.command(":nmap <Enter> :py tessera.open()<Enter>")

    def next(self):
        vim.command(":e %s" % self.files[self.index])
        self.index += 1

    def open(self):
        (row, col) = vim.current.window.cursor
        vim.command(":e %s" % self.files[ row - 2 ].filename)
        vim.command(":set nomodifiable")
        vim.command(":nmap q :bd<Enter>")


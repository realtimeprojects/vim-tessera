
import glob
import vim
from tessera import GitTessera
from vim import current, buffers

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
        vim.command(":set nomodifiable")
        vim.command(":set nomodified")

    def next(self):
        vim.command(":e %s" % self.files[self.index])
        self.index += 1


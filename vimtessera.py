
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
        for t in self.files:
            print(t.data())

    def next(self):
        vim.command(":e %s" % self.files[self.index])
        self.index += 1


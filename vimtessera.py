
import glob
import vim
from vim import current, buffers

class tessera:
    def __init__(self, directory = "."):
        self.directory = directory

    def list(self):
        """ clean radish highlights in current buffer
        """
        self.files = glob.glob(".tesserae/*/tessera")
        self.index = 0
        return self.files

    def next(self):
        vim.command(":e %s" % self.files[self.index])
        self.index += 1



import glob
import vim
from vim import current, buffers

def list():
    """ clean radish highlights in current buffer
    """
    files = glob.glob(".tesserae/*/tessera")
    print("files: %s" % files)


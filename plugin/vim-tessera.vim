com! -b -nargs=* TElist :py tessera.list()
com! -b -nargs=* TEnext :py tessera.next()

if !has('python')
    echoe 'vim-radish No python support available.'
    echoe 'Compile vim with python support to use vim-tessera'
    exit
endif

" Only parse the python library once
let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
if !exists('s:vimtessera_loaded')
    python import sys
    exe 'python sys.path = ["' . s:plugin_path . '/.."] + sys.path'

    python import vimtessera
    python tessera = vimtessera.tessera()

    let s:vimradish_loaded = 1
endif


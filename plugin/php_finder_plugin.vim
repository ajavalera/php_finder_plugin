if !has("python3")
    echo "php_finder_plugin will not work without python3 support... Sorry..."
    finish
endif

if exists('g:php_finder_plugin')
    echo "Other library called php_finder_plugin is installed. It's her or me!!"
    finish
endif

" Setting global commodity variables
let g:php_finder_plugin_path = expand("<sfile>:p:h")

" Add this library python modules into the system path.
function! PhpFinderPlugin()
python3 << endpython

import os
import sys
import vim

plugin_path = vim.eval("g:php_finder_plugin_path")
python_module_path = os.path.abspath('%s/../python' % (plugin_path))
sys.path.append(python_module_path)

endpython
endfunction

function! FindmeMethods()
python3 << endpython

import findInFile

file_path = vim.eval('expand("%:p")')
methods = findInFile.methods(file_path)

if 0 == len(methods):
    print("No methods where found, my master...")

for key in methods:
    print(key + " methods " + "----")
    for method in methods[key]:
        print(method)

endpython
endfunction

call PhpFinderPlugin()
let g:php_finder_plugin = 1

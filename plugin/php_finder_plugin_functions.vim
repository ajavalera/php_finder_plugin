" Functions
" Holds all the functions defined by the php_finder_plugin.

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

call PhpFinderPlugin()

" Finds methods in the current file.
function! FindmeMethods()
python3 << endpython
import findinfile

file_path = vim.eval('expand("%:p")')
methods = findinfile.methods(file_path)

if 0 == len(methods):
    print("No methods where found, my master...")

for key in methods:
    print(key + " methods " + "----")
    for method in methods[key]:
        print(method)

endpython
endfunction

" Finds usage of string in files in path.
command! -nargs=+ Findmeusage call FindmeUsage(<f-args>)
function! FindmeUsage(needle, path)
python3 <<endpython
import findinfile

needle = vim.eval("a:needle")
path = vim.eval("a:path")

hitlist = findinfile.find_usage(path, needle, [])

vim.command("botright new")
vim.command("setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap")

for line in hitlist:
    vim.command("normal 0i" + line)
    vim.command("normal o")

vim.command("normal gg")
endpython
endfunction

" Finds class in files in path.
command! -nargs=+ Findmeclass call FindmeClass(<f-args>)
function! FindmeClass(classname, path)
python3 <<endpython
import findinfile

needle = 'class ' + vim.eval("a:classname")

path = vim.eval("a:path")

classlist = findinfile.find_usage(path, needle, [])

vim.command("botright new")
vim.command("setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap")

for line in classlist:
    vim.command("normal 0i" + line)
    vim.command("normal o")

vim.command("normal gg")
result = []
endpython
endfunction

" Finds class in files in path.
command! -nargs=+ Findmethismethod call FindmeThisMethod(<f-args>)
function! FindmeThisMethod(methodname, path)
python3 <<endpython
import findinfile

needle = 'function ' + vim.eval("a:methodname")

path = vim.eval("a:path")

methodslist = findinfile.find_usage(path, needle, [])

vim.command("botright new")
vim.command("setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap")

for line in methodslist:
    vim.command("normal 0i" + line)
    vim.command("normal o")

vim.command("normal gg")
endpython
endfunction

command! -nargs=+ Findmethisnamespace call FindmeThisNamespace(<f-args>)
function! FindmeThisNamespace(subject, path)
python3 <<endpython
import findinfile

needle = "namespace " + vim.eval("a:subject")
path = vim.eval("a:path")

hitlist = findinfile.find_usage(path, needle)

vim.command("botright new")
vim.command("setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap")

for line in hitlist:
    vim.command("normal 0i" + line)
    vim.command("normal o")

vim.command("normal gg")
endpython
endfunction

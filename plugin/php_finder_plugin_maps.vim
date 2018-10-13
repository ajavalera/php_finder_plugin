" Maps file.
" All maps and short cuts defined by the php_finder_plugin.
"

"Open php file path in window on top. Used in conjunction with Findme methods.
noremap :oo 0vf:<left>y<c-w>k<leader>e <c-r>0<cr><c-w>j

"Insert the namespace of class in the path under `this` window's cursor
"in the position of cursor in the window above.  Used in conjunction with
"Findme methods
noremap :inn 0vf:<left>y<c-w>k<leader>Insertnamespace <c-r>0<cr><c-w>j

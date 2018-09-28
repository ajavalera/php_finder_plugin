if !has("python3")
    echo "php_finder_plugin will not work without python3 support... Sorry..."
    finish
endif

" Only load the library once.
if exists('g:php_finder_plugin')
    finish
endif

" Setting global commodity variables
let g:php_finder_plugin_path = expand("<sfile>:p:h")

execute("source " . expand("<sfile>:p:h") . "/php_finder_plugin_maps.vim")
execute("source " . expand("<sfile>:p:h") . "/php_finder_plugin_functions.vim")

let g:php_finder_plugin = 1

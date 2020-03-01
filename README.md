# denite-clipy

denite-clipy is denite extension which makes it easier to paste snippet from any directory.

## setting
set these variables in your vimscript.
|name|type|description|
|:--:|:--:|:--:|
|g:clipy_root|string|specify directory of your snippet|
|g:clipy_filetype|list|specify filetype of your snippet|

```vim
"example
let g:clipy_root = expand("~/snippet")
let g:clipy_filetype = {'cpp':['hpp','cpp'],'python':['py']}
```

When you set like above and edit cpp file, :Denite clipy command shows ~/snippet/**/*.(hpp|cpp).


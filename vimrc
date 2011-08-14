set nobackup

set helplang=cn

set encoding=utf-8

set nu

syntax enable
syntax on

set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set smarttab
set expandtab

set cinoptions={0,1s,t0,n-2,p2s,(03s,=.5s,>1s,=1s,:1s

set laststatus=2  
set statusline=%<%F%h%m%r\ [%{&ff}]\ [%{&fileencoding}]\ (%{strftime(\"%H:%M\ %d/%m/%Y\",getftime(expand(\"%:p\")))})%=%l,%c%V\ %P

if &term=="xterm"
    set t_Co=8
    set t_Sb=^[[4%dm
    set t_Sf=^[[3%dm
endif

"pydiction提供的自动补全
filetype plugin on
let g:pydiction_location='/usr/share/pydiction/complete-dict'
"default g:pydiction_menu_height == 15
"let g:pydiction_menu_height = 20

autocmd BufRead *.py set smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class


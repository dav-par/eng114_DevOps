[link to index](/readme.md)  

# vim
powerful text editor

## benefits 
- syntax highlighting
- available everywhere
- 

## modes
- command/normal mode
    - press esc
- extended command/line mode
    - type `:` in command mode
- insert mode
    - press i
        - edit text directly
    - press o
        - edit text starting at a new line
- replace mode
    - `shift-r`

## navigation
- `h` `j` `k` `l`
    - arrow keys
- `ctrl-f`
    - page up
- `ctrl-b`
    - page down
- `w` and `b`
    - forwards or backwards one word
- `shift-6`
    - first character in a line
- `gg` or `3G`
    - go to the first line in the file
- `G`/`:$`
    - go to the last line in the file
- `3gg`/`3GG`/`:3`
    - go to line 3
- `ctrl-w-w`
    - change window

## motions and operations
- `3dw`
    - number `3` is how many times to do the command that follows
    - first letter `d` is the motion
    - second letter `w` is the operation
- linewise
    - works on a whole line
-

## common commands
- `:q`
    - quit, exit file
- `:wq`
    - save/write file and quit
- `yy`
    - yank a line
-  `p` 
    - put/paste line
    - `P` put line above
- `dw`
    - delete word
- `dd`
    - delete line
- add `!` to force a command
- `ctrl-g`/`gG`
    - file info/more info
- `set <option>`
    - turns the option on or off
- `.`
    - repeat the previous command
- `x`
    - delete character
- `:help`
    - help menu
- `u`
    - undo
- `ctrl-r`
    - redo
- `fA`
    - goes to the first `A`
    - `;` repeats the search in the same direction
    - `,` repeats the search in the opposite direction
- `/and`
    - find next `and`
    - `n` to find next `and`
    - `N` find the previous `and`
- `:s/and/&`
    - substitutes `and` with `&` on the current line 
- `:%`
    - apply command to whole file
- `set: nu`
    - show line number
-  `:[range]s/{pattern}/{string}/[flags]
    - replaces the pattern with the string in the range specified
- `J`
    - join lines

## help
- `:help`
- navigation
    - `ctrl-o` back a page
    - `ctrl i` forwards a page

## registers
- `""`
    - unnamed
    - last bit of text from d, c, s, x, y
- `"1"`, `"2"` etc
    - numbered register with 0 first
- `__`
    - blackhole
- `"a"`, `"b"` etc
    - `a` register
- `"2`
    - access register `2`
    - `2"p` to put/paste register `2`
- append with captials
    - `"Jyy"`
        - add yanked line to register j

## text objects
-`{operator}a{object}`
    - `daw` delete a word
- `{operator}i{object}`
    - `ciw` change inner word
    -`ci]` change inside `[]` brackets 

## commands outside command mode
= shift and `zz`
    - save and quit
    - only if file already has a name

## vimtutor
- `vimtutor` to open
- teaches you how to use vim
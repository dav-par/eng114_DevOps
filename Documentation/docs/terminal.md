# Terminal

## Common directories
- `/` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Root  
- `/bin` &nbsp;&nbsp;&nbsp;&nbsp;- Binaries, executeable files
- `/etc` &nbsp;&nbsp;&nbsp;&nbsp;- System config files
- `/home` &nbsp;&nbsp;- Home directory, user accounts
- `/opt` &nbsp;&nbsp;&nbsp;&nbsp;- Optional and third party software thats not
- `/tmp` &nbsp;&nbsp;&nbsp;&nbsp;- Temp files, cleared every boot
- `/usr` &nbsp;&nbsp;&nbsp;&nbsp;- User related programs
- `/var` &nbsp;&nbsp;&nbsp;&nbsp;- Variable data, usually log files
- `/boot` &nbsp;&nbsp;- files for booting
- `/dev` &nbsp;&nbsp;&nbsp;&nbsp;- Device files

## Users
- `$` - User
- `#` - Superuser, root account
- `u` - user
- `g` - group
- `o` - other
- `a` - all

## common commands:
- `.` - all in current folder
- `cd ..` - go back a folder
- `ls` see files/folders
    - `-a` for all including hidden
    - `-l` for long list format
    - `-F` for file type
    - `-r` for reverse order
    - `-R` for recursive listing
    - `-t` sort by time
- `sudo` - as admin
- `sudo apt-get` `update` and `upgrade` - update fetches the latest version of the package list from your distro's software repository, and any third-party repositories you may have configured using the package manager `apt-get`
- `sudo apt-get install packagename -y` to install a package and skip the yes/no confirm
- `history` - see what you've typed so far
- `systemctl status packagename` - check the status of a package 
- `sudo systemctl stop packagename` - stop a package running as admin
- `who am i` - user details
- `uname` - os details, `-a` for all details
- `pwd` -  what folder are you in
- `cd ..` back a step
- `touch filename` - create a file called filename
- `nano filename` - create a file and go straight to editing
- `mv current_location new_location` - move files 
- `r` `w` `x` read, write, execute
- `ll` check file permissions
- `chmod` change permission `-x` make executable
- `rm -rf` delete file
- `hostname -I` check ip
- `cat` concatenates and displays files
- `echo` displays arguments on the screen
- `man` displays the manaual
- `mkdir` makes a directory, can use `-p`
- `rmdir` removes a directory, can use `-p`
- `rm -rf direcoty` rcursively removes a directory
- `find [path] [expresion]` looks for a file/directory in the path listed/ `locate` uses the index which is only generated after a period of time


## General tips
- use `tab` to auto complete
- `ctrl-x` or `ctrl-c` will quit most things
- `~` is short for home directory
- `enter` to see one more line in a page
- `spacebar` to see next page in list
- `-h` or `-help` for help
- there is no undoo or recyling bin
- symbolic links are 
- `.` dotfiles are hidden files
- avoid spaces in file names, use quotes if needed `"my notes.txt"`
- `*` and `?` are wild cards and good for finding files e.g. `find *.txt`


## Path
PATH is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user. It increases both the convenience and the safety of such operating systems and is widely considered to be the single most important environmental variable. 
- `echo $PATH` to see it
- controls the commmand search path
- contains a list of directories
- first in list has priority if there's two of the same executable 


## Bash Scripting  
Bash scrips are files you can write that run a sequence of tasks if they are allowed to exicute (+x)
- create a file with the extension .sh
- change permissions of this file `chmod +x filename.sh`
- first line `MUST BE` starting with `#!/bin/bash`
- [Special chars](howtogeek.com/439199/15-special-characters-you-need-to-know-for-bash/)

## chmod
- Uses octal numbers:
    - 4 - read
    - 2 - write
    - 1 - execute
- Add the sum of the numbers of the permissions you want to grant e.g 7 (4 + 2 + 1)
- Read, write, execute is 6 (4 + 2 + 1)
- Complete permissions are given as a three digit number
- Each digit corresponds to a context (owner, group, other)
    - e.g chmod 764 file1 (user = rwx, group = rw and others = read on file1)
    - chmod 700 file1 (user = rwx)
    - chmod 640 file1 (user = rw, group = r)
- https://linuxhandbook.com/chmod-calculator/

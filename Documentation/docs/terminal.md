# Terminal

## common commands:
- `.` - all in current folder
- `..` - go back a folder
- `ls` see files/folders `-a` for all including hidden
- `sudo` - as admin
- `sudo apt-get` `update` and `upgrade` - update fetches the latest version of the package list from your distro's software repository, and any third-party repositories you may have configured
- `sudo apt-get install packagename -y` to install a package and skip the yes/no confirm
- `history` - see what you've done so far
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

## General tips
- use tab to auto complete
- ctrl-x or ctrl-c will quit most things


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

## Linux

- `ls` , `-a` for all including hidden
- `sudo` - as admin
- `sudo apt-get update`
- `sudo apt-get upgrade`
- `sudo apt-get install nginx -y`
- `history`
- `sudo apt-get install nginx -y`
- `vagrant reload` = uses the new config file and keeps the up
- `systemctl status nginx` , go to config and 
- `sudo systemctl stop nginx` , go to a config and stop the package
- `who am i` - user details
- `uname -a` os details, -a for all details
- `pwd` , what folder are you in
- press tab to auto complete
- `cd ..` back a step
- `touch filename`
- `nano filename` - make and edit file
- `mv filename destination` - move file
- `r` `w` `x` read, write, exicute
- `ll` check file permissions
- `chmod` change permission `-x` make executable

chmod Absolute Mode

• Uses octal numbers.

- 4 = read

- 2 = write

- 1 = execute

• Add numbers of permissions you wish to grant.

- Sum of these is what you provide.

- Read, write, execute is 7 (4 + 2 + 1).

- Read, write is 6 (4 + 2).

• Complete permissions are expressed as three-digit number.

- Each digit corresponds to a context (owner, group, other).

• E.g. chmod 764 file1 (user = rwx, group = rw and others = read on file1)

           chmod 700 file1 (user = rwx)

           chmod 640 file1 (user = rw, group = r)
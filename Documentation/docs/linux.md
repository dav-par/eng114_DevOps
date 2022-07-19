[link to index](/readme.md)  

# Linux
kernel for open source os's
- Debian based
    - ubuntu
- Fedorda based
    - Redhat
    - centos

## kernel
heart of linux os
core components:
- resource allocation/scheduling of running programs
- file management
- security

## kernal space:
- device drivers run in the kernel
- networking is implemented in the kernel

## user space:
- programs e.g. shell, web browser 
- programs in user space interact with the kernel via special devices or system calls that they make

## processes
- a running program is called a process
- has its own virtual memory space
- a process runs as a user and a set of groups
- has a state
    - running
    - waiting to run
    - blocked
    
## daemon process
- not associated with the terminal
- started up by the system
- provide:
    - networking
    - special housekeeping tasks
    
## kernel threads
- part of the kernel running as if they were a regular user process or system daemons
- not associated with the terminal
- show in square brackets when running `ps -ef` e.g. `[rcu_gp]`

## other components
- bootloader
- application libraries
- package manager
- utilities and applications
- graphical user interface (gui)

## shell
- used to interface with the os and execute commands
- default is often bash

### users
- `$` - normal user
- `#` - root (admin user)

## arguments
- single dash means the option is an abbreviated form e.g. `-a`
- double dash means the option is meant to be interpreted as an entire word e.g. `--version`

## manual pages (manpages)
- gives information on how to execute commands and what they do
- accessed by `man` followed by the command e.g. `man crontab`
- `[ ]` gives us optional entities
    - you can only use one argument if several are inside the square brackets
- `...` (ellipsis) means you can make use of multiple options e.g. `ls file1 file2`

## users
a user has
- uid
    - user number
- gid
    - user primary group
- groups
    - supplementary groups

### commands
- useradd
- userdel
    - deletes the user but leaves the directory behind
- usermod
    - `-a` append
    - `-aG group_b user_a` add `user_a` to `group_b`
- groupapp
- `id user_b`
    - shows `user_b`'s info
- `passwd user_b`
    - change `user_b`'s password

## file permissions
![permissions](/Documentation/resources/linux/file_permissions.png)  
- files have 10 bits associated with them  
permissions are processed in order and stop as soon as a match is found
- first bit
    - `d` directory
    - `l` link
    - `b` block
    - `-` regular file
- next three
    - user who created the file 
- next three
    - the creating user's primary group
- next three
    - other users access
    - everyone who is not the owning user or in the primary group
- `ls -ld` to see permissions of a directory


### commands
- chmod to change ownership setting
    - `chmod u-rwx /common`
        - change the `u`ser ownership settings, removing `r`ead, `w`riting and `e`xecute permissions to `/common` for the owning user
- chown to change ownership group

## networking
- network-manager
- `nmcli` network manager command line interface 
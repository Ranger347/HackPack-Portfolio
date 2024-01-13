# OverTheWire Practice

## Prompt
```
Bandit Level 13 → Level 14
Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

Commands you may need to solve this level

ssh, telnet, nc, openssl, s_client, nmap
Helpful Reading Material

    SSH/OpenSSH/Keys
```

## Solution

After logging into the server, there is a `sshkey.private` file in the home directory. I `scp`-ed the file to my local machine using a very long command something like `scp -P 2220 bandit13@bandit.labs.overthewire.org:~/sshkey.private .` which will require the password from the last challenge. 

After the `scp` command I just tried to ssh straight to bandit14 using the following command: `ssh -p 2220 -i sshkey.private bandit14@bandit.labs.overthewire.org`. The `-i` on the ssh command indicates a some sort of ssh key (be it id_rsa or other key) to authenticate a user instead of a password. 

After trying that command there was a message saying `Permissions 0640 for 'sshkey.private' are too open.` This line means the permissions for the ssh key are not correct. Generally, ssh keys have a permission value of 700 (which means only a the user whose key it is has full access to it). [Here](https://quickref.me/chmod.html) is a reference to how linux permissions work. `chmod` is a program to change permissions of a file in linux.

After running the command `cmhod 700 sshkey.private`, rerun the `ssh -p 2220 -i sshkey.private bandit14@bandit.labs.overthewire.org` from earlier and the server authenticates without a password.


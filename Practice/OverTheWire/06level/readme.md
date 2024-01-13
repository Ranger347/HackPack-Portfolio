# OverTheWire Practice

## Prompt
```
Bandit Level 6 → Level 7
Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

    owned by user bandit7
    owned by group bandit6
    33 bytes in size

Commands you may need to solve this level

ls , cd , cat , file , du , find , grep
```

## Solution

Setup for this one is a little different. After logging in, there's nothing in the home directory. Looking at the prompt means this is going to be a bit more complicated; however still doable. 

From the last challenge the find command can be used. Looking at the man pages again (`man find`) there is a `-group gname` and a `-user uname` which can be used to find anything with a specific group or user. 

Searching for any file with these descriptions using the command `find / -user bandit7 -group bandit6 -size 33c` gives a lot of output with many permission denied messages. To simplify your life, you can redirect all those "errors" to /dev/null so you won't have to see them.

The final command is `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`

The output of the command is:
```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
```

After cat-ing the file the password is displayed: `z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`


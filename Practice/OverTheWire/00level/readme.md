# OverTheWire Practice

## How to Sign In to the Bandit Server

```text
Bandit Level 0
Level Goal

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

Commands you may need to solve this level

ssh

Helpful Reading Material

    Secure Shell (SSH) on Wikipedia
    How to use SSH on wikiHow
```

- Command to SSH into the Machine

`ssh bandit0@bandit.labs.overthewire.org -p 2220`

When the password prompt appears type in: `bandit0`

## Prompt

```text
Bandit Level 0 → Level 1
Level Goal

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

Commands you may need to solve this level

ls , cd , cat , file , du , find
```

## Solution

Once into the machine from the commands [above](#How to Sign In to the Bandit Server),

I ran the command `ls` to list the files in the current directory.

A readme appeared just like the prompt stated. After running `cat readme` the password was displayed: `NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL`

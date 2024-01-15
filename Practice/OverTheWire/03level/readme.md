# OverTheWire Practice

## Prompt

```text
Bandit Level 3 → Level 4
Level Goal

The password for the next level is stored in a hidden file in the inhere directory.

Commands you may need to solve this level

ls , cd , cat , file , du , find
```

## Solution

After logging into the server and listing the files, there is an `inhere` directory. Change into the directory with `cd inhere` and list the files in there. After a quick `ls` command, there appears to be nothing in the directory; however, according to the prompt there is a hidden file somewhere in this directory.

To list hidden files (or files that start with a . on Linux) you can run a `ls -la` command to list all the files and their permissions. That results with a `.hidden` file being discovered. Cat the file with `cat .hidden` and the password is revealed.

The password is: `2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe`

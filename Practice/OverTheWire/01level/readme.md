# OverTheWire Practice

## Prompt
```

Bandit Level 1 → Level 2
Level Goal

The password for the next level is stored in a file called - located in the home directory

Commands you may need to solve this level

ls , cd , cat , file , du , find

Helpful Reading Material

    Google Search for “dashed filename”
    Advanced Bash-scripting Guide - Chapter 3 - Special Characters
```


## Solution

After logging into bandit1 and looking at the files in the directory with `ls` there is a - file.

Apparently you cannot `cat` a file with that name. After looking at how to read that file with the command `cat < -` (basically reading in the contents of the file into cat) the password prints: `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi`.


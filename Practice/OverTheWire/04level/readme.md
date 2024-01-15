# OverTheWire Practice

## Prompt

```text
Bandit Level 4 → Level 5
Level Goal

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Commands you may need to solve this level

ls , cd , cat , file , du , find
```

## Solution

There is two ways to do this problem. Setup this problem by `ls` ing, seeing the `inhere/` directory, `cd` ing into the directory and `ls` ing again to see the files. You should see a list of 9 files all starting with the same format as the last challenge (files starting with -'s).

You can brute force this problem by looking through every file manually with `cat < filename`.

Or an alternate way to solve this challenge is to use bash for loops to look through every file and search for anything readable.

The command I used was: `for f in $(find . -type f); do cat < ${f}; echo \n; done | strings -n 10 | grep [a-z,A-Z,0-9]`.

Let me explain this command a bit. First, `for f in $(find . -type f); do cat < ${f}; echo \n; done | ...` is a bash for loop where it finds all the file types in the current directory and outputs them to the terminal. Second the `...| strings -n 10 | ...` part of the command means the output from the find command is piped to a strings command where it is looking for anything it can find with a length of 10 or greater (10 is just an arbitrary number that can be changed if nothing is found). Finally the `... | grep [a-z,A-Z,0-9]` part of the command means the output of strings command is piped to grep where it is looking for any lowercase letter, any uppercase letter, or any digit.

This command outputs the password with no other output: `lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`.

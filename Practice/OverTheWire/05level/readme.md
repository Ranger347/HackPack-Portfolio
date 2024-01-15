# OverTheWire Practice

## Prompt

```text
Bandit Level 5 → Level 6
Level Goal

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable

Commands you may need to solve this level

ls , cd , cat , file , du , find
```

## Solution

The setup for this is the same as the last problem (ls, cd into inhere/, ls); however, for this problem, there is a lot of maybehere## directories. Now I'm not sure about anyone else but I don't have the kind of time to look through all those directories for no reason. Lets automate it...

To automate what we're looking for,

The first thing I tried was a simple recursive ls with `ls -laR` and piped the output to grep to look for a certain number of bytes. The command was `ls -laR | grep 1033`. This command worked and displayed which file was 1033 bytes; however, it did not display where the file was. The output of this command follows:

```bash
bandit5@bandit:~/inhere$ ls -laR | grep 1033
-rw-r-----  1 root bandit5 1033 Oct  5 06:19 .file2
```

From this we can see there is a hidden file named `.file2` in a directory somewhere with 1033 bytes. This didn't really work though since I still had no idea where the file was, and there there were a few `.file2`'s after looking through some of the directories.

The second thing I tried after looking at the man pages for find with `man find`. Apparently find has a `-size` I used to specify a file size. Even without the other hints from the prompt, the command `find . -size 1033c` (c for bytes).

This command worked and outputed where the file was: `./maybehere07/.file2`

Cat this file and the password is: `P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU`.

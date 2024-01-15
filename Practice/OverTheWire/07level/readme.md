# OverTheWire Practice

## Prompt

```text
Bandit Level 7 → Level 8
Level Goal

The password for the next level is stored in the file data.txt next to the word millionth

Commands you may need to solve this level

man, grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
```

## Solution

After looking through the home directory there appears a `data.txt`. After trying to cat it, there produces WAY too much output, which you can stop outputting with CTRL+C if you want.

Really we only care about the millionth word so we can `cat data.txt | grep millionth`.

This command outputs the password:

```bash
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```

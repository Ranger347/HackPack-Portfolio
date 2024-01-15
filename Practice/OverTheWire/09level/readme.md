# OverTheWire Practice

## Prompt

```text
Bandit Level 9 → Level 10
Level Goal

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
```

## Solution

After logging in there is the same `data.txt` file from the previous challenge. The prompt says its one of the only lines with several '=' characters before it.

I tried to just `cat data.txt | grep =` but for some reason grep doesn't understand what I'm trying to do because it throws the following message:

```bash
bandit9@bandit:~$ cat data.txt | grep ==
grep: (standard input): binary file matches
```

Instead of just catting the file, I ran the file through `strings` with the same pipe to `grep`. `strings` is a program to print the sequences of printable characters in a file. `grep` understands the output of `strings` as printable characters when trying to find an '='.

The command I used was: `strings data.txt | grep ==`

The output and password follows:

```bash
bandit9@bandit:~$ strings data.txt | grep ==
x]T========== theG)"
========== passwordk^
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```

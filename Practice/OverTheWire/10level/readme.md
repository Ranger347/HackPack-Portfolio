# OverTheWire Practice

## Prompt

```text
Bandit Level 10 → Level 11
Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data

Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
Helpful Reading Material

    Base64 on Wikipedia
```

## Solution

After logging into the server, there's another `data.txt`. This time after catting it, its a short base64 encoded string.

Base64 can be decoded on [Cyberchef](https://gchq.github.io/CyberChef/) or on the command line using `base64 -d data.txt` or `cat data.txt | base64 -d`.

Either way the resulting answer and password is:

```bash
bandit10@bandit:~$ base64 -d data.txt 
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```

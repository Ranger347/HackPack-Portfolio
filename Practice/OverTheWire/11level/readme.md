# OverTheWire Practice

## Prompt

```text
Bandit Level 11 → Level 12
Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
Helpful Reading Material

    Rot13 on Wikipedia
```

## Solution

After logging into the server, there's another `data.txt` but this time the prompt says it has been rotated 13 positions. This sounds like [rot13](https://en.wikipedia.org/wiki/ROT13) to me.

Rot13 is part of a simple Caesar cipher where each of the characters has been rotated according to their ascii value by 13 values.

Rot13 can be decoded using [CyberChef](https://gchq.github.io/CyberChef/) or after a [quick google search](https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address) using the command `tr 'A-Za-z' 'N-ZA-Mn-za-m'`.

Either way the result is the same:

```bash
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```  

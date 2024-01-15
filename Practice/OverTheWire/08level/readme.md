# OverTheWire Practice

## Prompt

```text
Bandit Level 8 → Level 9
Level Goal

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
Helpful Reading Material

    Piping and Redirection
```

## Solution

After logging in, there is the same `data.txt` file from last challenge. This time the prompt says to find the line of text that only appears once. This challenge stumped me for a little bit.

I tried to see if I could find something about uniqueness in grep but couldn't find anything. I looked into the `sort` and `uniq` commands from the commands I may need section. I found that `sort` just sorts the lines of a text file and uniq reports or omit's repeated lines. More importantly `uniq` has a `-u` which only prints the unique lines.

Putting those together the command is: `sort data.txt | uniq -u`

The resulting password is: `EN632PlfYiZbn3PhVK3XOGSlNInNE00t`

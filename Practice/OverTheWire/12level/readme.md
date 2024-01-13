# OverTheWire Practice

## Prompt
```
Bandit Level 12 → Level 13
Level Goal

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file
Helpful Reading Material

    Hex dump on Wikipedia
```

## Solution

After logging into the server, there is the same `data.txt` in the home directory. However after catting the file and reading the prompt, I realize it is a ascii file, which is really a hexdump. A hexdump is basically the hex values of a file as a representation of the raw bytes. You can read about it with `man hexdump` and `man xxd`.

According to the prompt, there will be a lot of unzipping compressed files. The first time I completed this problem, I did all the unzipping manually. Each time the files was decompressed into another file, using xxd, base64, gzip, or bzip2. 

The easier way to do this problem is to make a bash script to go through all the decompressions for you. A long time ago I watched a [John Hammond](https://www.youtube.com/@_JohnHammond) video on this exact problem. The [resulting script](./matroyshka.sh) was created based on that video, which can be found [here](https://www.youtube.com/watch?v=wRSwagjvSqU).

I won't really discuss how I created the script because John would do much better than I would do in a text file (which is why I highly recommend his video). 

However after running the script in the tmp directory cat the flag.txt and the resulting password is: `The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw`


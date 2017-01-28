# CHECK RO MOUNT FILE SYSTEM

Check whether the mounted filesystem readable or writable with help of file creation.

---

```{r, engine='bash'}
$ python check_ro.py --help

usage: check_ro.py [-h] [-f FILE]

Check whether the mounted filesystem readable or writable

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File with mounted filesystems to check. If not
                        specified, /proc/mounts will be used
```


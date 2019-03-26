#!/usr/bin/env python
from __future__ import print_function

if __name__ == '__main__':
    import time

    elapsed = 0
    step = 5

    while True:
        print("{} seconds alive".format(elapsed))
        elapsed += step
        time.sleep(step)

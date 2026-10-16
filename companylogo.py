#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()


from collections import Counter

counts = Counter(s)
common = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]

for char, count in common:
    print(char, count)

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = [input() for _ in range(n)]

import re


transposed = ''.join([''.join(row[i] for row in matrix) for i in range(m)])

decoded = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', transposed)

print(decoded)

        

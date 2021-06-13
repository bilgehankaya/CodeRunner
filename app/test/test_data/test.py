import math
import random
import re
import os
import sys


def test(a, b):
    # Write your code
    return a ** b


if __name__ == '__main__':
    inp = input().split()
    a, b = int(inp[0]), int(inp[1])
    print(test(a, b))

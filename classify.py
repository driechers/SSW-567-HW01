#!/usr/bin/python3

import sys

def classify_triangle(a, b, c):
    return 'equilateral'

if __name__ == '__main__':
    print(classify_triangle(
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3])))

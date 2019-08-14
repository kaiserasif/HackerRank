#!/bin/python3

# https://www.hackerrank.com/challenges/battery/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    timeCharged = float(input())

    X, Y = [], []
    with open('trainingdata.txt', 'rt') as f:
        for line in f.readlines():
            x, y = [float(i) for i in line.split(',')]
            if y < 8: # there's a clip at 8, avoid it
                X.append(x)
                Y.append(y)

    mean = lambda x: sum(x) / len(x)
    cov = lambda x, y: mean( [a*b for a,b in zip(x,y)] ) - mean(x)*mean(y)
    m = cov(X, Y) / cov(X, X)
    b = mean(Y) - m * mean(X)

    pred = round(m*timeCharged + b, 2)
    print (pred if pred < 8 else 8.0)


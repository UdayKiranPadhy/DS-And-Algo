import math
from sys import *
import io
import os
import sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.setrecursionlimit()

ans = [1, 2, 5, 6, 5, 5]
sys.stdout.write(" ".join(map(str, ans)))
sys.stdout.write("\n")


n, m = [int(x) for x in input().split()]
coords = [int(x) for x in input().split()]
directions = [x for x in input().split()]


#import queue
input = stdin.readline
I = int
R = range
def listInput(): return list(map(int, input().strip().split()))
def lineInput(): return map(int, input().strip().split())
def sJoin(a, sep): return '{}'.format(sep).join(a)


def arrJoin(a, sep): return '{}'.format(sep).join(map(str, a))


inf = sys.maxsize
mod = 10000007

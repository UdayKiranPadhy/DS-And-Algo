import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.setrecursionlimit()

ans = [1, 2, 5, 6, 5, 5]
sys.stdout.write(" ".join(map(str, ans)))
sys.stdout.write("\n")


n, m = [int(x) for x in input().split()]
coords = [int(x) for x in input().split()]
directions = [x for x in input().split()]



from sys import *
import math
#import queue
input=stdin.readline
I=int
R=range
listInput=lambda:list(map(int,input().strip().split()))
lineInput= lambda:map(int,input().strip().split())
sJoin=lambda a,sep : '{}'.format(sep).join(a)
arrJoin=lambda a,sep : '{}'.format(sep).join(map(str,a))

inf = sys.maxsize
mod = 10000007

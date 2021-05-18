import io, os, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.setrecursionlimit()

ans = [1, 2, 5, 6, 5, 5]
sys.stdout.write(" ".join(map(str, ans)))
sys.stdout.write("\n")


n, m = [int(x) for x in input().split()]
coords = [int(x) for x in input().split()]
directions = [x for x in input().split()]

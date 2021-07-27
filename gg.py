from functools import lru_cache
import sys


@lru_cache(None)
def go(string, l, h):
    if l > h:
        return sys.maxsize
    if (l == h):
        return 0
    if l == h-1:
        return 0 if string[l] == string[h] else 1
    if string[l] == string[h]:
        return go(string, l+1, h-1)
    else:
        return min(go(string, l+1, h), go(string, l, h-1)) + 1


print(go("abc", 0, 2))

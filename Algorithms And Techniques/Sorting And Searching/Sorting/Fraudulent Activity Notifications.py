_, slide = list(map(int, input().split()))
l = list(map(int, input().split()))


def median1(l):
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    return l[len(l) // 2]


notification = 0
left = 0
l.sort()
for i in range(slide, len(l) - 1):
    l1 = l[left:i]
    left += 1
    median = median1(l1)
    if l[i] >= (2 * median):
        notification += 1

print(notification)


"""
Solution

#!/bin/python3

import sys
import bisect as bs

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bs.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def median(a_sorted, days):
    half = len(a_sorted)//2
    
    if days % 2:
        median = a_sorted[half]
    else:
        median = (a_sorted[half-1] + a_sorted[half])/2
        
    return float(median)

def activityNotifications(log, days):
    heap = sorted(log[:days])
    res = 0
    med = 0
    to_del = 0
    
    for ind in range(days, len(log)):
        med = median(heap, days)
        #print("heap: {}".format(heap))
        #print("log[{}] = {} med = {}".format(ind, log[ind], med))
            
        if float(log[ind]) >= 2*med:
            res += 1
        
        #del heap[heap.index(log[to_del])]
        del heap[index(heap, log[to_del])]
        bs.insort(heap, log[ind])
        to_del += 1
            
    return res
        

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)

"""
from functools import lru_cache

N = int(input())

A = []

for i in range(N):
    A.append(int(input()))

graph = {i:[] for i in range(2,N+1)}

for i in range(2,N + 1):
    xor = i
    for j in range(i+1,N+1):
        xor = xor ^ j
        if j%i != 0:
            graph[i].append([j,xor])

@lru_cache(None)
def go(index):
    if index == N:
        return 0
    
    best = float('inf')
    for next_node in graph[index]:
        best = min(best,next_node[1] + go(next_node[0]))
    return best

print(go(2))
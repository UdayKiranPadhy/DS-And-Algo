from collections import deque


for t in range(int(input())):
    n , m = [int(x) for x in input().strip().split(" ")]
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    edges = []
    for i in range(m):
        edges.append([int(x) for x in input().strip().split(" ")])
    source = int(input())
    for start,end in edges:
        graph[start].append(end)
    distances = [99999 for _ in range(n+1)]
    stack = deque([-1,source])
    level = 1
    while stack:
        present_node = stack.pop()
        if present_node == -1:
            level += 1
            if len(stack) !=0:
                stack.appendleft(-1)
        else:
            for child in graph[present_node]:
                stack.appendleft(child)
                distances[child] = min(distances[child],level*6)
    result =[]
    for i in range(1,n+1):
        if i == source:
            continue
        elif distances[i]==99999:
            result.append(-1)
        else:
            result.append(distances[i])
    print(result)
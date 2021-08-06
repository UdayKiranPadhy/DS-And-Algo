array = [1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]

adj = {}

max_distance = 0
for i in range(len(array)):
    if array[i] not in adj:
        adj[array[i]] = i
    else:
        if i - adj[array[i]] > max_distance:
            max_distance = i - adj[array[i]]

print(max_distance)
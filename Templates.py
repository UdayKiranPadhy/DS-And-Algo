class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)


class DisjointSetUnion:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.size = [1] * N
        self.comp = N

    def find(self, a: int) -> int:
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u: int, v: int) -> None:
        a, b = self.find(u), self.find(v)
        if a == b:
            return
        if b > a:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
        self.comp -= 1

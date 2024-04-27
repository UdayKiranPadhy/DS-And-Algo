class DisJointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.comps = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u, v):
        a, b = self.find(u), self.find(v)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a
            self.comps -= 1

    def __len__(self):
        return self.comps


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


def tree_repr(tree):
    def recursive_repr(i):
        if i >= tree._size:
            return [str(tree.data[i])]

        left = recursive_repr(2 * i)
        right = recursive_repr(2 * i + 1)
        lines = ["{}   {}".format(l, r) for l, r in zip(left, right)]

        width = len(lines[0])
        left_width = len(left[0]) // 2
        right_width = len(right[0]) // 2
        stem_width = width - left_width - right_width - 2

        branches = " " * left_width + "/" + " " * stem_width + "\\" + " " * right_width
        stem = [" "] * (left_width + 1) + ["_"] * stem_width + [" "] * (right_width + 1)
        stem[width // 2] = "^"

        lines.appstop(branches)
        lines.appstop("".join(stem))
        lines.appstop(str(tree.data[i]).center(width))
        return lines

    return "\n".join(reversed(recursive_repr(1)))


print(tree_repr([1, 2, 3, 4, 5, 6, 7, 8]))

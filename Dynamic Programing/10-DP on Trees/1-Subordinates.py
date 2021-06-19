"""
Date :- 18/06/21
Problem Statement :- https://cses.fi/problemset/task/1674/
Explanatation = https://youtu.be/fGznXJ-LTbI?list=PLb3g_Z8nEv1j_BC-fmZWHFe6jmU_zv-8s  


Given the structure of a company, your task is to calculate for each employee 
the number of their subordinates.

Input

The first input line has an integer n: the number of employees. 
The employees are numbered 1,2,…,n, and employee 1 is the general director of the company.

After this, there are n−1 integers: for each employee 2,3,…,n their direct 
boss in the company.

Output

Print n integers: for each employee 1,2,…,n the number of their subordinates.

Constraints
1≤n≤2⋅105
Example

Input:
5
1 1 2 3

Output:
4 1 1 0 0

"""


def solve(src, parent, tree):
    subordinates = 0
    for childs in tree[src]:
        if childs != parent:
            solve(childs, src, tree)
            subordinates += (1 + ans[childs])
    ans[src] = subordinates


def main():
    n = int(input())
    l = [int(x) for x in input().strip().split(" ")]
    tree = [[] for _ in range(n+1)]
    global ans
    ans = [0]*(n+1)
    index = 0
    for i in range(2, n+1):
        tree[i].append(l[index])
        tree[l[index]].append(i)
        index += 1
    print(tree)
    solve(1, 0, tree)
    print(ans)


if __name__ == '__main__':
    main()

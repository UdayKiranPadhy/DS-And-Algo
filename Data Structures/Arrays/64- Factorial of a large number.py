"""
Factorial of 100 has 158 digits. It is not possible to store these 
many digits even if we use long long int.


Input : 100
Output : 933262154439441526816992388562667004-
         907159682643816214685929638952175999-
         932299156089414639761565182862536979-
         208272237582511852109168640000000000-
         00000000000000

Input :50
Output : 3041409320171337804361260816606476884-
         4377641568960512000000000000

"""


def fact(N):
    res = [None] * 20
    res_size = 1
    res[0] = 1
    iterator = 2
    while iterator <= N:
        carry = 0
        i = 0
        while i < res_size:
            prod = res[i]*iterator + carry
            res[i] = prod % 10
            carry = prod // 10
            i += 1
        while carry:
            res[i] = carry % 10
            carry = carry // 10
            i += 1
            res_size += 1
        iterator += 1
    ans = []
    for i in range(res_size-1, -1, -1):
        ans.append(res[i])
    print(ans)


fact(7)

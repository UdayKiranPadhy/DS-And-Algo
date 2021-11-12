input1 = "a3b2"
input2 = 5
res= ""
for i in range(0,len(input1),2):
    res += input1[i] * int(input1[i+1])

if input2 < len(res):
    return res[input2]
else:
    return -1
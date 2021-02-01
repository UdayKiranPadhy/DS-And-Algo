"""
Estimated End Date: 18/02/21
FizzBuzz in list
Complete the given function solve. This function accepts as parameter 2 numbers start and end.

You have to generate a list with numbers start from start ending with end. Additionally, you have to do the following:

for those numbers that are divisible by 3, you must have the word Fizz instead of the number
for those numbers that are divisible by 5, your must have the word Buzz instead of the number
And for those numbers divisible by both 3 and 5, we must have the word FizzBuzz
Return the list that you have generated.

Example Input:
2 18

Output:
2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz
"""
def solve(start,end):
    l=[]
    for i in range(start,end+1):
        if i%3 == 0 and i%5==0:
            l.append("FizzBuzz")
            continue
        if i%3 == 0:
            l.append("Fizz")
            continue
        if i%5 == 0:
            l.append("Buzz")
            continue
        l.append(i)
    return l
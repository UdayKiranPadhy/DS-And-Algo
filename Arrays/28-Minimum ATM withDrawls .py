"""
Source :-Edyst and HackwithInfy Sample Questions
Date :-15/06/21

Minimum ATM Withdrawals

There is a unique ATM in Wonderland. Imagine this ATM as an array of numbers. 
You can withdraw cash only from either ends of the array. Sarah wants to withdraw 
X amount of cash from the ATM.

What are the minimum number of withdrawals Sarah would need to accumulate X amount 
of cash. If it is not possible for Sarah to withdraw X amount, return -1.

Input Format
The first line contains an integer N, denoting the number of elements in ATM
Each line i of the N subsequent lines (where 0 <=i <= N) contains an integer 
describing the cash in ATM.
The next line contains an integer, X, denoting the total amount to withdraw

Constraints
1<=N<=10^5
1<= ATM[i] <= 105
1 <= X <= 105
Sample Input
2
1
1
3
Sample Output
-1
Explanation
The total amount of cash in the ATM is 2, hence Sarah cannot withdraw an amount of 5

"""


def main():
    # N = int(input())
    arr = [6, 49, 76, 99, 0, 53, 12, 75, 59, 81, 0, 78, 26, 73, 93, 38, 28, 5, 98, 67, 97, 93, 88, 18, 33, 73, 30, 81, 83, 21, 19, 96, 71, 51, 97, 74, 54, 37, 35, 96, 57, 40, 26, 50, 30, 69, 46, 34, 39,
           9, 61, 7, 32, 18, 55, 78, 23, 64, 59, 56, 16, 85, 67, 85, 83, 99, 19, 9, 39, 13, 67, 59, 80, 15, 8, 12, 21, 59, 13, 86, 34, 44, 6, 10, 93, 24, 50, 19, 14, 87, 81, 38, 91, 57, 85, 7, 65, 89, 67, 38]
    # for i in range(N):
    #     arr.append(int(input()))
    K = 4400
    i = 0
    j = 0
    if sum(arr) < K:
        return -1
    maximum_size_subarray = -1
    current_sum = arr[0]
    while i <= j and j < len(arr):
        if current_sum < K:
            current_sum += arr[j]
            j += 1
        elif current_sum > K:
            current_sum -= arr[i]
            i += 1
        else:
            maximum_size_subarray = max(maximum_size_subarray, j-i+1)
            current_sum -= arr[i]
            i += 1
    return len(arr)-maximum_size_subarray


if __name__ == '__main__':
    print(main())

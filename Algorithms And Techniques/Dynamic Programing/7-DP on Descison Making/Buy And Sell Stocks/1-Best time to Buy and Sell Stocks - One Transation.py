"""

Problem Statement : https://leetcode.com/problems/best-time-to-buy-and-sell-/

121. Best Time to Buy and Sell 
Easy
You are given an array prices where prices[i] is the price of a given  on the ith day.

You want to maximize your profit by choosing a single day to buy one  and choosing a different day in the future to sell that .

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104


"""

# Solution Explanatation :- https://www.youtube.com/watch?v=4YjEHmw1MX0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=30&ab_channel=Pepcoding
# https://www.youtube.com/watch?v=eMSfBgbiEjk&ab_channel=takeUforward

def main():
    listInput = [int(x) for x in input().split(" ")]
    least_value_index_so_far = 0
    max_profit_so_far = 0

    for i in range(1, len(listInput)):
        if listInput[i] < listInput[least_value_index_so_far]:
            least_value_index_so_far = i
        else:
            max_profit_so_far = max(
                max_profit_so_far, listInput[i]-listInput[least_value_index_so_far])
    return max_profit_so_far


def main2():
    prices = [int(x) for x in input().split(" ")]
    least_value_so_far = prices[0]
    profit = 0
    for i in range(len(prices)):
        profit = max(profit, prices[i]-least_value_so_far)
        least_value_so_far = min(least_value_so_far, prices[i])
    return profit


if __name__ == '__main__':
    print(main2())

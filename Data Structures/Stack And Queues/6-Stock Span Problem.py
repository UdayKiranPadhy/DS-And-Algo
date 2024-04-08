"""

The stock span problem is a financial problem where we have a series of n 
daily price quotes for a stock and we need to calculate span of stock’s 
price for all n days.

The span Si of the stock’s price on a given day i is defined as the maximum 
number of consecutive days just before the given day, for which the price 
of the stock on the current day is less than or equal to its price on the given day.

For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

"""


def StockSpan(arr):
    output = []
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            output.append([None, -1])
        elif len(stack) > 0 and stack[-1][0] > arr[i]:
            output.append(stack[-1])
        elif len(stack) > 0 and stack[-1][0] <= arr[i]:
            while len(stack) > 0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append([arr[i], i])
    stack.clear()

    for i in range(len(output)):
        stack.append(i - output[i][1])
    return stack


print(StockSpan([100, 80, 60, 70, 60, 75, 85]))

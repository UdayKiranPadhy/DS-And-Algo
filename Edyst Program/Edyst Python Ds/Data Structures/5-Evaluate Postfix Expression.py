"""
Evaluate Postfix expression
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are+, -, *, /.Each operand may be an integer or another expression.

Example :
Input :
A. ["2", "1", "+", "3", "*"]
 
B. ["4", "13", "5", "/", "+"]
Output :
A. ((2 + 1) * 3) = 9
 
B. (4 + (13 / 5)) = 6

"""

import math


class Solution:
    def evaluateRPN(self, a):
        stack = [None] * len(a)
        res = 0
        for i in a:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                if i == "+":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    res = op1 + op2
                    stack.append(res)
                elif i == "-":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    res = op1 - op2
                    stack.append(res)
                elif i == "*":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    res = op1 * op2
                    stack.append(res)
                elif i == "/":
                    op2 = stack.pop()
                    op1 = stack.pop()
                    if op1 < op2:
                        res = op1 / op2
                    else:
                        res = op1 // op2
                    stack.append(math.ceil(res))
        return stack.pop()

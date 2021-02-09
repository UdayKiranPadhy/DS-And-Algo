"""
While us humans can understand how to calculate a simple mathematical expression like 2 + 3 * 7 - 9 / 5, computers use a special technique to make it easier for them. They convert an infix expression to a postfix expression.

An infix expression is one in which all the operators (+,-,*,/) appear between operands, just like our usual expressions.

A postifx expression is one in which all the operands appear first, and the operators appear after the operands.

Write a class Fixes that has 2 strings infix and postfix. It should have a parameterized constructor to accept the value of infix.

Also, it should have a method called convert that converts the infix to a postfix expression and stores it in the postfix.

Write only the Fixes class. Main class has already been written.

Hint: Check google for tutorials on infix to postfix conversion first. Then write the code for it.
Note: all operands will be of single digit only

Example Input:
2+3*7-9/5
Output:
237*+95/-
Example Input:
(2+3)*7-9/2^1
Output:
23+7*921^/-
"""


class Fixes:
    def __init__(self, x):
        self.s = x.strip()
        self.postfix = ""

    def convert(self):
        Operators = ["+", "-", "*", "/", "%", "(", ")", "^"]
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        stack = []
        for i in self.s:
            if i not in Operators:
                self.postfix = self.postfix + i
            else:
                if i not in Operators:
                    self.postfix = self.postfix + i
                elif i == "(":
                    stack.append(i)
                elif i == ")":
                    while stack and stack[-1] != "(":
                        self.postfix += stack.pop(-1)
                    stack.pop(-1)
                else:
                    while (
                        stack
                        and stack[-1] != "("
                        and precedence[i] <= precedence[stack[-1]]
                    ):
                        self.postfix += stack.pop()
                    stack.append(i)
        for i in range(len(stack) - 1, -1, -1):
            self.postfix += stack[i]


testcases = int(input())
for _ in range(testcases):
    equation = input()
    fix = Fixes(equation)
    print(f"Infix: {equation}")
    fix.convert()
    print(f"Postfix: {fix.postfix}")
    print("---")

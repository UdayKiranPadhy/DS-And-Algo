
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                number = ""
                while stack and stack[-1].isdigit():
                    gg = stack.pop()
                    number = gg + number

                stack.append(int(number) * substr)

        return "".join(stack)
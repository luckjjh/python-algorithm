from collections import deque


class Solution:
    def romanToInt(self, s: str) -> int:
        temp = []
        for i in range(len(s)):
            if s[i] == 'I':
                temp.append(1)
            elif s[i] == 'V':
                temp.append(5)
            elif s[i] == 'X':
                temp.append(10)
            elif s[i] == 'L':
                temp.append(50)
            elif s[i] == 'C':
                temp.append(100)
            elif s[i] == 'D':
                temp.append(500)
            elif s[i] == 'M':
                temp.append(1000)
        stack = deque()
        for i in temp:
            if stack and stack[-1] < i:
                tmp = stack.pop()
                stack.append(i-tmp)
            else:
                stack.append(i)

        return sum(stack)

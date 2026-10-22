class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = 0
        y = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-/*":
                y = stack.pop()
                x = stack.pop()
                if tokens[i]=="+":
                    stack.append(x+y)
                elif tokens[i]=="-":
                    stack.append(x-y)
                elif tokens[i]=="*":
                    stack.append(x*y)
                elif tokens[i]=="/":
                    stack.append(int(x/y))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
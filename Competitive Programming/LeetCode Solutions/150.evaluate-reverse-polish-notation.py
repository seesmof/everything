#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        res = 0
        stack = []
        for token in tokens:
            if token != "+" or token != "-" or token != "*" or token != "/":
                stack.append(token)
            else:
                operandOne, operandTwo = stack.pop(), stack.pop()
                if token == "+":
                    res += operandOne + operandTwo
                elif token == "-":
                    res += operandOne - operandTwo
                elif token == "*":
                    res += operandOne * operandTwo
                else:
                    res *= operandTwo


# @lc code=end

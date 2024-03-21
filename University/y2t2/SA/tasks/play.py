from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def generate_parentheses(n):
    def is_valid(s):
        # Check if the string is valid
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if not stack or stack.pop() != "(":
                    return False
        return not stack  # If the stack is empty, the string is valid

    def generate(s, left, right, arr):
        # Base case: if we have used all pairs of parentheses
        if left == 0 and right == 0:
            if is_valid(s):
                arr.append(s)
            return

        # Recursive case: try adding an opening parenthesis
        if left > 0:
            generate(s + "(", left - 1, right, arr)

        # Recursive case: try adding a closing parenthesis
        if right > 0 and left < right:
            generate(s + ")", left, right - 1, arr)

    res = []
    generate("", n, n, res)
    return res


# Example usage
res = generate_parentheses(3)
console.print(res, type(res))

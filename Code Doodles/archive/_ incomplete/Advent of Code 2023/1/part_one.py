from rich.console import Console

console = Console()

with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

ans = 0
for line in lines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if line[i:].startswith(val):
                digits.append(str(d + 1))
    value = int(digits[0] + digits[-1])
    ans += value
console.print(ans)

from rich.console import Console

console = Console()

with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

ans = 0
for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    value = int(digits[0] + digits[-1])
    ans += value
console.print(ans)

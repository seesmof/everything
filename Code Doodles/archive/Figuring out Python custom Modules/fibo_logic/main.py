from rich import print


def fib(n: int) -> None:
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fibo(n: int) -> [int]:
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def formFibonacci(n: int) -> [int]:
    fibonacciSequence = []
    current, nextNumber = 0, 1
    while current < n:
        fibonacciSequence.append(current)
        current, nextNumber = nextNumber, current + nextNumber
    return fibonacciSequence
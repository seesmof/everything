from rich.console import Console
from rich.traceback import install
from scipy.optimize import minimize_scalar

install()
console = Console()


def f(x):
    return (x - 2) ** 2


def df(x):
    return 2 * (x - 2)


def searchPowell(x0: float = -1, e1: float = 1e-6, e2: float = 1e-6) -> float:
    x: float = x0
    while True:
        alpha = minimize_scalar(lambda alpha: f(x - alpha * df(x))).x
        newX: float = x - alpha * df(x)
        if abs(f(newX) - f(x)) < e1 and abs(newX - x) < e2:
            break
        x = newX
    return x


def main() -> None:
    bounds: tuple[float, float] = (-1, 3)

    with console.status("Optimizing...", spinner="point"):
        resPowell: float = f"{searchPowell():.2f}"
        resScalar: float = f"{minimize_scalar(f, bounds).x:.2f}"

    console.print(f"Powell's Method: {resPowell}")
    console.print(f"Scalar Method: {resScalar}")
    console.print()
    console.print(
        "[green bold]Correct answer found![/green bold]"
        if resPowell == resScalar
        else "[red bold]Doesn't match![/red bold]"
    )


if __name__ == "__main__":
    main()

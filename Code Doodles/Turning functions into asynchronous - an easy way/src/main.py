from asyncio import Task, create_task, run, to_thread
from requests import Response
import requests
from rich.console import Console
from rich.traceback import install

install()
console = Console()


async def fetchWebsiteStatus(url: str) -> dict:
    response: Response = await to_thread(requests.get, url)
    return {"url": url, "status": response.status_code}


async def main() -> None:
    appleTask: Task[dict] = create_task(fetchWebsiteStatus("https://apple.com"))
    googleTask: Task[dict] = create_task(fetchWebsiteStatus("https://google.com"))

    appleStatus: dict = await appleTask
    googleStatus: dict = await googleTask

    console.print([appleStatus, googleStatus])


if __name__ == "__main__":
    run(main())

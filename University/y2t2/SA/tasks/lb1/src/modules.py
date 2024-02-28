from collections import defaultdict
import json
import time
import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich import box
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from os import path

"""
Jesus - 1979
The Nativity Story - 2006
The Passion of the Christ - 1988
Paul, Apostle of Christ - 2018
Пропала грамота - 1972
Поводир - 2014
Мавка. Лісова пісня - 2023
Клондайк - 2022
"""

"""
available halls will be a list of 3-5 random numbers from 1-10

each session has a 2d list of seat rows and on each row a list of seats with 0 being free and 1 being occupied

at first to user we will show the list of movies and ask which one they want to watch

then we will ask how many tickets they want to buy

in main menu we will have a tab with bought tickets and a tab with available movies
    in tickets tab there will be an option to give up a ticket
"""

"""
Cinema:
    a list of movies
        for each movie - a list of rooms
            in each room a list of seats - taken and free
            be able to take and free seats
    be able to add new movies
"""


class Room:
    def __init__(self, number: int = 0, seats: list[list[int]] = []):
        self.seats: list[list[int]] = seats
        self.number: int = number


class Movie:
    def __init__(self, title: str = "Movie", rooms: list[Room] = []):
        self.title: str = title
        self.rooms: list[Room] = rooms


class Ticket:
    def __init__(self, movie: Movie, room: Room, row: int, seat: int):
        self.movie: Movie = movie
        self.room: Room = room
        self.row: int = row
        self.seat: int = seat


class Cinema:
    def __init__(self, name: str = "Cinema", movies: list[Movie] = []):
        self.movies: list[Movie] = movies
        self.name: str = name
        self.tickets: list[Ticket] = []
        self.watched: dict = defaultdict(int)

    def buyTicket(self, movie: Movie, room: Room, row: int, seat: int) -> None:
        room.seats[row][seat] = 0
        self.tickets.append(Ticket(movie, room, row, seat))

    def sellTicket(self, ticket: Ticket) -> None:
        self.tickets.remove(ticket)
        room = ticket.room
        room.seats[ticket.row][ticket.seat] = 1

    def readMoviesFromJson(self, path: str = "") -> None:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.name = data["name"]
        for movie in data["movies"]:
            curRooms = []
            for room in movie["rooms"]:
                curRoom = Room(number=room["number"], seats=room["seats"])
                curRooms.append(curRoom)
            curMovie = Movie(title=movie["title"], rooms=curRooms)
            self.movies.append(curMovie)


def drawRoomTable(room: Room, movie: Movie) -> None:
    seats = [["🔴" if not seat else "🟢" for seat in row] for row in room.seats]

    table = Table.grid(padding=(1, 1))
    for i, row in enumerate(seats):
        table.add_row(*[f"[bold]{i+1}[/]"] + row)

    console.print(
        f'[bold]All seats for "{movie.title}" in room #{room.number}[/bold]\n',
        table,
        "\n",
    )


def drawTicketsTable(tickets: list[Ticket]) -> None:
    table = Table(box=box.ROUNDED)
    table.add_column("Index", justify="right", style="cyan", no_wrap=True)
    table.add_column("Movie", style="bold yellow")
    table.add_column("Year", style="violet", no_wrap=True)
    table.add_column("Room", style="magenta", no_wrap=True)
    table.add_column("Row", style="green", no_wrap=True)
    table.add_column("Seat", style="blue", no_wrap=True)
    for i, ticket in enumerate(tickets):
        name, year = ticket.movie.title.split(" - ")
        table.add_row(
            f"{i+1}",
            f"{name}",
            f"{year}",
            f"{ticket.room.number}",
            f"{ticket.row+1}",
            f"{ticket.seat+1}",
        )
    console.print(table, "\n")


def drawMoviesTable() -> None:
    table = Table(box=box.ROUNDED)
    table.add_column("Index", style="cyan", no_wrap=True, justify="right")
    table.add_column("Movie", style="bold yellow", no_wrap=True)
    table.add_column("Year", style="violet", no_wrap=True)
    table.add_column("Times Watched", style="magenta", no_wrap=True, justify="left")
    for i, (movie, count) in enumerate(cinema.watched.items()):
        name, year = movie.split(" - ")
        table.add_row(
            f"{i+1}",
            f"{name}",
            f"{year}",
            f"{count}",
        )
    console.print(table, "\n")


currentDir: str = path.dirname(path.abspath(__file__))
moviesDataPath: str = path.join(currentDir, "..", "data", "movies.json")

cinema: Cinema = Cinema()
cinema.readMoviesFromJson(moviesDataPath)

while True:
    actions = [
        "Browse Tickets",
        "View Bought Tickets",
        "View Watched Movies",
        "Add New Movie",
        "Exit",
    ]
    action = inquirer.prompt(
        [
            inquirer.List(
                "action",
                message="What would you like to do?",
                choices=actions,
            )
        ]
    )["action"]

    if action == "Browse Tickets":
        if not cinema.movies:
            console.print("[bold]No movies found[/bold]\n")

        movie = inquirer.prompt(
            [
                inquirer.List(
                    "movie",
                    message="Which movie would you like to watch?",
                    choices=[movie.title for movie in cinema.movies],
                )
            ]
        )["movie"]
        movie = [movie.title for movie in cinema.movies].index(movie)
        movie = cinema.movies[movie]

        room = inquirer.prompt(
            [
                inquirer.List(
                    "room",
                    message="Choose a room (hall) where you would like to watch the movie",
                    choices=range(1, len(movie.rooms) + 1),
                )
            ]
        )["room"]
        room = movie.rooms[room - 1]

        drawRoomTable(room, movie)

        availableRows = [i + 1 for i, row in enumerate(room.seats) if True in row]
        row = inquirer.prompt(
            [
                inquirer.List(
                    "row",
                    message="Choose a seat row where you would like to watch the movie",
                    choices=availableRows,
                )
            ]
        )["row"]
        row = row - 1

        seats = [i + 1 for i, seat in enumerate(room.seats[row]) if seat]
        seat = inquirer.prompt(
            [
                inquirer.List(
                    "seat",
                    message="Choose a seat where you would like to watch the movie",
                    choices=seats,
                )
            ]
        )["seat"]
        seat = seat - 1

        confirmation = inquirer.prompt(
            [
                inquirer.Confirm(
                    "confirm",
                    message=f'Are you sure you want to buy a ticket for "{movie.title}" in room {room.number} row {row+1} seat {seat+1}?',
                    default=True,
                )
            ]
        )

        if confirmation["confirm"]:
            cinema.buyTicket(movie, room, row, seat)
            console.print("\n[bold]Ticket bought![/bold]\n")

        drawRoomTable(room, movie)

    elif action == "View Bought Tickets":
        if not cinema.tickets:
            console.print("[bold]No bought tickets found[/bold]\n")
            continue
        drawTicketsTable(cinema.tickets)

        indeces = range(1, len(cinema.tickets) + 1)
        ticketIndex = inquirer.prompt(
            [
                inquirer.List(
                    "ticket",
                    message="Choose a ticket number",
                    choices=indeces,
                )
            ]
        )["ticket"]
        ticketIndex = ticketIndex - 1

        action = inquirer.prompt(
            [
                inquirer.List(
                    "action",
                    message="What would you like to do?",
                    choices=["Watch movie", "Return ticket", "Exit"],
                )
            ]
        )["action"]

        ticketData = cinema.tickets[ticketIndex]
        movieName = ticketData.movie.title

        if action == "Return ticket":
            cinema.sellTicket(ticketData)
            console.print(f'[bold]"{movieName}"[/bold] was returned!\n')
        elif action == "Watch movie":
            cinema.watched[movieName] += 1
            console.print(f'[bold]"{movieName}"[/bold] was watched!\n')
            cinema.tickets.remove(ticketData)

    elif action == "View Watched Movies":
        if not cinema.watched:
            console.print("[bold]No watched movies found[/bold]\n")
            continue
        drawMoviesTable()

    elif action == "Add New Movie":
        pass

    else:
        break

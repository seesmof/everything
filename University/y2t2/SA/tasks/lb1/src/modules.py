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


class Room:
    def __init__(self, number: int = 0, seats: list[list[int]] = []):
        self.seats = seats
        self.number = number

    def takeSeat(self, row: int, seat: int) -> None:
        self.seats[row][seat] = 1

    def freeSeat(self, row: int, seat: int) -> None:
        self.seats[row][seat] = 0


class Movie:
    def __init__(self, title: str = "Movie", rooms: list[Room] = []):
        self.title = title
        self.rooms = rooms


class Cinema:
    def __init__(self, name: str = "Cinema", movies: list[Movie] = []):
        self.movies = movies
        self.name = name

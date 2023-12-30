"""
Properties: Name, Description, Status, Difficulty

Difficulty: easy, medium, hard (1, 2, 3)
Status: todo, doing, done
"""

from os import path
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

import click
import sqlite3

currentDir = path.dirname(path.abspath(__file__))
databasePath = path.join(currentDir, "..", "data", "project_ideas.db")

# help
# add task
# remove task
# list tasks


@click.group()
def cli():
    pass


@click.command(help="Add new project idea")
def add():
    console.print("Adding new project idea...")


@click.command(help="Remove project idea")
def remove():
    console.print("Removing project idea...")


@click.command(help="List project ideas")
def display():
    console.print("Listing project ideas...")


@cli.command()
def help():
    console.print("Help...")


if __name__ == "__main__":
    cli()

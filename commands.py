import click
from sys import argv
from os import getenv
from database import Database


@click.group()
def cli():
    pass


@click.command()
def create_table():
    db = Database(getenv("DB_NAME"))
    db.create_table(
        "CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)"
    )


@click.command()
@click.argument("category")
@click.argument("url")
def add(category, url):
    db = Database(getenv("DB_NAME"))
    db.insert("urls", None, category, url)


@click.command()
@click.argument("category")
def index(category):
    db = Database(getenv("DB_NAME"))
    links = db.fetch_all("urls", category=category)

    for link in links:
        print(link[2])


@click.command()
def fetch_categories():
    db = Database(getenv("DB_NAME"))
    categories = db.fetch_distinct("category", "urls")

    for name in categories:
        print(name[0])

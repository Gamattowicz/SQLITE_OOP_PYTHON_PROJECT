import click
from sys import argv
from os import getenv
from database import Database
from repositories.urls import save, fetch_categories, fetch_urls


@click.group()
def cli():
    pass


@click.command(name = 'create')
def create_table():
    db = Database(getenv("DB_NAME"))
    db.create_table(
        "CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)"
    )


@click.command(name = 'add')
@click.argument("category")
@click.argument("url")
def add(category, url):
    print('Add new url address')
    save(category, url)


@click.command(name = 'urls')
@click.argument("category")
def show_urls(category):
    print(f'List of urls from category {category}')
    for link in fetch_urls(category):
        print(link[2])


@click.command(name = 'categories')
def show_categories():
    print('List of categories')
    for name in fetch_categories():
        print(name[0])

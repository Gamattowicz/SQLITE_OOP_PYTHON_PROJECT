from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()
from database import Database
import click
     
@click.group()
def cli():
    pass

@click.command()
def create_table():
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')

@click.command()
@click.argument('category')
@click.argument('url')
def add(category, url):
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)

@click.command()
@click.argument('category')
def index(category):
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category = category)

    for link in links:
        print(link[2])

@click.command()
def fetch_categories():
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('category', 'urls')
    
    for name in categories:
        print(name[0])


cli.add_command(create_table)
cli.add_command(add)
cli.add_command(index)
cli.add_command(fetch_categories)
           
# if len(argv) > 1 and argv[1] == 'setup':
#     print('Create table in database')

    
if __name__ == '__main__':
    cli()
    
print(getenv('DB_NAME'))

# if len(argv) == 4 and argv[1] == 'add':
#     print('Add new adress url')
#     category = argv[2]
#     url = argv[3]

# if len(argv) == 3 and argv[1] == 'list':
#     print(f'Show list of links in category {argv[1]}')
#     category = argv[2]

    
    


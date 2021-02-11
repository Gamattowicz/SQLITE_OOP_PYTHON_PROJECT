from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()
from database import Database
                
if len(argv) > 1 and argv[1] == 'setup':
    print('Create table in database')
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')
    

print(getenv('DB_NAME'))

if len(argv) == 4 and argv[1] == 'add':
    print('Add new adress url')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)
    
if len(argv) == 3 and argv[1] == 'list':
    print(f'Show list of links in category {argv[1]}')
    category = argv[2]
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category = category)
    
    for link in links:
        print(link[2])

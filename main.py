from os import getenv
from dotenv import load_dotenv
from commands import cli, create_table, add, fetch_categories, index
load_dotenv()

cli.add_command(create_table)
cli.add_command(add)
cli.add_command(index)
cli.add_command(fetch_categories)
           
if __name__ == '__main__':
    cli()
    
print(getenv('DB_NAME'))

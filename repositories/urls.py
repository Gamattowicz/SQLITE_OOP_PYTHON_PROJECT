from os import getenv
from database import Database


def save(category, url):
    db = Database(getenv("DB_NAME"))
    db.insert("urls", None, category, url)
    
def fetch_categories():
    db = Database(getenv("DB_NAME"))
    return db.fetch_distinct("category", "urls")

def fetch_urls(category):
    db = Database(getenv("DB_NAME"))
    return db.fetch_all("urls", category=category)
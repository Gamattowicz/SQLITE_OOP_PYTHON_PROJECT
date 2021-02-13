from flask import Flask, jsonify, request
from repositories.urls import save, fetch_categories, fetch_urls

app = Flask(__name__)

@app.route('/add', methods = ['POST'])
def add():
    data = request.json
    category = data['category']
    url = data['url']
    save(category, url)
    return {
        'status': 'OK'
    }
    
    
@app.route('/categories')
def get_categories():
    categories = fetch_categories()
    return jsonify(categories)
    
    
@app.route('/category/<name>')
def get_category(name):
    urls = fetch_urls(name)
    return jsonify(urls)
    
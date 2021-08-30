from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests

from bs4 import BeautifulSoup

app: Flask = Flask(__name__)
client = MongoClient('mongodb://test:test@3.38.93.118', 27017)
db = client.dbsparta


# HTML 을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/cafes', methods=['GET'])
def listing():
    location = request.args['location']
    query = {
        "address": {
            "$regex": f"{ location }"
        }
    }
    cafes = list(db.cafes.find(query, {'_id': False}))
    return jsonify({"cafes": cafes})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

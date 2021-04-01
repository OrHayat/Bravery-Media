from flask import Flask, request
import requests
from data_manager.Queries import *
import json


app = Flask(__name__)


@app.route('/get_top_items', methods=['GET'])
def get_top_items():
    category = request.args.get("category")
    top_items = search_favorites(category)
    print(top_items)
    return json.dumps(top_items)


@app.route('/get_search_results', methods=['GET'])
def get_search_results():
    item_type = request.args.get("item_type")
    keywords = request.args.get("keywords")
    search_results = search_by_type(item_type, keywords)
    return json.dumps(search_results)


@app.route('/get_item', methods=['GET'])
def get_item():
    item_id = request.args.get("item_id")
    item_info = get_item_info(item_id)
    return json.dumps(item_info)


@app.route('/add_recommendation', methods=['POST'])
def add_recommendation():
    recommendation = request.json
    item_id = recommendation.id
    bravery_moments = recommendation.selectedHeroismMoments
    content = recommendation.recommendation
    reviewer = recommendation.recommenderName
    item_rating = recommendation.braveryRate
    add_review(item_id, bravery_moments, content, reviewer, item_rating)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
# get top items test
    url = '127.0.0.1:5000/get_top_items'
    params = {'category': 'movie'}
    req = requests.get(url, params=params)
    response = req.json()
    print(response)
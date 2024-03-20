from flask import Blueprint, jsonify, request
import requests
from bs4 import BeautifulSoup

newspaper_overview_blueprint = Blueprint('newspaper_overview', __name__)
@newspaper_overview_blueprint.route('/api/get-newspaper-overview', methods=['POST'])
def get_newspaper_overview():
    data = request.json
    url = data['url']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    overview = soup.find('meta', property='og:description')
    if overview:
        return jsonify({"overview": overview.get('content')})
    return jsonify({"error": "No suitable overview found"}), 404
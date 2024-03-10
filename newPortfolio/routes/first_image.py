from flask import Blueprint, jsonify, request
import requests
from bs4 import BeautifulSoup


first_image_blueprint = Blueprint('first_image', __name__)

@first_image_blueprint.route('/api/get-first-image', methods=['POST'])
def get_first_image():
    data = request.json
    url = data['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')

    # Define a tuple of common image file extensions
    valid_extensions = ('jpg', 'jpeg', 'png', 'gif', 'svg', 'webp', 'bmp', 'avif')

    for img_tag in img_tags:
        img_src = img_tag.get('src', '')
        if img_src.startswith('http') and any(ext in img_src.lower() for ext in valid_extensions):
            head_resp = requests.head(img_src)
            if head_resp.status_code != 404:
                # If status code is 200, the image exists, return the image URL
                return jsonify({"imageUrl": img_src})
            
    return jsonify({"error": "No suitable image found"}), 404

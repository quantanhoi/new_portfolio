from flask import Blueprint, jsonify
from models.newspaper import Newspaper

newspapers_blueprint = Blueprint('newspapers', __name__)
@newspapers_blueprint.route('/newspapers', methods=['GET'])
def get_newspaper():
    query = Newspaper.select()
    newspapers_list = [{"id": newspaper.id, 
                        "title": newspaper.title, 
                        "url": newspaper.url, 
                        "topic": newspaper.topic.name} for newspaper in query]
    return jsonify(newspapers_list)
from flask import Blueprint, jsonify, request
from models.newspaper import Newspaper
from models.topic import Topic
from peewee import IntegrityError

newspapers_blueprint = Blueprint('newspapers', __name__)
@newspapers_blueprint.route('/api/newspapers', methods=['GET'])
def get_newspaper():
    query = Newspaper.select().order_by(Newspaper.id.desc())
    newspapers_list = [{"id": newspaper.id, 
                        "title": newspaper.title, 
                        "url": newspaper.url, 
                        "topic": newspaper.topic.name} for newspaper in query]
    return jsonify(newspapers_list)


@newspapers_blueprint.route('/api/newspapers', methods=['POST'])
def add_newspaper():
    data = request.json
    title = data.get('title')
    url = data.get('url')
    topic_name = data.get('topic')

    try:
        # Check if the topic exists
        topic, created = Topic.get_or_create(name=topic_name)
        
        # Create a new Newspaper entry
        newspaper = Newspaper.create(title=title, url=url, topic=topic)
        
        # Return success response
        return jsonify({"id": newspaper.id, "title": newspaper.title, "url": newspaper.url, "topic": newspaper.topic.name}), 201
    except IntegrityError as e:
        return jsonify({"error": str(e)}), 400



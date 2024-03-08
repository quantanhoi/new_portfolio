from flask import Blueprint, jsonify
from models.topic import Topic

topics_blueprint = Blueprint('topics', __name__)
@topics_blueprint.route('/api/topics', methods=['GET'])
def get_topic():
    query = Topic.select()
    topic_list = [{"id": topic.id, "name": topic.name} for topic in query]
    return jsonify(topic_list)
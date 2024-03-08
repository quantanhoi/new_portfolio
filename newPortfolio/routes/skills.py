from flask import Blueprint, jsonify
from models.skill import Skill

skills_blueprint = Blueprint('skills', __name__)

@skills_blueprint.route('/api/skills', methods=['GET'])
def get_skills():
    query = Skill.select()
    skills_list = [{"id": skill.id, "name": skill.name} for skill in query]
    return jsonify(skills_list)


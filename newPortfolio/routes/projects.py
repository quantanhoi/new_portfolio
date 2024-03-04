from flask import Blueprint, jsonify
from models.project import Project

projects_blueprint = Blueprint('projects', __name__)
@projects_blueprint.route('/projects', methods=['GET'])
def get_projects():
    query = Project.select()
    projects_list = [{"id": project.id, "name": project.name, "url": project.url, "icon": project.icon} for project in query]
    return jsonify(projects_list)
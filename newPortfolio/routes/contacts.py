from flask import Blueprint, jsonify
from models.contact import Contact

contacts_blueprint = Blueprint('contacts', __name__)
@contacts_blueprint.route('/contacts', methods=['GET'])
def get_contacts():
    query = Contact.select()
    contacts_list = [{"id": contact.id, "name": contact.name, "detail": contact.detail} for contact in query]
    return jsonify(contacts_list)



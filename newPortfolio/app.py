from flask import Flask
from routes.skills import skills_blueprint
from routes.projects import projects_blueprint
from routes.contacts import contacts_blueprint

app = Flask(__name__)
app.register_blueprint(skills_blueprint)
app.register_blueprint(projects_blueprint)
app.register_blueprint(contacts_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

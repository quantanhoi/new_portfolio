from flask import Flask
from routes.skills import skills_blueprint
from routes.projects import projects_blueprint
from routes.contacts import contacts_blueprint
from routes.newspapers import newspapers_blueprint
from routes.topics import topics_blueprint
from routes.first_image import first_image_blueprint
from routes.newspaper_overview import newspaper_overview_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(skills_blueprint)
app.register_blueprint(projects_blueprint)
app.register_blueprint(contacts_blueprint)
app.register_blueprint(newspapers_blueprint)
app.register_blueprint(topics_blueprint)
app.register_blueprint(first_image_blueprint)
app.register_blueprint(newspaper_overview_blueprint)

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port = "5000", debug=True)

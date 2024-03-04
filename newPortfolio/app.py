# from database.database import db
# from models.skill import Skill

# # The given code snippet goes here

# if __name__ == '__main__':
#     # Make sure the database connection is established
#     db.connect()
    
#     # Retrieve a specific Skill entity by name
#     skill_name = "Python"  # Example skill name you're looking for
#     try:
#         db.execute_sql('SET search_path TO db2sttrthie;')
#         skill = Skill.get(Skill.name == skill_name)
#         print(f"Skill Found: {skill.name}")
#     except Skill.DoesNotExist:
#         print(f"Skill with name '{skill_name}' does not exist.")
    
#     # Don't forget to close the connection when you're done
#     db.close()


from flask import Flask
from routes.skills import skills_blueprint  # Adjust the import path based on your project structure
from routes.projects import projects_blueprint

app = Flask(__name__)
app.register_blueprint(skills_blueprint)
app.register_blueprint(projects_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

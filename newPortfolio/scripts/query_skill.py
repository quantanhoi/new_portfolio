from database import db
from models import Skill

# The given code snippet goes here

if __name__ == '__main__':
    # Make sure the database connection is established
    db.connect()
    
    # Retrieve a specific Skill entity by name
    skill_name = "Python"  # Example skill name you're looking for
    try:
        skill = Skill.get(Skill.name == skill_name)
        print(f"Skill Found: {skill.name}")
    except Skill.DoesNotExist:
        print(f"Skill with name '{skill_name}' does not exist.")
    
    # Don't forget to close the connection when you're done
    db.close()

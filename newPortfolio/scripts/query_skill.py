from database import db
from models import Skill



if __name__ == '__main__':
    db.connect()
    
    # Retrieve a specific Skill entity by name
    skill_name = "Python" 
    try:
        skill = Skill.get(Skill.name == skill_name)
        print(f"Skill Found: {skill.name}")
    except Skill.DoesNotExist:
        print(f"Skill with name '{skill_name}' does not exist.")
    
    db.close()

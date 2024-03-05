from database.database import db
from models import Skill, Project, Contact, Topic, Newspaper


if __name__ == '__main__':
    db.connect()
    db.create_tables([Skill, Project, Contact, Topic, Newspaper])
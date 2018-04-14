from peewee import *

db = SqliteDatabase('jobber.db')

class BaseModel(Model):
    class Meta:
        database = db

# the user model specifies its fields (or columns) declaratively, like django
class Job(BaseModel):
    title = CharField(unique=True)
    company = CharField()
    url = CharField()
    description = TextField()
    presence = BooleanField(default=True)
    join_date = DateTimeField()


db.create_tables([Job], safe = True)

# db.connect()



from peewee import *

db = SqliteDatabase('jobber.db')

class Job(Model):
    title = CharField()
    company = CharField()
    url = CharField()
    location = CharField()
    summary = CharField()
    applied = BooleanField()
    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([Job], safe=True)

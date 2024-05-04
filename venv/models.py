# models.py

from peewee import Model, CharField, ForeignKeyField
from database import database

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    name = CharField()

    @classmethod
    def get_all(cls):
        return cls.select()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.get_or_none(cls.id == user_id)

class Post(BaseModel):
    title = CharField()
    content = CharField()
    user = ForeignKeyField(User, backref='posts')

    @classmethod
    def find_by_user(cls, user):
        return cls.select().where(cls.user == user)

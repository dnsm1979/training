from peewee import *
import datetime

# from playhouse.cockroachdb import JSONField

db = SqliteDatabase("tweets.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = TextField()


class Tweet(BaseModel):
    content = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref="tweets")


class Favorite(BaseModel):
    user = ForeignKeyField(User, backref="favorites")
    tweet = ForeignKeyField(Tweet, backref="favorites")


if __name__ == "__main__":
    db.create_tables([User, Tweet, Favorite])

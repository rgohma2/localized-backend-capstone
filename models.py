import os
from peewee import *
from flask_login import UserMixin
import datetime

from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:

	DATABASE = connect(os.environ.get('DATABASE_URL'))

else:

	DATABASE = SqliteDatabase('localized.sqlite', pragmas={'foreign_keys': 1})

class BaseModel(Model):
	"""Our base model that all other models will inherit from"""
	class Meta:
		database = DATABASE

class Address(BaseModel):
	address_1 = CharField()
	address_2 = CharField()
	city = CharField()
	state = CharField()
	zip_code = CharField()
	country = CharField()

class User(BaseModel, UserMixin):
	address = ForeignKeyField(Address, on_delete='CASCADE')
	first_name = CharField()
	last_name = CharField()
	email = CharField(unique=True) 
	password = CharField()

class Business(BaseModel):
	address = ForeignKeyField(Address)
	owner = ForeignKeyField(User, backref='business', on_delete='CASCADE')
	name = CharField()
	about = CharField()
	category = CharField()
	image = CharField()

class Post(BaseModel):
	business = ForeignKeyField(Business, backref='posts', on_delete='CASCADE')
	image = CharField()
	content = CharField()
	date = DateTimeField(default=datetime.datetime.now)

class Subscription(Model):
	following = ForeignKeyField(Business, backref='subscribers', on_delete='CASCADE')
	follower = ForeignKeyField(User, backref='subscriptions', on_delete='CASCADE')

	class Meta:
		database = DATABASE
		indexes = (
			(('following','follower'), True),
		)
class Comment(BaseModel):
	post = ForeignKeyField(Post, backref='comments')
	commenter = ForeignKeyField(User, backref='comments', on_delete='CASCADE')
	content = CharField()
	date = DateTimeField(default=datetime.datetime.now)


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Address, User, Business, Post, Subscription, Comment], safe=True)
	print('Sucessfully connected to DataBase')
	DATABASE.close()









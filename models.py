from peewee import *
from flask_login import UserMixin
import datetime


DATABASE = SqliteDatabase('localized.sqlite')

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
	address = ForeignKeyField(Address)
	first_name = CharField()
	last_name = CharField()
	email = CharField(unique=True) 
	password = CharField()

class Business(BaseModel):
	address = ForeignKeyField(Address)
	owner = ForeignKeyField(User, backref='business')
	name = CharField()
	about = CharField()
	category = CharField()
	image = CharField()

class Post(BaseModel):
	business = ForeignKeyField(Business, backref='posts')
	image = CharField()
	content = CharField()
	date = DateTimeField(default=datetime.datetime.now)

class Subscription(Model):
	following = ForeignKeyField(Business, backref='subscribers')
	follower = ForeignKeyField(User, backref='subscriptions')

	class Meta:
		database = DATABASE
		indexes = (
			(('following','follower'), True),
		)



def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Address, User, Business, Post, Subscription], safe=True)
	print('Sucessfully connected to DataBase')
	DATABASE.close()









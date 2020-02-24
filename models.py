from peewee import *
from flask_login import UserMixin


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
	address = ForeignKeyField(Address, backref='address')
	first_name = CharField()
	last_name = CharField()
	email = CharField(unique=True) 
	password = CharField()

class Business(BaseModel):
	address = ForeignKeyField(Address, backref='address')
	owner = ForeignKeyField(User, backref='owner')
	name = CharField()
	about = CharField()
	category = CharField()
	image = CharField()


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Address, User, Business], safe=True)
	print('Sucessfully connected to DataBase')
	DATABASE.close()









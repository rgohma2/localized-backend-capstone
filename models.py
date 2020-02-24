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
	first_name = CharField()
	last_name = CharField()
	email = CharField(unique=True) 
	password = CharField()
	address = ForeignKeyField(Address, backref='address')


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Address, User], safe=True)
	print('Sucessfully connected to DataBase')
	DATABASE.close()









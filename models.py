from peewee import *


DATABASE = SqliteDatabase('localized.sqlite')

class BaseModel(Model):
	"""Our base model that all other models will inherit from"""
	class Meta:
		database = DATABASE





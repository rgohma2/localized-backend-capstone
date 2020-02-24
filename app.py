from flask import Flask, jsonify
from flask_login import LoginManager

import models
from resources.users import users


DEBUG = True
PORT = 8000

app = Flask(__name__) 

app.register_blueprint(users, url_prefix='/api/v1/users')

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
	try:
		return models.User.get(models.User.id == user_id)
	except models.DoesNotExist:
		return None










if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
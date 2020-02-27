from flask import Flask, jsonify
from flask_login import LoginManager
from flask_cors import CORS

import models
from resources.users import users
from resources.businesses import businesses
from resources.posts import posts
from resources.subscriptions import subscriptions
from resources.comments import comments

DEBUG = True
PORT = 8000

app = Flask(__name__) 

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(businesses, origins=['http://localhost:3000'], supports_credentials=True)
CORS(posts, origins=['http://localhost:3000'], supports_credentials=True)
CORS(subscriptions, origins=['http://localhost:3000'], supports_credentials=True)
CORS(comments, origins=['http://localhost:3000'], supports_credentials=True)





app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(businesses, url_prefix='/api/v1/businesses')
app.register_blueprint(posts, url_prefix='/api/v1/posts')
app.register_blueprint(subscriptions, url_prefix='/api/v1/subscriptions')
app.register_blueprint(comments, url_prefix='/api/v1/comments')


app.secret_key = '9pq438hiredfbkajhosei'

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
	try:
		return models.User.get(models.User.id == user_id)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
			data={},
			message='Error, user not logged in',
			status=401
		), 401 










if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
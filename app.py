from flask import Flask, jsonify

import models
from resources.users import users


DEBUG = True
PORT = 8000

app = Flask(__name__) 

app.register_blueprint(users, url_prefix='/api/v1/users')












if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
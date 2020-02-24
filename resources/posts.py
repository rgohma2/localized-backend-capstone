import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['GET'])
def test():
	return 'posts resource working'
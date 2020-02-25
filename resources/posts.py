import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=['GET'])
def post_index():
	posts = models.Post.select()

	post_dicts = [model_to_dict(post) for post in posts]
	[(post['business'].pop('owner'), post['business'].pop('address')) for post in post_dicts]

	return jsonify(
			data=post_dicts,
			message=f'Sucessfully retrieved {len(posts)} posts',
			status=201
		), 201


@posts.route('/', methods=['POST'])
def create_post():
	payload = request.get_json()
	try:
		business = models.Business.get(models.Business.owner == current_user.id)
		print(business)
		payload['business'] = business
		post = models.Post.create(**payload)
		post_dict = model_to_dict(post)
		print(post_dict)
		return jsonify(
				data=post_dict,
				message='New post created!',
				status=200
			), 200
	except:
		return jsonify (
				data={},
				message='You are not the owner of this business.',
				status=401
			), 401








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
		return jsonify(
				data={},
				message='You are not the owner of this business.',
				status=401
			), 401

@posts.route('/<id>', methods=['Delete'])
def delete_post(id):
	post = models.Post.get_by_id(id)
	if post.business.owner.id == current_user.id:
		post.delete_instance()
		return jsonify(
				data={},
				message='Sucessfully deleted post!',
				status=201
			), 201
	else:
		return jsonify(
				data={},
				message='You do not own the business that made this post.',
				status=401
			), 401

@posts.route('/<id>', methods=['PUT'])
def update_post(id):
	payload = request.get_json()
	post = models.Post.get_by_id(id)
	if post.business.owner.id == current_user.id:
		post.content = payload['content'] if 'content' in payload else None
		post.image = payload['image'] if 'image' in payload else None
		post.save()

		post_dict = model_to_dict(post)
		post_dict['business'].pop('owner')

		return jsonify(
				data=post_dict,
				message='Sucessfully updated post!',
				status=201
			), 201
	else:
		return jsonify(
				data={},
				message='You do not own the business that made this post.',
				status=401
			), 401
	














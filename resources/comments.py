import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

comments = Blueprint('comments', 'comments')

@comments.route('/<post_id>', methods=['GET'])
def comment_index(post_id):
	post = models.Post.get_by_id(post_id)
	print(model_to_dict(post))

	return 'comments resource working'



@comments.route('/<post_id>', methods=['POST'])
@login_required
def create_comment(post_id):
	payload = request.get_json()

	comment = models.Comment.create(
			post=post_id,
			commenter=current_user.id,
			content=payload['content'] 
		)

	comment_dict = model_to_dict(comment)

	return jsonify(
			data=comment_dict,
			message='Successfully posted new comment',
			status=200
		), 200


@comments.route('/<id>')
@login_required
def delete_comment(id):
	comment = models.Comment.get_by_id(id)
	if comment.commenter.id == current_user.id:
		comment.delete_instance()
		return jsonify(
				data={},
				message='Successfully deleted comment',
				status=200
			), 200
	else:
		return jsonify(
				data={},
				message='You are not the owner of the comment',
				status=401
			), 401






















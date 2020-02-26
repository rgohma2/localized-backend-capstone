import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

subscriptions = Blueprint('subscriptions', 'subscriptions')

@subscriptions.route('/', methods=['GET'])
@login_required
def subscription_index():

	# query that finds all the subscriptions of the logged in user
	subscriptions_query = models.Subscription.select().join(models.User).where(models.User.id == current_user.id)
	
	# gets the businesses being followed from the subscriptions
	businesses_being_followed = [subscription.following for subscription in subscriptions_query]

	post_dicts=[]
	for i in range (0, len(businesses_being_followed)):
		posts = businesses_being_followed[i].posts
		print(posts)
		# post_dicts=[model_to_dict(post) for post in posts]
		for j in range (0, len(posts)):
			print("THIS IS THE POST DICT")
			post = model_to_dict(posts[j])
			post['business'].pop('owner')
			post['business'].pop('address')
			post_dicts.append(post)
	print(post_dicts)


	return jsonify(
			data=post_dicts,
			message='subscriptions: {}'.format(len(businesses_being_followed)),
			status=200
		), 200

@subscriptions.route('/<id>', methods=['POST'])
@login_required
def subscribe(id):
	try:

		business = models.Business.get_by_id(id)
		models.Subscription.create(
				following=business.id,
				follower=current_user.id
			)
		return jsonify(
				data={},
				message=f'subscribed to {business.name}',
				status=200
			), 200
	except:
		return jsonify(
				data={},
				message=f'you are already subscribed to {business.name}',
				status=401
			), 401




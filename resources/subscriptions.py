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
	print(model_to_dict(businesses_being_followed[1]))

	
	# loops through businesses and joins the posts while simultaniously making dictionaries
	# post_dicts = []
	# for i in range (0, len(businesses_being_followed)):

	# post_query = models.Post.select().join(models.Business).where(models.Business.id == businesses_being_followed[i].id)

		# post_dicts.append(post)
		# post_dicts = [model_to_dict(post) for post in posts]
		# [(post['business'].pop('owner'), post['business'].pop('address')) for post in post_dicts]


	# print(post_dicts)
	posts = businesses_being_followed[0].posts
	print(model_to_dict(posts[0]))
	# post_dicts = [model_to_dict(business.posts) for business in businesses_being_followed]

	return jsonify(
			data={},
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




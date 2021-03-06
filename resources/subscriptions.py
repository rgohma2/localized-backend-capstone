import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

subscriptions = Blueprint('subscriptions', 'subscriptions')

@subscriptions.route('/', methods=['GET'])
@login_required
def subscription_index():

	# query that finds all the subscriptions of the logged in user
	subscriptions_query = (models.Subscription
		.select().join(models.User)
		.where(models.User.id == current_user.id))
	
	# gets the businesses being followed from the subscriptions
	businesses_being_followed = [model_to_dict(subscription.following) for subscription in subscriptions_query]
	print(businesses_being_followed)
	# finding posts where follower id matches logged in user id
	posts = (models.Post
		.select()
		.join(models.Business)
		.join(models.Subscription)
		.where(models.Subscription.follower == current_user.id))
	post_dicts = [model_to_dict(post) for post in posts]
	[(post['business'].pop('owner'), post['business'].pop('address')) for post in post_dicts]



	return jsonify(
			data=post_dicts,
			subscriptions=businesses_being_followed,
			message='subscriptions: {}'.format(len(businesses_being_followed)),
			status=200
		), 200

@subscriptions.route('/<business_id>', methods=['POST'])
@login_required
def subscribe(business_id):
	try:

		business = models.Business.get_by_id(business_id)
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

@subscriptions.route('/<business_id>', methods=['Delete'])
@login_required
def delete_sub(business_id):
	try:

		subscription = (
			models.Subscription
			.get(models.Subscription.follower == current_user.id
			, models.Subscription.following == business_id))


		print('SUBSCRIPTION TO DELETE')
		print(model_to_dict(subscription))

		subscription.delete_instance()

		return jsonify(
				data={},
				message='Unsubscribed!',
				status=200
			), 200
	except:
		return jsonify(
				data={},
				message='You are trying to remove a subscription you dont have.',
				status=401
			), 401



	












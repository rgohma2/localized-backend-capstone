import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

subscriptions = Blueprint('subscriptions', 'subscriptions')

@subscriptions.route('/', methods=['GET'])
@login_required
def subscription_index():
	subscriptions_query = models.Subscription.select().join(models.User).where(models.User.id == current_user.id)
	
	businesses_being_followed = [subscription.following for subscription in subscriptions_query]
	post_dicts = [model_to_dict(business.posts) for business in businesses_being_followed]

	return jsonify(
			data=post_dicts,
			message='subscriptions: {}'.format(len(business_sub_dicts)),
			status=200
		), 200

@subscriptions.route('/<id>', methods=['POST'])
@login_required
def subscribe(id):
	try:

		business = models.Business.get_by_id(id)
	# # business = models.Subscription.select().where(models.Subscription.following == id)
	# # business = models.Business.subscribers
	# # print(business)
	# # print('these are the subscribers to the business')
	# # print(business.subscribers)
	# # print(model_to_dict(business.subscribers))
	# # for subscriber in business.subscribers:
	# # 	if current_user.id == subscriber:
	# # 		return jsonify(
	# # 				message='you are already subscribed'
	# # 			)
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




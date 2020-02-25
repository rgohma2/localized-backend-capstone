import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

subscriptions = Blueprint('subscriptions', 'subscriptions')

@subscriptions.route('/', methods=['GET'])
def test():
	return 'subscriptions resource working'

@subscriptions.route('/<id>', methods=['POST'])
@login_required
def subscribe(id):
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
	


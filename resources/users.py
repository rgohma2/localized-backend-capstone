import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user



users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test():
	return 'users resource working!'


@users.route('/register', methods=['POST'])
def register():
	"""User register route"""
	payload = request.get_json()
	payload['email'] = payload['email'].lower()

	try:
		models.User.get(models.User.email == payload['email'])

		return jsonify(
				data={},
				message='There is already a user registered with that email.',
				status=401
			), 401

	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		print(payload)
		# return 'hi'
		# if payload['address_2'] == None:
		# 	payload['address_2'] == ''
		user_address = models.Address.create(
				address_1=payload['address_1'],
				address_2=payload['address_2'],
				city=payload['city'], 
				state=payload['state'], 
				zip_code=payload['zip_code'], 
				country=payload['country'] 
			)
		print(user_address)

		new_user = models.User.create(
				first_name=payload['first_name'],
				last_name=payload['last_name'],
				email=payload['email'],
				password=payload['password'],
				address=user_address.id
			)
		new_user_dict = model_to_dict(new_user)
		new_user_dict.pop('password')
		print(new_user_dict)

		return jsonify (
				data=new_user_dict,
				message='Sucessfully created new user with email: {}'.format(new_user_dict['email']),
				status=200
			), 200
		







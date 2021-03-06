import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user, login_required, current_user



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

@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()

	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		password_matches = check_password_hash(user_dict['password'], payload['password'])
		
		# checking to see if user is the owner of a business
		business = (models.Business
			.select()
			.join(models.User)
			.where(models.Business.owner == user.id))
		business_dict = ''
		# if the user owns a business then we will send it back as a dict
		if len(business) != 0:
			business = business[0]
			business_dict = model_to_dict(business)
		if password_matches:
			login_user(user)
			user_dict.pop('password')

			return jsonify(
					data=user_dict,
					business=business_dict,
					message=f'Welcome back {user.first_name}.',
					status=201
				), 201
		else:
			print('bad password')
			return jsonify(
					data={},
					message='Incorrect email or password.',
					status=401
				), 401
	except models.DoesNotExist:
		print('bad username')
		return jsonify(
				data={},
				message='Incorrect email or password.',
				status=401
			), 401

@users.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return jsonify(
			data={},
			message='Sucessfully logged out user.',
			status=200
		), 200


@users.route('/delete', methods=['Delete'])
@login_required
def delete_account():
	user = models.User.get_by_id(current_user.id)
	user.delete_instance(recursive=True)

	return jsonify(
			data={},
			message='Account deleted.',
			status=201
		), 201

















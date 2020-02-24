import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


# nice to add: if users business is the same address as their house 
# they should have the option to choose same as home address.
# also should not be required for privacy reasons



businesses = Blueprint('businesses', 'businesses')

@businesses.route('/', methods=['GET'])
def test():
	businesses = models.Business.select()
	# creates a list of dictionaries from all the business models
	business_dicts = [model_to_dict(business) for business in businesses]
	# pops each business owners address and password
	[(business['owner'].pop('address'), business['owner'].pop('password')) for business in business_dicts]

	return jsonify(
			data=business_dicts,
			message=f'Successfully retrieved {len(businesses)} businesses.',
			status=200
		), 200

@businesses.route('/', methods=['POST'])
@login_required
def create_business():
	payload = request.get_json()

	business_address = models.Address.create(
			address_1=payload['address_1'],
			address_2=payload['address_2'],
			city=payload['city'],
			state=payload['state'],
			zip_code=payload['zip_code'],
			country=payload['country']
		)
	print(business_address)

	business = models.Business.create(
			address=business_address.id,
			owner=current_user.id,
			name=payload['name'],
			about=payload['about'],
			category=payload['category'],
			image=payload['image']
		)
	business_dict = model_to_dict(business)
	print(business_dict)
	# pops each business owners address and password
	business_dict['owner'].pop('address')
	business_dict['owner'].pop('password')
	print(business_dict)

	return jsonify(
			data=business_dict,
			message=f'{business.name} successfully created!',
			status=200
		), 200

@businesses.route('/<id>', methods=['Delete'])
@login_required
def delete_business(id):
	business = models.Business.get_by_id(id)
	# storing business name to be used in response message
	name = business.name
	if current_user.id == business.owner.id:
		business.delete_instance()
		return jsonify(
				data={},
				message=f'Your business {name} has been deleted!',
				status=200
			), 200
	else:
		return jsonify(
				data={},
				message=f'You do not own {name}',
				status=401
			), 401

@businesses.route('/<id>', methods=['PUT'])
@login_required
def update_business(id):
	payload = request.get_json()
	business = models.Business.get_by_id(id)

	if business.owner.id == current_user.id:

		address = models.Address.get_by_id(business.address.id)

		address.address_1 = payload['address_1'] if 'address_1' in payload else None
		address.address_2 = payload['address_2'] if 'address_2' in payload else None
		address.city = payload['city'] if 'city' in payload else None
		address.state = payload['state'] if 'state' in payload else None
		address.zip_code = payload['zip_code'] if 'zip_code' in payload else None
		address.country = payload['country'] if 'country' in payload else None
		address.save()

		business.address = address
		business.name = payload['name'] if 'name' in payload else None
		business.about = payload['about'] if 'about' in payload else None
		business.category = payload['category'] if 'category' in payload else None
		business.image = payload['image'] if 'image' in payload else None
		business.save()

		business_dict = model_to_dict(business)
		business_dict['owner'].pop('password')
		business_dict['owner'].pop('address')

		return jsonify(
				data=business_dict,
				message=f'Successfully updated {business.name}!',
				status=200
			), 200
	else:
		return jsonify(
				data={},
				message=f'You do not own {business.name}.',
				status=401
			), 401




















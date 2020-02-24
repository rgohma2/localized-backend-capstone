import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user


# nice to add: if users business is the same address as their house 
# they should have the option to choose same as home address.
# also should not be required for privacy reasons



businesses = Blueprint('businesses', 'businesses')

@businesses.route('/', methods=['GET'])
def test():
	return 'businesses resource working'

@businesses.route('/', methods=['POST'])
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
	business_dict['owner'].pop('address')
	business_dict['owner'].pop('password')

	return jsonify(
			data=business_dict,
			message=f'Successfully created business with name: {business.name}',
			status=200
		), 200







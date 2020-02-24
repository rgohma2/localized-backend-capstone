from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

businesses = Blueprint('businesses', 'businesses')

@businesses.route('/', methods=['GET'])
def test():
	return 'businesses resource working'
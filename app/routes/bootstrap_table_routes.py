from load_dotenv import load_dotenv

import os
from app.services.get_bootstrap_services import generate_service_data
from flask import Blueprint, jsonify, request, make_response

load_dotenv()

ORG_NAME = 'whatcomcodersBootstrap'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GCP_PROJECT_ID = "whatcomcoders-bootstrap"

bp = Blueprint('bootstrap_table', __name__, url_prefix='/bootstrap-table')

@bp.route('/', methods=['GET'])
def get_all_bootstrap_services():
    services = generate_service_data(ORG_NAME, GITHUB_TOKEN, GCP_PROJECT_ID)
    services_data = []
    for service in services:
        print(service)
        services_data.append(service)

    response = make_response(jsonify(services_data), 200)
    return response


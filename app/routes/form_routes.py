import os
from load_dotenv import load_dotenv
from flask import Blueprint, jsonify, request, make_response
from app.services.github_manager import GithubManager

load_dotenv()

TOKEN = os.getenv('GITHUB_TOKEN')

bp = Blueprint('bootstrap', __name__, url_prefix='/bootstrap')

@bp.route('/', methods=['GET'])
def health_check():
    response = make_response(jsonify({'status': 'ok'}), 200)
    return response

@bp.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        print(data)
        print(type(data))
        github_username = data['githubUsername']
        language = data['language'].split(' ')[0].lower()

        github_manager = GithubManager(TOKEN)
        template_repo = github_manager.get_template_repo(language)
        new_repo = github_manager.create_github_repo_from_template(template_repo, github_username)
       
        if not new_repo:
            raise Exception("Failed to create a new repository.")


        github_manager.add_user_to_repo(new_repo, github_username)
        response = make_response(jsonify({'status': 'ok'}), 200)

    except Exception as e:
        response = make_response(jsonify({'status': 'error', 'message': str(e)}), 500)
        return response

    return response
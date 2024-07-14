from load_dotenv import load_dotenv
import os
import requests

load_dotenv()

# Replace with your GitHub organization name and personal access token
ORG_NAME = 'whatcomcodersBootstrap'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_repos(org_name, token):
    url = f'https://api.github.com/orgs/{org_name}/repos'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_owner(repo_url, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(repo_url, headers=headers)
    response.raise_for_status()
    return response.json()['owner']['login']

def generate_service_data(org_name, token, project_id):
    repos = get_repos(org_name, token)
    service_data = []
    for repo in repos:
        service_name = repo['name']
        owner = get_owner(repo['url'], token)
        repo_url = repo['html_url']
        logs_url = f'https://console.cloud.google.com/logs/query;project={project_id}&query=resource.type%3D"{service_name}"'
        service_data.append({
            'service_name': service_name,
            'owner': owner,
            'repo': repo_url,
            'logs': logs_url,
        })
    return service_data
    

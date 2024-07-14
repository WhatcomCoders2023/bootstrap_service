import requests

TEMPLATE_OWNER = 'WhatcomCodersDev'
TEMPLATE_REPO = 'bootstrap_python_example'
NEW_OWNER = 'WhatcomCodersBootstrap'

class GithubManager:
    """Manages Creating Github Repositories for bootstrap services"""

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.baptiste-preview+json",
        }

    def get_template_repo(self, language: str):
        if language == 'python':
            return 'bootstrap_python_example'
        elif language == 'javascript':
            raise NotImplementedError('bootstrap_javascript_example not implemented yet')
        elif language == 'java':
            raise NotImplementedError('bootstrap_java_example not implemented yet')
        elif language == 'go':
            raise NotImplementedError('bootstrap_go_example not implemented yet')
        else:
            raise ValueError('Language not supported')

    def create_github_repo_from_template(self, template_repo_name, username):
        """Create a new repository from a template repository."""
        url = f"https://api.github.com/repos/{TEMPLATE_OWNER}/{template_repo_name}/generate"
        new_repo_name = f'{username}-new-flask-app'

        payload = {
            "owner": NEW_OWNER,
            "name": new_repo_name,
            "description": "This is your new repo",
            "include_all_branches": False,
            "private": False
        }

        response = requests.post(url, json=payload, headers=self.headers)
        print(response.json())
        if response.status_code == 201:
            print("Repository created successfully")
            repo_full_name = response.json()['full_name']
            self.add_user_to_repo(repo_full_name, username)
            return repo_full_name
        else:
            raise Exception(f"Failed to create repository. Status code: {response.status_code}, Message: {response.json().get('message', '')}")

    def add_user_to_repo(self, repo_full_name, username):
        """Add a user to a repository with admin access."""
        url = f"https://api.github.com/repos/{repo_full_name}/collaborators/{username}"
  
        payload = {
            "permission": "admin"
        }

        response = requests.put(url, json=payload, headers=self.headers)
        if response.status_code == 201:
            print(f"User {username} added to repository {repo_full_name}")
        elif response.status_code == 204:
            print(f"User {username} already has admin access to repository {repo_full_name}")
        else:
            print(f"Failed to add user to repository. Status code: {response.status_code}, Message: {response.json().get('message', '')}")

# Example usage
if __name__ == "__main__":
    token = "your_github_token"
    manager = GithubManager(token)
    template_repo_name = manager.get_template_repo('python')
    new_repo_full_name = manager.create_github_repo_from_template(template_repo_name, "new_github_username")

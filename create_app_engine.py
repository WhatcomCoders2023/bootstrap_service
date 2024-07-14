import subprocess
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """ Run a shell command and handle exceptions """
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running command: {e}")
        logging.error(e.stderr)
        raise
    except FileNotFoundError as e:
        logging.error(f"Command not found, ensure gcloud is installed and in PATH: {e}")
        raise
    
def initalize_app_engine(project_id, region='us-central1'):
    """Initialize a Google App Engine project"""
    command = ["gcloud", "app", "create", "--project", project_id, "--region", region]
    return run_command(command)

def set_project(project_id):
    """Set the current Google Cloud project"""
    command = ["gcloud", "config", "set", "project", project_id]
    return run_command(command)


project_id = 'whatcomcoders-bootstrap'
try:
    set_project(project_id)
    initalize_app_engine(project_id)
except Exception as e:
    logging.error(f"Error initializing App Engine: {e}")
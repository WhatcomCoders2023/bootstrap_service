from flask import Flask
from app.routes import form_routes, bootstrap_table_routes
from flask_cors import CORS


allowed_origins = [
    "http://localhost:3000",
    "https://www.whatcomcoders.com",
    "https://whatcomcoders.com",
]


def create_app():
    app = Flask(__name__)
    app.register_blueprint(form_routes.bp)
    app.register_blueprint(bootstrap_table_routes.bp)

    CORS(app, resources={r"/*": {
        "origins": allowed_origins,
        "supports_credentials": True}}, supports_credentials=True)

    # CORS(app, allowed_origins="*", access_control_allow_headers="Content-Type")
    return app
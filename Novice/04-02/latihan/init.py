from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # Set globals
    db = SQLAlchemy()
    redis_store = FlaskRedis()
    with app.app_context():
        # Set global values
        redis_store.endpoint = app.config['ENDPOINT']
        redis_store.post_query = app.config['POST_QUERY']

        # Initialize globals
        redis_store.init_app(app)
        db.init_app(app)
        # Add some routes
        from . import routes


return app

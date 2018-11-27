import os
import logging

from flask import Flask, jsonify

from bucket.db import setup_session


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('BUKKET_LOG_LVL', 'info') == 'debug':
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Log level set to DEBUG.")
    else:
        logging.basicConfig(level=logging.INFO)
        logging.info("Log level set to INFO.")

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        user = os.environ.get('DB_USER')
        host = os.environ.get('DB_HOST')
        app.config.from_mapping(
            DATABASE={
                'host': host,
                'user': user,
                'password': os.environ.get('DB_PASSWORD')
            }
        )
        logging.info(f"Using database {user}@{host}/bucket")

    app.db = setup_session(**app.config['DATABASE'])

    @app.route('/')
    def index():
        r = {
            'version': '0.1.0',
            'name': 'bukket-core'
        }
        return jsonify(r)

    from bucket import factoid
    app.register_blueprint(factoid.bp)

    return app

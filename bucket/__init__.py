import os

from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_mapping(
            DATABASE={
                'host': os.environ.get('DB_HOST'),
                'user': os.environ.get('DB_USER'),
                'password': os.environ.get('DB_PASSWORD')
            }
        )

    @app.route('/')
    def hello():
        r = {
            'version': '0.1.0',
            'name': 'bukket-core'
        }
        return jsonify(r)

    from bucket import factoid
    app.register_blueprint(factoid.bp)

    return app

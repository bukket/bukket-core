from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return "hello, world"

    from bucket import bucket
    app.register_blueprint(bucket.bp)

    return app

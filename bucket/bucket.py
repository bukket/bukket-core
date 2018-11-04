from flask import Blueprint


bp = Blueprint('bucket', __name__, url_prefix='/bucket')


@bp.route('/')
def index():
    return "Yes, this is bucket"

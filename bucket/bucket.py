from flask import Blueprint, jsonify, request

from bucket.models import Factoid
from bucket.db import get_db
from sqlalchemy.orm.exc import NoResultFound


bp = Blueprint('bucket', __name__, url_prefix='/v1/bucket')


@bp.route('/')
def index():
    return "Yes, this is bucket"


@bp.route('/factoid/')
def list_factoids():
    session = get_db()
    result = []
    if request.args.get('fact'):
        for fact in session.query(Factoid).filter(Factoid.fact == request.args['fact']).all():
            result.append(fact.serialize())
    else:
        #  Proof of concept: get 10 facts, chosen from a random starting index
        q = session.query(Factoid).all()
        import random
        maximum = len(q)
        middle = random.randint(0, maximum)
        for fact in q[middle-5:middle+5]:
            result.append(fact.serialize())

    return jsonify(result)


@bp.route('/factoid/<int:id>', methods=('GET',))
def get_factoid(id):
    session = get_db()
    try:
        f = session.query(Factoid).filter(Factoid.id == id).one()
    except NoResultFound:
        return jsonify({'error': "Not found."})
    return jsonify(f.serialize())

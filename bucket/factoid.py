from flask import Blueprint, jsonify, request

from bucket.models import Factoid
from bucket.db import get_db
from sqlalchemy.orm.exc import NoResultFound
from bucket.exceptions import FactoidNotFound


bp = Blueprint('factoid', __name__, url_prefix='/factoid')


def search_factoids(phrase, by_tidbit=False):
    session = get_db()
    results = []
    if by_tidbit is True:
        q = session.query(Factoid).filter(Factoid.tidbit.like(f"%{phrase}%")).all()
    else:
        q = session.query(Factoid).filter(Factoid.fact.like(f"%{phrase}%")).all()

    for fact in q:
        results.append(fact.serialize())
    return results


def list_exact_factoids(phrase):
    """ Given a trigger phrase, try to find a list of matching tidbits and
    return them. The behavior of choosing a random tidbit is left to the client.
    """
    session = get_db()
    results = []
    for fact in session.query(Factoid).filter(Factoid.fact == phrase).all():
        results.append(fact.serialize())
    return results


def one_factoid(id):
    """ Return a single factoid given a factoid ID """
    session = get_db()
    try:
        result = session.query(Factoid).filter(Factoid.id == id).one()
    except NoResultFound as e:
        raise FactoidNotFound from e
    else:
        return result.serialize()


@bp.route('/')
def list_factoids():
    result = {
        "error": "Factoid list not implemented."
    }
    response = jsonify(result)
    response.status_code = 501
    return response


@bp.route('/<int:id>')
def get_factoid(id):
    try:
        f = one_factoid(id)
    except FactoidNotFound:
        response = jsonify({"error": "Factoid not found."})
        response.status_code = 404
        return response
    else:
        return jsonify({"data": f})


@bp.route('/<string:phrase>')
def list_exact_factoid_route(phrase):
    factoids = list_exact_factoids(phrase)
    response = jsonify({"data": factoids})
    return response


@bp.route('/search/<string:phrase>')
def search_factoids_route(phrase):
    by_tidbit = request.args.get('tidbit', '').lower() == 'true'
    factoids = search_factoids(phrase, by_tidbit=by_tidbit)
    response = jsonify({"data": factoids})
    return response

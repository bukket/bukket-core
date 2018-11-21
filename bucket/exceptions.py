from sqlalchemy.orm.exc import NoResultFound


class FactoidNotFound(NoResultFound):
    pass

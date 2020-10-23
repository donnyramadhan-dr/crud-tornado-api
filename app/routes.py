from tornado.web import Application
from tornado_sqlalchemy import SQLAlchemy
from .config.meta import db_url

from .handlers.siswa import SiswaGetHandler, SiswaPostHandler, SiswaUpdtHandler, SiswaDelHandler


def route():
    route = [

        (r"/siswa", SiswaGetHandler),
        (r"/siswa/action/add", SiswaPostHandler),
        (r"/siswa/(?P<id>\w+)/action/update", SiswaUpdtHandler),
        (r"/siswa/(?P<id>\w+)/action/delete", SiswaDelHandler)

    ]
    return Application(route, db=SQLAlchemy(db_url), debug=True)
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.schema import MetaData
from tornado.web import RequestHandler
from abc import ABC

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html

NAMING_CINVENTION ={
    "ix" : "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metaData = MetaData(naming_convention=NAMING_CINVENTION)
Base = declarative_base(metadata=metaData)
db_url = "postgresql://slack:qwerty@localhost:5432/sekolah"

class BaseHandler(RequestHandler, ABC):
    def set_default_headers(self) :
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header("Access-Control-Allow-Methods", 'POST, GET, OPTIONS, PATCH,  PUT')
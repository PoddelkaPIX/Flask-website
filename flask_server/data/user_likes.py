import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User_likes(SqlAlchemyBase):
    __tablename__ = 'user_likes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    news = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    images = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relation('User')

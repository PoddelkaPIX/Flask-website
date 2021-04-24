import datetime
from datetime import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

time = '{:%Y-%m-%d %H:%M}'.format(datetime.now())


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    created_date = sqlalchemy.Column(sqlalchemy.String,
                                     default=time)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    images = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relation('User')


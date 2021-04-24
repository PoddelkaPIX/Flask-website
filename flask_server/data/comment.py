import datetime
from datetime import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

time = '{:%Y-%m-%d %H:%M}'.format(datetime.now())


class Comment(SqlAlchemyBase):
    __tablename__ = 'comment'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    created_date = sqlalchemy.Column(sqlalchemy.String,
                                     default=time)
    news_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("news.id"))

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

from datetime import datetime
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, SmallInteger, BigInteger, String, DECIMAL
from sqlalchemy import DateTime



BASE = declarative_base()

class Classes(BASE):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    # no = Column(String(192))
    status = Column(SmallInteger)
    type = Column(SmallInteger)
    parent_id = Column(BigInteger)
    date_s = Column(DateTime, default=datetime.utcnow)
    date_e = Column(DateTime, default=datetime.utcnow)
    link = Column(String(192))
    preview_img = Column(String(192))
    title = Column(String(192))
    note = Column(String(192))
    is_theme = Column(SmallInteger)
    level = Column(String(192))
    tag_id = Column(String(192))
    want_revised = Column(SmallInteger)
    want_recommand = Column(SmallInteger)
    created_by = Column(BigInteger)
    hosted_by = Column(BigInteger)
    deleted_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    @classmethod
    def dict_inject(cls, dict_input):
        cls.user_dict = dict_input

    def __repr__(self):
        formated_str = datetime.strftime(self.date_s, "%m/%d-%H00")
        return f"id= {self.id}, start={self.date_s}, host= {self.user_dict.get(self.hosted_by)}, topic= {self.title}"


class Users(BASE):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    no = Column(String(192))
    first_name = Column(String(192))
    last_name = Column(String(192))
    points = Column(DECIMAL(8,2))
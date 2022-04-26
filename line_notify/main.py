from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, SmallInteger, BigInteger, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import DateTime
from sqlalchemy import create_engine

from config.project_setting import sql_conf

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

    def __repr__(self):
        return f"id= {self.id}, start={self.date_s}, host= {self.hosted_by}, topic= {self.title}"

engine = create_engine(f"mysql+pymysql://{sql_conf.sql_user}:{sql_conf.sql_pw}@{sql_conf.db_url}/{sql_conf.db_database}", echo=True, future=True)
Session = sa.orm.sessionmaker(bind=engine)

BASE.metadata.create_all(engine)

s = Session()
classes = s.query(Classes)
print(classes)
for class_ in classes:
    print(class_)
s.close()
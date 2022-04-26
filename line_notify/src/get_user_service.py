import sqlalchemy as sa
from sqlalchemy import create_engine

from config.project_setting import sql_conf
from src.utils.schema import Users

engine = create_engine(f"mysql+pymysql://{sql_conf.sql_user}:{sql_conf.sql_pw}@{sql_conf.db_url}/{sql_conf.db_database}", echo=True, future=True)
Session = sa.orm.sessionmaker(bind=engine)

def get_user_dict():
    
    user_dict = {}
    with Session() as s:
        users = s.query(Users)
        for user_ in users:
            user_dict[user_.id] = f"{user_.first_name} {user_.last_name}"
    return user_dict

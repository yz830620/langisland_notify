
import sqlalchemy as sa
from sqlalchemy import create_engine

from config.project_setting import sql_conf
from src.utils.schema import Classes

from src.get_user_service import get_user_dict

user_dict = get_user_dict()
Classes.dict_inject(user_dict)

engine = create_engine(f"mysql+pymysql://{sql_conf.sql_user}:{sql_conf.sql_pw}@{sql_conf.db_url}/{sql_conf.db_database}", echo=True, future=True)
Session = sa.orm.sessionmaker(bind=engine)

# BASE.metadata.create_all(engine)

s = Session()
classes = s.query(Classes)
print(classes)
for class_ in classes:
    if class_.title and class_.hosted_by:
        print(class_)
s.close()
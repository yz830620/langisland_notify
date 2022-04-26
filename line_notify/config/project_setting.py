from pydantic import BaseSettings

class Sql_Config(BaseSettings):
    sql_user: str = "root"
    sql_pw: str = "123"
    db_url: str = "localhost:3306"
    db_database: str = "langisland"


sql_conf = Sql_Config()
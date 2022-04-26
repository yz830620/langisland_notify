from pydantic import BaseSettings

class Sql_Config(BaseSettings):
    sql_user: str = "root"
    sql_pw: str = "123"
    db_url: str = "localhost:3306"
    db_database: str = "langisland"
    db_datetime_format: str = "%m/%d/%Y, %H:%M:%S"

class LineNotifyConfig(BaseSettings):
    notification_time: int = 6
    allowed_time_difference: int = 5

sql_conf = Sql_Config()
line_notify_config = LineNotifyConfig()

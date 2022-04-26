from datetime import datetime, timedelta

from config.project_setting import sql_conf, line_notify_config

def should_notify(t1 ,t2):
    
    try:
        if isinstance(t1, str):
            t1 = datetime.strptime(t1, sql_conf.db_datetime_format)
        elif isinstance(t2, str):
            t2 = datetime.strptime(t2, sql_conf.db_datetime_format)
    except Exception:
        log.exception(f'some error happen during checking should_notify, t1 = {t1}, t2 = {t2}')

    diff = t1 - t2
    standard = timedelta(hours=line_notify_config.notification_time)
    deviation = timedelta(minutes=line_notify_config.allowed_time_difference)

    return time_difference_within(diff, standard, deviation)


def time_difference_within(diff, standard, deviation):
    return diff < standard + deviation and diff > standard - deviation

    
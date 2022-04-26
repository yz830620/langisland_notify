from datetime import datetime, timedelta
import pytest
from unittest import TestCase
from src.line_notify import should_notify


class_time = "2022-03-09 21:00:00"

dt_class_time = datetime.strptime(class_time, "%Y-%m-%d %H:%M:%S")

test_now = dt_class_time - timedelta(hours=6)


class TestNotifyClass(TestCase):
    def test_should_notify(self):
        """if test_time is around 6 hour away from now, """
        assert should_notify(dt_class_time, test_now) == True
    
    def test_should_notify_within_five_minute_difference(self):
        for i in range(1, 5):
            assert should_notify(dt_class_time, test_now + timedelta(minutes=i)) == True
            assert should_notify(dt_class_time, test_now + timedelta(minutes=i)) == True
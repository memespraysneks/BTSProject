import pytest
from dbconnection import get_db
import sqlite3
from calendarpage import get_month_data


def test_get_month_data_true():
    assert get_month_data(2022, 2) == ('February', [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 0, 0, 0, 0, 0]])
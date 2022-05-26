from calendarpage import get_last_next_week, get_last_next_month

def test_get_last_next_week():
    last_week, next_week = get_last_next_week(2022, 5, 0)
    assert last_week == "2022-4-4"
    assert next_week == "2022-5-1"

    last_week, next_week = get_last_next_week(2022, 5, 4)
    assert last_week == "2022-5-3"
    assert next_week == "2022-6-0"

def test_get_last_next_month():
    last_month, next_month = get_last_next_month(2022, 1)
    assert last_month == "2021-12"
    assert next_month == "2022-2"

    last_month, next_month = get_last_next_month(2022, 12)
    assert last_month == "2022-11"
    assert next_month == "2023-1"

from timetrack import calculate_hours, calculate_weekly_hours


def test_calculate_hours_normal_day():
    assert calculate_hours(8, 17) == 9


def test_calculate_hours_short_day():
    assert calculate_hours(9, 15) == 6


def test_calculate_hours_same_time():
    assert calculate_hours(8, 8) == 0


def test_weekly_hours():
    assert calculate_weekly_hours([8, 8, 8, 8, 8]) == 40


def test_weekly_hours_part_time():
    assert calculate_weekly_hours([4, 4, 4, 4, 4]) == 20
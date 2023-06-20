def convert_days(days: int) -> str:
    years = days//365
    remaining_days = days%365
    months = remaining_days //30
    remaining_days = remaining_days%30
    weeks = remaining_days // 7
    remaining_days = remaining_days%7
    return f'{days} days is equivalent to {years} year(s),\
{months} month(s), {weeks} week(s) and {remaining_days} day(s)'


print(convert_days(462))


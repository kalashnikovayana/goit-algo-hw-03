from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today()
    delta = today - given_date
    return delta.days

date = '2020-10-09'
days = get_days_from_today(date)
print(days)

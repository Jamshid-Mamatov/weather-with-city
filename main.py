import datetime

tday=datetime.date(2021,3,3)
print(tday.year,tday.month)
print(tday.isoweekday())
tdelta=datetime.timedelta(weeks=1)
print(tday-tdelta)
print(datetime.date())
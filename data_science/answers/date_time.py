from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar

a = date(2004, 1, 1)
b = date(2005, 1, 1)
diff = b-a
diff.days

age = date.today()-date(1986, 3, 4)
age.days

diff = datetime.now() - datetime(1970, 1, 1)
diff.total_seconds()

calendar.day_abbr[(date.today() - relativedelta(years=2, days=25)).weekday()]

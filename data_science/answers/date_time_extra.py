import pandas as pd
import plotly.express as px
import plotly.io as pio
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

pio.renderers.default = 'firefox'
flights = pd.read_csv("data_science/datasets/flights.csv")

flights['hour'] = flights['sched_dep_time'] // 100
flights['minute'] = flights['sched_dep_time'] % 100
flights['sched_dep_time_dt'] = pd.to_datetime(flights[['year', 'month', 'day', 'hour', 'minute']])

px.histogram(flights, x='minute').show()

flights['dep_part'] =pd.cut(flights['hour'], [0, 6, 12, 18, 24],
                            labels=['night', 'morning', 'afternoon', 'evening'])

px.histogram(flights, x='dep_part').show()

flights['hour'] = flights['dep_time'] // 100
flights['minute'] = flights['dep_time'] % 100
flights['dep_time_dt'] = pd.to_datetime(flights[['year', 'month', 'day', 'hour', 'minute']])

flights['hour'] = flights['arr_time'] // 100
flights['minute'] = flights['arr_time'] % 100
flights['arr_time_dt'] = pd.to_datetime(flights[['year', 'month', 'day', 'hour', 'minute']])

flights['arr_time_dt'] = flights[flights['dep_time_dt'] > flights['arr_time_dt']]['arr_time_dt'] + relativedelta(days=1)
flights[flights['dep_time_dt'] > flights['arr_time_dt']]

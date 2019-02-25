from fitparse import FitFile
from os import listdir
from os.path import isfile, join
import pytz
from pytz import timezone
import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
import datetime
import matplotlib as plt

directory = '/Users/stefan/Library/Mobile Documents/iCloud~com~altifondo~HealthFit/Documents/'

onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

# timezone = pytz.timezone("Europe/Vienna")
plt.interactive(False)

class Workout:
    def __init__(self, duration_in_seconds, timestamp, calories, avg_temperature, sport, sub_sport):
        self.duration_in_seconds = duration_in_seconds
        self.max_heart_rate = 0  # max_heart_rate
        self.avg_heart_rate = 0  # max_heart_rate
        self.date = timestamp
        self.avg_temperature = avg_temperature
        self.total_calories = calories
        self.sport = sport
        self.sub_sport = sub_sport

    def duration_minutes(self):
        return self.duration_in_seconds / 60

    def local_date(self):
        return self.date.astimezone(timezone('Europe/Vienna')).strftime('%Y-%m-%d %H:%M:%S')


workouts = []


def parse_fit_file(fit_file):
    duration_in_seconds = 0
    timestamp = '1970-01-01 00:00:00'
    calories = 0
    avg_temperature = 0
    sport = ''
    sub_sport = ''

    for record in fit_file.get_messages():

        for record_data in record:

            # Print the records name and value (and units if it has any)
            if record_data.units:
                if record_data.name == 'total_timer_time':
                    duration_in_seconds = int(record_data.value)
                elif record_data.name == 'total_calories':
                    calories = record_data.value
                elif record_data.name == 'avg_temperature':
                    avg_temperature = record_data.value
                # print(" * * {}: {} {}".format(record_data.name, record_data.value, record_data.units))
            else:
                if record_data.name == 'timestamp':
                    timestamp = pytz.utc.localize(record_data.value)
                elif record_data.name == 'sport':
                    sport = record_data.value
                elif record_data.name == 'sub_sport':
                    sub_sport = record_data.value
                # print(" * {}: {}".format(record_data.name, record_data.value))

    workouts.append(Workout(duration_in_seconds, timestamp, calories, avg_temperature, sport, sub_sport))


def read_fit_file(fit_file):
    parse_fit_file(FitFile(fit_file))


def print_heatmap():
    today = pytz.utc.localize(datetime.datetime.now())
    min_date = today

    days = []
    values = []

    for workout in workouts:
        days.append(workout.date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None))
        values.append(workout.duration_minutes())
        if workout.date < min_date:
            min_date = workout.date

    days = np.asarray(days)
    events = pd.Series(values, index=days)
    calmap.yearplot(events, year=2018)

    # all_days = pd.date_range('1/15/2014', periods=700, freq='D')
    # days = np.random.choice(all_days, 5)
    # events = pd.Series(np.random.randn(len(days)), index=days)

    # calmap.calendarplot(events, monthticks=3, daylabels='MTWTFSS',
    #                     dayticks=[0, 2, 4, 6], cmap='YlGn',
    #                     fillcolor='grey', linewidth=0,
    #                     fig_kws=dict(figsize=(8, 4)))

    plt.pyplot.show()


for index, file in enumerate(onlyfiles):
    read_fit_file(join(directory, file))

for workout in workouts:
    print('date: {}, duration: {}, calories: {}, temperature: {}, sport: {}, subsport: {}'.format(workout.local_date(), workout.duration_minutes(), workout.total_calories, workout.avg_temperature, workout.sport, workout.sub_sport))

print_heatmap()

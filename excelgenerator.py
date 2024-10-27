import pandas as pd
import openpyxl
import datetime
import random
from numpy import random
from faker import Faker
import datetime
from openpyxl import load_workbook


def generateHours(start_date, end_date, file):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    date_removed = [d.date() for d in date_range if not (3 < d.month < 11
                                                  or (d.month == 12 and (d.day == 25 or d.day == 26 or d.day == 31))
                                                  or (d.month == 1 and (d.day == 1 or d.day == 6))
                                                  or (d.month == 11 and (d.day == 1 or d.day == 11)))]

    time_fragments = 4
    time_period = int(len(date_removed)/time_fragments)
    x = [[] for _ in range(time_fragments)]
    x[0] = [f"10 - 22" for _ in(range(time_period))]
    x[1] = [f"6 - 21" for _ in (range(time_period))]
    x[2] = [f"7 - 22" for _ in (range(time_period))]
    x[3] = [f"8 - 20" for _ in (range(time_period))]

    punkty = [
        [item for sublist in [x[random.randint(0, time_fragments - 1)] for _ in range(time_fragments)] for item in
         sublist]
        for _ in range(3)
    ]
    for i in range(3):
        while len(punkty[i]) < len(date_removed):
            punkty[i].extend(punkty[i])  # Duplicate existing elements to increase length
        punkty[i] = punkty[i][:len(date_removed)]  # Trim to exact length

    data = {
        'Data': date_removed,
        'Punkt1': punkty[0],
        'Punkt2': punkty[1],
        'Punkt3': punkty[2]
    }

    df = pd.DataFrame(data)

    df.to_excel(file, index=False)


def generateReviews(start_date, end_date, file):
    fake = Faker()

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    date_array = []
    for date in date_range:
        for _ in range(random.randint(0, 10)):
            date_array.append(date.date())

    row_no = len(date_array)
    description = [fake.sentence() for _ in range(row_no)]
    rating = random.choice([1, 2, 3, 4, 5], p=[0.1, 0.2, 0.3, 0.3, 0.1], size=row_no)
    user = [fake.name() for _ in range(row_no)]
    print("generated ", row_no, " entries")
    data = {
        'UŻytkownik': user,
        'Ocena': rating,
        'Data': date_array,
        'Treść': description
    }

    df = pd.DataFrame(data)

    df.to_excel(file, index=False)


start_date = '2000-01-01'
end_date = '2010-12-31'
generateHours(start_date, end_date, 'godziny_otwarcia.xlsx')
generateReviews(start_date, end_date, 'oceny.xlsx')

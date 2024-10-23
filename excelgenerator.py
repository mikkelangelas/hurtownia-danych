import pandas as pd
import openpyxl
import datetime
import random
from faker import Faker


def generateHours():
    start_date = '2000-01-01'
    end_date = '2004-12-31'

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    # date_array = [date.date() for date in date_range]
    date_removed = [d.date() for d in date_range if not ((d.month == 12 and (d.day == 25 or d.day == 26 or d.day == 31))
                                                  or (d.month == 1 and (d.day == 1 or d.day == 6))
                                                  or (d.month == 11 and (d.day == 1 or d.day == 11))
                                                  or 3 < d.month < 11)]
    start_time = '8:00'
    end_time = '21:00'
    punkt1 = [f"{start_time} - {end_time}" for _ in(range(len(date_removed)))]

    data = {
        'Data': date_removed,
        'Punkt1': punkt1,
        'Punkt2': punkt1,
        'Punkt3': punkt1
    }

    df = pd.DataFrame(data)

    df.to_excel('godziny_otwarcia.xlsx', index=False)


def generateReviews():
    fake = Faker()
    start_date = '2000-01-01'
    end_date = '2004-12-31'

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    date_array = []
    rating = []
    description = []
    for date in date_range:
        for _ in range(random.randint(0, 100)):
            date_array.append(date.date())
            rating.append(random.randint(1, 5))
            description.append("gsdsdf")

    user = [fake.name() for _ in range(len(date_array))]
    print("generated ", len(user), " entries")
    data = {
        'UŻytkownik': user,
        'Ocena': rating,
        'Data': date_array,
        'Treść': description
    }
    df = pd.DataFrame(data)

    df.to_excel('oceny.xlsx', index=False)


generateHours()
generateReviews()

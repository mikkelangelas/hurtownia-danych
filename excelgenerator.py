import pandas as pd
import openpyxl
import datetime
import random
from numpy import random
from faker import Faker
import datetime


def generateHours(start_date, end_date, file):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    date_removed = [d.date() for d in date_range if not (3 < d.month < 11
                                                  or (d.month == 12 and (d.day == 25 or d.day == 26 or d.day == 31))
                                                  or (d.month == 1 and (d.day == 1 or d.day == 6))
                                                  or (d.month == 11 and (d.day == 1 or d.day == 11)))]

    start_time = datetime.time(8, 0)  # 8 hours, 0 minutes
    end_time = datetime.time(21, 0)  # 8 hours, 0 minutes
    punkt1 = [f"{start_time} - {end_time}" for _ in(range(len(date_removed)))]
    """for date in date_removed:
        if date.month in ([11,2,3]):
            punkt1.append(f"{start_time} - {end_time}")
    """
    data = {
        'Data': date_removed,
        'Punkt1': punkt1,
        'Punkt2': punkt1,
        'Punkt3': punkt1
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
end_date = '2004-12-31'
generateHours(start_date, end_date, 'godziny_otwarcia.xlsx')
generateReviews(start_date, end_date, 'oceny.xlsx')

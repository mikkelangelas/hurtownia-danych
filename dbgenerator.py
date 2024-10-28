import random
import csv
import datetime
import pandas as pd
from faker import Faker

from constants import *

def write_csv(items: list, filename: str):
    with open(filename, "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        for i in items:
            csv_writer.writerow(i)


def generate_pracownik(num: int, filename: str) -> list:
    pracownicy = list()

    fake = Faker(locale="pl_PL")

    for i in range(num):
        pracownicy.append((i + 1, fake.first_name(), fake.last_name(), "+48" + str(random.randint(100000000, 999999999))))

    idx = int(0.75 * num)

    write_csv(pracownicy[:idx], filename)

    return pracownicy


def generate_punkt(num: int, filename: str) -> list:
    punkty = list()

    for i in range(num):
        punkty.append((i + 1, random.randint(20, 50), random.randint(20, 50), random.randint(10, 40), random.randint(20, 80), random.randint(10, 40)))

    write_csv(punkty, filename)

    return punkty


def generate_marka(filename: str) -> list:
    marki = list()

    for marka in BRANDS:
        marki.append((marka, "+48" + str(random.randint(100000000, 999999999)), marka + "@email.com"))

    write_csv(marki, filename)

    return marki


def generate_element_wyposazenia(num: int, punkty: list, marki: list, filename: str) -> list:
    elementy_wyposazenia = list()

    for i in range(num):
        fk_punkt = (random.choice(punkty))[0]
        fk_marka = (random.choice(marki))[0]

        typ = random.choice(EQ_TYPES)

        cena = round(random.uniform(45.0, 550.0))

        if typ == "narty" or typ == "deska":
            cena = round(random.uniform(50.0, 200.0), 2)
            rozmiar = random.randint(85, 192)
        elif typ == "kask":
            cena = round(random.uniform(25.0, 70.0), 2)
            rozmiar = random.randint(48, 63)
        elif typ == "kijki":
            cena = round(random.uniform(5.0, 15.0), 2)
            rozmiar = random.randint(90, 160)
        elif typ == "buty":
            cena = round(random.uniform(50.0, 100.0), 2)
            rozmiar = random.randint(190, 325)

        elementy_wyposazenia.append((i + 1, fk_punkt, fk_marka, typ, cena, rozmiar))

    write_csv(elementy_wyposazenia, filename)

    return elementy_wyposazenia



def generate_wypozyczenie(num: int):
    pracownicy1 = generate_pracownik(150, "pracownik1.csv")
    pracownicy2 = generate_pracownik(50, "pracownik2.csv")
    marki = generate_marka("marka.csv")
    punkty = generate_punkt(3, "punkt.csv")
    elementy_wyposazenia1 = generate_element_wyposazenia(3000, punkty, marki, "element_wyposazenia1.csv")
    elementy_wyposazenia2 = generate_element_wyposazenia(200, punkty, marki, "element_wyposazeni2.csv")


    excel = pd.read_excel("godziny_otwarcia.xlsx", sheet_name=0)

    dates = excel["Data"]

    wypozyczenia1 = list()
    wypozyczenia2 = list()

    wypozyczenia_wyposazenia1 = list()
    wypozyczenia_wyposazenia2 = list()

    id = 1

    idx = int(0.75 * len(dates))

    for date in range(len(dates)):
        quantity = random.randint(500, 800)
        
        if date < idx:
            pracownicy = pracownicy1
            elementy_wyposazenia = elementy_wyposazenia1
        else:
            pracownicy = pracownicy1 + pracownicy2
            elementy_wyposazenia = elementy_wyposazenia1 + elementy_wyposazenia2

        rented = [False for _ in range(len(elementy_wyposazenia))]

        for _ in range(quantity):
            price = 0
            employee = random.choice(pracownicy)[0]
            point = random.randint(1, len(punkty))

            point_time = excel["Punkt" + str(point)][date].split(" - ")

            open_time = point_time[0] + ":00:00"
            if len(open_time.split(":")[0]) == 1:
                open_time = "0" + open_time

            close_time = point_time[1] + ":00:00"
            if len(close_time.split(":")[0]) == 1:
                close_time = "0" + close_time

            receive_time = datetime.datetime.fromisoformat(dates[date].isoformat().split("T")[0] + " " + open_time) + datetime.timedelta(hours=random.randint(0, 4))
            return_time = datetime.datetime.fromisoformat(dates[date].isoformat().split("T")[0] + " " + close_time) - datetime.timedelta(hours=random.randint(0, 4))

            diff_time = divmod((return_time - receive_time).total_seconds(), 3600)[0]

            num_equipment = random.randint(1, 5)

            for _ in range(num_equipment):
                eq_idx = random.randint(0, len(elementy_wyposazenia) - 1)

                while rented[eq_idx] is True:
                    eq_idx = random.randint(0, len(elementy_wyposazenia) - 1)

                if date < idx:
                    wypozyczenia_wyposazenia1.append((id, elementy_wyposazenia[eq_idx][0]))
                else:
                    wypozyczenia_wyposazenia2.append((id, elementy_wyposazenia[eq_idx][0]))
                
                price += elementy_wyposazenia[eq_idx][4] * diff_time

                rented[eq_idx] = True


            if date < idx:
                wypozyczenia1.append((id, employee, receive_time, return_time, round(price, 2)))
            else:
                wypozyczenia2.append((id, employee, receive_time, return_time, round(price, 2)))

            id += 1

    write_csv(wypozyczenia_wyposazenia1, "wypozyczenie_wyposazenia1.csv")
    write_csv(wypozyczenia1, "wypozyczenie1.csv")
    write_csv(wypozyczenia_wyposazenia2, "wypozyczenie_wyposazenia2.csv")
    write_csv(wypozyczenia2, "wypozyczenie2.csv")

def main():
    generate_wypozyczenie(int(input("How many: ")))



if __name__ == "__main__":
    main()
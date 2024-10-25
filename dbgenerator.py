import random
import csv
import datetime
import pandas as pd
from faker import Faker

from constants import *

def write_csv(items: list, filename: str):
    with open(filename, "w", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        for i in items:
            csv_writer.writerow(i)


def generate_pracownik(num: int) -> list:
    pracownicy = list()

    fake = Faker()

    for i in range(num):
        pracownicy.append((i + 1, fake.first_name(), fake.last_name(), "+48" + str(random.randint(100000000, 999999999))))

    write_csv(pracownicy, "pracownicy.csv")

    return pracownicy


def generate_punkt(num: int) -> list:
    punkty = list()

    for i in range(num):
        punkty.append((i + 1, random.randint(20, 50), random.randint(20, 50), random.randint(10, 40), random.randint(20, 80), random.randint(10, 40)))

    write_csv(punkty, "punkty.csv")

    return punkty


def generate_marka() -> list:
    marki = list()

    for marka in BRANDS:
        marki.append((marka, "+48" + str(random.randint(100000000, 999999999)), marka + "@email.com"))

    write_csv(marki, "marka.csv")

    return marki


def generate_element_wyposazenia(num: int, punkty: list, marki: list) -> list:
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

    return elementy_wyposazenia



def generate_wypozyczenie(num: int):
    pracownicy = generate_pracownik(200)
    marki = generate_marka()
    punkty = generate_punkt(5)
    elementy_wyposazenia = generate_element_wyposazenia(500,  punkty, marki)

    dates = pd.read_excel("godziny_otwarcia.xlsx", sheet_name=0)["Data"]

    for d in dates:
        quantity = random.randint(50, 250)
        rented = [False for _ in range(len(elementy_wyposazenia))]

        


    write_csv(dates, "daty.csv")


def main():
    generate_wypozyczenie(int(input("how many? ")))



if __name__ == "__main__":
    main()
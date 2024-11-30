USE RentMaster;

BULK INSERT dbo.Pracownik from '..\dane\pracownik1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Marka from '..\dane\marka.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Punkt from '..\dane\punkt.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.ElementWyposazenia from '..\dane\element_wyposazenia1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Wypozyczenie from '..\dane\wypozyczenie1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.WypozyczenieWyposazenia from '..\dane\wypozyczenie_wyposazenia1.csv' WITH (FIELDTERMINATOR=',');
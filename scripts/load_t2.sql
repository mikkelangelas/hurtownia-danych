USE RentMaster;

BULK INSERT dbo.Pracownik from '..\dane\pracownik2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.ElementWyposazenia from '..\dane\element_wyposazenia2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Wypozyczenie from '..\dane\wypozyczenie2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.WypozyczenieWyposazenia from '..\dane\wypozyczenie_wyposazenia2.csv' WITH (FIELDTERMINATOR=',');
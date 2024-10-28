USE RentMaster;

BULK INSERT dbo.Pracownik from 'C:\Users\msuga\Documents\studia\hurtownie\dane\pracownik1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Marka from 'C:\Users\msuga\Documents\studia\hurtownie\dane\marka.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Punkt from 'C:\Users\msuga\Documents\studia\hurtownie\dane\punkt.cdv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.ElementWyposazenia from 'C:\Users\msuga\Documents\studia\hurtownie\dane\element_wyposazenia1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Wypozyczenie from 'C:\Users\msuga\Documents\studia\hurtownie\dane\wypozyczenie1.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.WypozyczenieWyposazenia from 'C:\Users\msuga\Documents\studia\hurtownie\dane\wypozyczenie_wyposazenia1.csv' WITH (FIELDTERMINATOR=',');
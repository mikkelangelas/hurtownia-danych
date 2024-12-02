use RentMaster

BULK INSERT dbo.Pracownik from 'C:\Users\msuga\Documents\studia\hurtownie\dane\pracownik2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.ElementWyposazenia from 'C:\Users\msuga\Documents\studia\hurtownie\dane\element_wyposazenia2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.Wypozyczenie from 'C:\Users\msuga\Documents\studia\hurtownie\dane\wypozyczenie2.csv' WITH (FIELDTERMINATOR=',');
BULK INSERT dbo.WypozyczenieWyposazenia from 'C:\Users\msuga\Documents\studia\hurtownie\dane\wypozyczenie_wyposazenia2.csv' WITH (FIELDTERMINATOR=',');
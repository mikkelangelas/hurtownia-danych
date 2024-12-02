USE RentMaster;

SELECT * FROM dbo.Marka WHERE Nazwa ='Head';
UPDATE dbo.Marka SET AdresEmail = 'Head@newmail.com' WHERE Nazwa = 'Head';
SELECT * FROM dbo.Marka WHERE Nazwa ='Head';

SELECT * FROM dbo.Pracownik WHERE ID = 150;
UPDATE dbo.Pracownik SET Nazwisko = 'Kowal' WHERE ID = 150;
SELECT * FROM dbo.Pracownik WHERE ID = 150;

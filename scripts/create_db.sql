CREATE DATABASE RentMaster;
GO

USE RentMaster;
GO

CREATE TABLE Pracownik (
    ID INT PRIMARY KEY,
    Imie VARCHAR(15) NOT NULL,
    Nazwisko VARCHAR(20) NOT NULL,
    NumerTelefonu VARCHAR(15)
);
GO

CREATE TABLE Wypozyczenie (
    ID INT PRIMARY KEY,
    FK_Pracownik INT FOREIGN KEY REFERENCES Pracownik(ID),
    DataCzasWypozyczenie DATETIME,
    DataCzasZwrot DATETIME,
    Kwota FLOAT
);
GO


CREATE TABLE Marka (
    Nazwa VARCHAR(20) PRIMARY KEY,
    NumerTelefonu VARCHAR(15),
    AdresEmail VARCHAR(30)
);
GO

CREATE TABLE Punkt (
    ID INT PRIMARY KEY,
    MaxNarty INT,
    MaxDeski INT,
    MaxKaski INT,
    MaxKijki INT,
    MaxButy INT
);
GO

CREATE TABLE ElementWyposazenia (
    ID INT PRIMARY KEY,
    Punkt INT FOREIGN KEY REFERENCES Punkt(ID),
    Marka VARCHAR(20) FOREIGN KEY REFERENCES Marka(Nazwa),
    Typ VARCHAR(10),
    CenaZaGodzine FLOAT,
    Rozmiar FLOAT,
);
GO

CREATE TABLE WypozyczenieWyposazenia (
    FK_Wypozyczenie INT FOREIGN KEY REFERENCES Wypozyczenie(ID),
    FK_ElementWyposazenia INT FOREIGN KEY REFERENCES ElementWyposazenia(ID),
);
GO
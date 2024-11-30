CREATE DATABASE SkiCenterWarehouse;
GO

USE SkiCenterWarehouse;
GO

-- Table: Data
CREATE TABLE Data (
    ID_Data INT PRIMARY KEY IDENTITY(1, 1),
    Data DATE NOT NULL,
    Dzien INT NOT NULL,
    Miesiac VARCHAR(10) NOT NULL,
    NrMiesiaca INT NOT NULL,
    Rok INT NOT NULL,
    DzienTygodnia VARCHAR(15) NOT NULL
);

-- Table: Czas
CREATE TABLE Czas (
    ID_Czas INT PRIMARY KEY IDENTITY(1, 1),
    Godzina INT NOT NULL,
    Minuta INT NOT NULL,
    PoraDnia VARCHAR(15) NOT NULL
);

-- Table: Marka (SCD Type 2)
CREATE TABLE Marka (
    ID_Marka INT PRIMARY KEY IDENTITY(1, 1),
    Nazwa VARCHAR(30) NOT NULL,
    NumerTelefonu VARCHAR(15),
    AdresEmail VARCHAR(30),
    IsCurrent BIT NOT NULL
);

-- Table: Sprzet_narciarski
CREATE TABLE Sprzet_narciarski (
    ID_Sprzet INT PRIMARY KEY IDENTITY(1, 1),
    ID INT NOT NULL,
    Typ VARCHAR(30) NOT NULL
);

-- Table: Uzytkownik
CREATE TABLE Uzytkownik (
    ID_Uzytkownik INT PRIMARY KEY IDENTITY(1, 1),
    Nazwa VARCHAR(30) NOT NULL
);

-- Table: Wystawienie_recenzji
CREATE TABLE Wystawienie_recenzji (
    ID_DataWystawienia INT NOT NULL,
    ID_Uzytkownik INT NOT NULL,
    Ocena INT NOT NULL,
    PRIMARY KEY (ID_DataWystawienia, ID_Uzytkownik),
    FOREIGN KEY (ID_DataWystawienia) REFERENCES Data(ID_Data),
    FOREIGN KEY (ID_Uzytkownik) REFERENCES Uzytkownik(ID_Uzytkownik)
);

-- Table: Wypozyczenie_sprzetu
CREATE TABLE Wypozyczenie_sprzetu (
    ID_CzasWypozyczenia INT NOT NULL,
    ID_CzasZwrotu INT NOT NULL,
    ID_DataTransakcji INT NOT NULL,
    ID_SprzetNarciarski INT NOT NULL,
    ID_Marka INT NOT NULL,
    Cena DECIMAL(10, 2) NOT NULL,
    Czas INT NOT NULL,
    DlugoscDniaPracy INT NOT NULL,
    CzasOdZwrotuDoZamkniecia INT NOT NULL,
    CzasOdOtwarciaDoWypozyczenia INT NOT NULL,
	RozmiarSprzetu INT NOT NULL,
    PRIMARY KEY (ID_CzasWypozyczenia, ID_CzasZwrotu, ID_DataTransakcji, ID_SprzetNarciarski, ID_Marka),
    FOREIGN KEY (ID_CzasWypozyczenia) REFERENCES Czas(ID_Czas),
    FOREIGN KEY (ID_CzasZwrotu) REFERENCES Czas(ID_Czas),
    FOREIGN KEY (ID_DataTransakcji) REFERENCES Data(ID_Data),
    FOREIGN KEY (ID_SprzetNarciarski) REFERENCES Sprzet_narciarski(ID_Sprzet),
    FOREIGN KEY (ID_Marka) REFERENCES Marka(ID_Marka)
);
GO
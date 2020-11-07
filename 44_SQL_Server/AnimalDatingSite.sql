DROP TABLE IF EXISTS Interests;
DROP Table IF EXISTS Animals;
DROP Table IF EXISTS Species;

CREATE TABLE Species(
	ID INT PRIMARY KEY IDENTITY,
	Species VARCHAR(50) NOT NULL UNIQUE,
	FriendlyName VARCHAR(50) NOT NULL
);

CREATE TABLE Animals(
    ID INT PRIMARY KEY IDENTITY,
    Name VARCHAR(50) NOT NULL,
	SpeciesID INT NOT NULL REFERENCES Species(ID),
	ContactEmail VARCHAR(50) NOT NULL UNIQUE
 );

 -- intermediary table:
 CREATE TABLE Interests(
	AnimalID INT NOT NULL,
	SpeciesID INT NOT NULL,
	CONSTRAINT FK_InterestsAnimals FOREIGN KEY (AnimalID) REFERENCES Animals(ID),
	CONSTRAINT FK_InterestsSpecies FOREIGN KEY (SpeciesID) REFERENCES Species(ID),
	CONSTRAINT PK_Interests PRIMARY KEY(AnimalID, SpeciesID) -- compound (composite)
 );
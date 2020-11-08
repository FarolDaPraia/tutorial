INSERT INTO Species
VALUES ('Pentalagus P. furnessi', 'Bunny');

INSERT INTO Animals
VALUES ('Sally', 1, 'sally@cabe.com'),
       ('Franklin', 1, 'franklin@cabe.com');

SELECT ID, Name, SpeciesID, ContactEmail
FROM Animals;

SELECT Animals.ID, Animals.Name
FROM Animals;

SELECT Animals.ID, Animals.ContactEmail + ' - ' + Animals.Name AS Contact
FROM Animals;

Select *
FROM Animals;
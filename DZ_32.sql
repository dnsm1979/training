--Задание 0
CREATE DATABASE Birds;
--Задание 1
ALTER DATABASE Birds RENAME TO Cats;
--Задание 2
DROP DATABASE Cats;
--Задание 3
CREATE DATABASE Vegetables_and_fruits;
--Задание 4
CREATE TABLE FruitGroup(
	Title varchar(30),
	TypeFruit varchar(30),
	Color varchar(30),
	CalorieContent int,
	BriefDescription varchar(30)
);
ALTER TABLE FruitGroup ALTER COLUMN BriefDescription TYPE text;
INSERT INTO FruitGroup(Title, TypeFruit, Color, CalorieContent, BriefDescription) VALUES ('apple', 'fruit', 'green', 52, 'spherical edible apple fruit');
INSERT INTO FruitGroup(Title, TypeFruit, Color, CalorieContent, BriefDescription) VALUES ('pear', 'fruit', 'yellow', 50, 'it is a fruit that grows on pear trees');
INSERT INTO FruitGroup(Title, TypeFruit, Color, CalorieContent, BriefDescription) VALUES ('tomato', 'vegatables', 'red', 20, 'juicy fruits, usually red in color and round in shape');
INSERT INTO FruitGroup(Title, TypeFruit, Color, CalorieContent, BriefDescription) VALUES ('cucumber', 'vegatables', 'green', 15, 'Elongated cylindrical fruits');
INSERT INTO FruitGroup(Title, TypeFruit, Color, CalorieContent, BriefDescription) VALUES ('orange', 'fruit', 'orange', 75, 'round citrus fruit with orange peel');
--Задание 5
SELECT * FROM FruitGroup;
SELECT * FROM FruitGroup WHERE TypeFruit = 'vegatables';
SELECT * FROM FruitGroup WHERE TypeFruit = 'fruit';
SELECT Title, TypeFruit FROM FruitGroup;
SELECT DISTINCT Color FROM FruitGroup;
SELECT Title, Color FROM FruitGroup WHERE TypeFruit = 'fruit' AND Color = 'green';
SELECT Title, Color FROM FruitGroup WHERE TypeFruit = 'vegatables' AND Color = 'red';
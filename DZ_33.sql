--SELECT * FROM StudentGrades;
--SELECT * FROM StudentGrades WHERE AverageGrade between 3 and 4.5;
--SELECT * FROM StudentGrades WHERE BirthDate < '2003-01-01';
--SELECT * FROM StudentGrades WHERE StudentName LIKE 'Ivan%';
--SELECT * FROM StudentGrades WHERE PhoneNumber LIKE '%777%';
--SELECT * FROM StudentGrades WHERE EmailAddress LIKE 'm%';
--SELECT ALL MIN (AverageGrade) FROM StudentGrades;
--SELECT ALL MAX (AverageGrade) FROM StudentGrades;
--SELECT City, COUNT(id) FROM StudentGrades GROUP BY City;
--SELECT Country, COUNT(id) FROM StudentGrades GROUP BY Country;
--SELECT StudentName, COUNT(SubjectWithMaxGrade = 'Math.') FROM StudentGrades GROUP BY StudentName;
--SELECT GroupName, COUNT(StudentName) FROM StudentGrades GROUP BY GroupName;
--SELECT GroupName, AVG(AverageGrade) FROM StudentGrades GROUP BY GroupName;
SELECT DISTINCT SubjectWithMaxGrade, SubjectWithMinGrade FROM StudentGrades;
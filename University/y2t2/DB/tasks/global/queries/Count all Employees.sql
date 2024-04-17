SELECT
  IIF(Gender = 'Male', "Males", "Females") AS "Gender",
  COUNT(*) AS "Count"
FROM Employee
GROUP BY Gender
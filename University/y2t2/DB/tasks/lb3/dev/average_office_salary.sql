SELECT
  IIF(Department_Name = 1, "Office", "Field") AS "Department",
  AVG(Base_Pay_per_Day) AS "Average Base Pay"
FROM Position
GROUP BY Department_Name
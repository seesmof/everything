SELECT
  Employee.EmployeeID,
  Employee.EmployeeName,
  Position.PositionBasePay
FROM [Position] INNER JOIN Employee ON Employee.EmployeePosition = Position.PositionID
ORDER BY PositionBasePay DESC;
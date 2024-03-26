SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Position_ID
FROM [Position] 
INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.[Position_ID] = 2 OR Position.[Position_ID] = 4
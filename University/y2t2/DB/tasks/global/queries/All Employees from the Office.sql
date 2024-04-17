SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Department_Name
FROM [Position] INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.Department_Name = 1;

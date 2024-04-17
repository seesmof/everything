SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Base_Pay_per_Day
FROM [Position] 
INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.[Base_Pay_per_Day] < 200
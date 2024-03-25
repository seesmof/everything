Department
Department_ID primary key
Department_Name varchar not null
Department_Description varchar
Department_Manager int foreign key

Position
Position_ID primary key
Position_Name varchar not null
Position_Description varchar
Base_Pay_per_Day money not null
Department_Name int foreign key not null

Employee
Employee_ID primary key
Employee_Name varchar not null
Employee_Position int foreign key not null
Hired_Since date not null
Gender select 'Female' or 'Male'

Payroll
Payroll_ID primary key
Employee_Name foreign key not null
Payroll_Date date not null default current_date
Days_Worked int default 1
Gross_Pay money
Taxes float default 19,5%
Net_Pay money
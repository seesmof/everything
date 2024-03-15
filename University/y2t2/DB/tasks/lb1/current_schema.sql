Department
Department_ID primary key
Department_Name varchar not null
Department_Description varchar
Department_Manager varchar foreign key

Position
Position_ID primary key
Position_Name varchar not null
Position_Description varchar
Base_Pay_per_Day money not null
Department_Name varchar foreign key not null

Employee
Employee_ID primary key
Employee_Name varchar not null
Employee_Position varchar foreign key not null
Department_Name varchar foreign key not null
Hired_Since date not null
Age int
Gender varchar foreign key
Date_of_Birth date

Payroll
Payroll_ID primary key
Employee_Name varchar foreign key not null
Payroll_Date date not null default current_date
Days_Worked int default 1
Gross_Pay money
Taxes float default 19,5%
Net_Pay money

Gender
Gender_ID primary key
Gender_Name varchar
Short_Name varchar(1)
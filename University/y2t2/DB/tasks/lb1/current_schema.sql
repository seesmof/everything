Gender
Gender_ID primary key
Gender_Name varchar not null
Short_Name varchar(1) not null

Department
Department_ID primary key
Department_Name varchar not null
Department_Description varchar
Department_Manager foreign key

Position
Position_ID primary key
Position_Name varchar not null
Position_Description varchar
Base_Pay_per_Day money not null
Department_Name foreign key not null

Employee
Employee_ID primary key
Employee_Name varchar not null
Employee_Position foreign key not null
Hired_Since date not null
Gender foreign key

Payroll
Payroll_ID primary key
Employee_Name foreign key not null
Payroll_Date date not null default current_date
Days_Worked int default 1
Gross_Pay money
Taxes float default 19,5%
Net_Pay money
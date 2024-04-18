Department
Department_ID primary key
Department_Name varchar not null
Department_Description varchar

Position
Position_ID primary key
Position_Name varchar not null
Position_Description varchar
Base_Pay_per_Month money not null
Department_Name int foreign key not null

Employee
Employee_ID primary key
Employee_Name varchar not null
Employee_Position int foreign key not null
Gender select 'Female' or 'Male'

Allowance
Allowance_ID primary key
Employee_Name foreign key not null
Allowance_Type varchar not null select ['Health', 'Transportation', 'Food', 'Education', 'Sick Leave', 'Vacation', 'Years of Service', 'Voluntary Encouragement', 'Overtime', 'Other']
Allowance_Amount money not null
Allowance_Note varchar

Deduction
Deduction_ID primary key
Employee_Name foreign key not null
Deduction_Type varchar not null select ['Health Insurance', 'Retirement Plan', 'Union Membership', 'Charity', 'Other']
Deduction_Amount money not null
Deduction_Note varchar

Tax
Tax_ID primary key
Tax_Type varchar not null
Tax_Rate float not null
Tax_Note varchar

Payroll
Payroll_ID primary key
Employee_Name foreign key not null
Payroll_Date date not null default current_date
Gross_Pay money
Allowances money
Deductions money
Taxes float default 19,5%
Net_Pay money
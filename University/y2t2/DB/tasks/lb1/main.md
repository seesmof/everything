<div align="center">
  <h3>Звіт з Лабораторної Роботи №1</h3>
  <p>Виконав <strong>Онищенко Олег</strong>, студент групи <strong>КНТ-122</strong></p>
</div>

#### Резюме

В рамках лабораторної роботи 1 було розроблено локальне подання до предметної області **автоматизована система розрахунку заробітної плати**, в яку входять 3 сутності:

- компанія
- підрозділ
- працівник

#### Опис сутностей та зв'язків між ними

| №   | Назва сутності | Клас приналежності | Ступінь зв'язку | Ключове поле | Зв'язана сутність    |
| --- | -------------- | ------------------ | --------------- | ------------ | -------------------- |
| 1   | Department     | Обов'язковий       | 1:N, N:1        | DepartmentID | Position, Employee   |
| 2   | Position       | Обов'язковий       | 1:N, N:1        | PositionID   | Employee, Department |
| 3   | Employee       | Обов'язковий       | N:1             | EmployeeID   | Department, Position |
| 4   | Payroll        | Необов'язковий     | 1:1             | EmployeeID   | Employee             |

#### Опис атрибутів сутностей

| №                     | Назва атрибуту        | Є ключем  | Тип даних  | Обов'язковий до заповнення | Маска введення |
| --------------------- | --------------------- | --------- | ---------- | -------------------------- | -------------- |
| **Department Entity** |
| 1                     | DepartmentID          | Первинний | autonumber | +                          |                |
| 2                     | DepartmentName        |           | string     | +                          |                |
| 3                     | DepartmentDescription |           | string     |                            |                |
| **Employee Entity**   |
| 1                     | EmployeeID            | Первинний | autonumber | +                          |                |
| 2                     | EmployeeName          |           | string     | +                          |                |
| 3                     | EmployeePosition      | Зовнішній | string     | +                          |                |
| 4                     | DepartmentID          | Зовнішній | int        | +                          |                |
| 5                     | HiredSince            |           | date       | +                          |                |
| **Position Entity**   |
| 1                     | PositionID            | Первинний | autonumber | +                          |                |
| 2                     | PositionName          |           | string     | +                          |                |
| 3                     | PositionDescription   |           | string     |                            |                |
| 4                     | PositionBasePay       |           | money      | +                          |                |
| 5                     | DepartmentID          | Зовнішній | int        | +                          |                |
| **Payroll**           |
| 1                     | PayrollID             | Первинний | autonumber | +                          |                |
| 2                     | EmployeeName          | Зовнішній | string     | +                          |                |
| 3                     | PayrollDate           |           | date       | +                          |                |
| 4                     | DaysWorked            |           | int        |                            |                |
| 5                     | GrossPay              |           | money      |                            |                |
| 6                     | Taxes                 |           | float      |                            |                |
| 7                     | NetPay                |           | money      |                            |                |

#### Схема даних

![Схема даних](https://lh3.googleusercontent.com/pw/AP1GczN9LsWqVefmopo097DwPewnS2xCQscT6J_yLJZIXUuG4_esqn3GW-iDsNcXnMfq7fThM4t8_f9FzpjF7xo5mZvbNi2A4_s_UCOzkK_CKxt3Q5yJR5nNUXSIm3_JdsZnxwk4BxScBuAbyLHTmYEeJD1NSQ=w1132-h441-s-no?authuser=0)

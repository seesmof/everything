<div align="center">
  <h3>Звіт з Лабораторної Роботи №1</h3>
  <p>Виконав <strong>Онищенко Олег</strong>, студент групи <strong>КНТ-122</strong></p>
</div>

#### Резюме

В рамках лабораторної роботи 1 було розроблено локальне подання до предметної області **автоматизована система розрахунку заробітної плати**, в яку входять 5 сутностей:

- Gender
- Department
- Position
- Employee
- Payroll

#### Опис сутностей та зв'язків між ними

| №   | Назва сутності | Клас           | Ступінь зв'язку | Ключове поле  | Зв'язані сутності                     |
| --- | -------------- | -------------- | --------------- | ------------- | ------------------------------------- |
| 1   | Gender         | Необов'язковий | 1:N             | Gender_ID     | Employee                              |
| 2   | Department     | Обов'язковий   | 1:N, N:1        | Department_ID | Employee, Position                    |
| 3   | Position       | Обов'язковий   | 1:N, N:1        | Position_ID   | Employee, Department                  |
| 4   | Employee       | Обов'язковий   | 1:N, N:1        | Employee_ID   | Department, Position, Payroll, Gender |
| 5   | Payroll        | Необов'язковий | N:1             | Payroll_ID    | Employee                              |

#### Опис атрибутів сутностей

| №          | Назва атрибуту         | Є ключем | Тип даних  | Обов'язковий? | Маска |
| ---------- | ---------------------- | -------- | ---------- | ------------- | ----- |
| Gender     |
| 1          | Gender_ID              | primary  | autonum    |               |       |
| 2          | Gender_Name            |          | varchar    | +             |       |
| 3          | Short_Name             |          | varchar(1) | +             |       |
| Department |
| 1          | Department_ID          | primary  | autonum    |               |       |
| 2          | Department_Name        |          | varchar    | +             |       |
| 3          | Department_Description |          | varchar    |               |       |
| 4          | Department_Manager     | foreign  | int        |               |       |
| Position   |
| 1          | Position_ID            | primary  | autonum    |               |       |
| 2          | Position_Name          |          | varchar    | +             |       |
| 3          | Position_Description   |          | varchar    |               |       |
| 4          | Base_Pay_per_Day       |          | money      | +             |       |
| 5          | Department_Name        | foreign  | int        | +             |       |
| Employee   |
| 1          | Employee_ID            | primary  | autonum    |               |       |
| 2          | Employee_Name          |          | varchar    | +             |       |
| 3          | Employee_Position      | foreign  | int        | +             |       |
| 4          | Hired_Since            |          | date       | +             |       |
| 5          | Gender                 | foreign  | int        |               |       |
| Payroll    |
| 1          | Payroll_ID             | primary  | autonum    |               |       |
| 2          | Employee_Name          | foreign  | int        | +             |       |
| 3          | Payroll_Date           |          | date       | +             |       |
| 4          | Days_Worked            |          | int        |               |       |
| 5          | Gross_Pay              |          | money      |               |       |
| 6          | Taxes                  |          | money      |               |       |
| 7          |                        | Net_Pay  |            | money         |       |

#### Схема даних

![Схема даних](https://lh3.googleusercontent.com/pw/AP1GczNTgg3jfvfm30LjTfwwXw5t4MnMgaoJ6JWlg2Wk891OmlTD5mO6Wep2Kpuqvev8D1uynitAhaDI_V7v5GWCvfAD0xjR5PsFsurkAUl20Gfyg2VZQpdrVgQr4TE73hPBzbX57qnBYeNoyMpx-rRSJLXh2w=w873-h776-s-no?authuser=1)

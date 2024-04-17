<div align="center">
  <h3>Звіт з Лабораторної Роботи №3</h3>
  <p>Виконав <strong>Онищенко Олег</strong>, студент групи <strong>КНТ-122</strong></p>
</div>

#### Резюме

В рамках лабораторної роботи 3 було спроектовано 4 складних запити до схеми даних з предметної області **автоматизована система розрахунку заробітної плати**. Деталі запитів наведені нижче.

- отримати середню зарплату для кожного відділу
- порахувати всіх працівників, згрупованих за статтю
- додати нового працівника Аврама у відділ
- змініть ім'я Аврама на Авраам

#### Запити до бази даних

##### Середня зарплатня

###### Запит мовою SQL

```sql
SELECT
  IIF(Department_Name = 1, "Office", "Field") AS "Department",
  AVG(Base_Pay_per_Day) AS "Average Base Pay"
FROM Position
GROUP BY Department_Name
```

###### Результати запиту

Результати запиту наведено нижче у вигляді знімку з екрану.

![Query Results](https://lh3.googleusercontent.com/pw/AP1GczNIuBhC6WYjzQMyJlrArIKBnSV6xgAQGI9rKykkTJ3ozKRywCAYs3AXZpaf2P6OH7o5WpEfzu9izy22CkpssNOQPyFYbZRVbxaH94bREdYpK0lM1nITVBfAG5nkkLu5z29saCeotIM4X-iGy249XNX41Q=w358-h60-s-no?authuser=0)

##### Кількість працівників

###### Запит мовою SQL

```sql
SELECT
  IIF(Gender = 'Male', "Males", "Females") AS "Gender",
  COUNT(*) AS "Count"
FROM Employee
GROUP BY Gender
```

###### Результати запиту

Результати запиту наведено нижче у вигляді знімку з екрану.

![Query Results](https://lh3.googleusercontent.com/pw/AP1GczNLX5sjzxdZvSqdcoMJyM9wKcLZErq2QsafN5NytRER_9Kw4lMlJ2mjDvIwIb4cy8YRdFIHWG-cfLiLGRB3cT_BycNkKjGo6EBwPFoi-UgKbuug995TPEKlsODtYCwOUhV2Od2AEnVjRdpFKMXvDK_9xg=w191-h59-s-no?authuser=0)

##### Додання Аврама у офіс

###### Запит мовою SQL

```sql
INSERT INTO Employee (Employee_Name, Employee_Position, Hired_Since, Gender)
VALUES ("Abram", 1, "2024-04-01", "Male");
```

###### Результати запиту

Аби виконати запит, потрібно двічі натиснути на нього у списку об'єктів Microsoft Access, після чого з'явиться вікно підтвердження, де необхідно натиснути "Так" задля виконання операції додавання нового об'єкту у таблицю "Employee".

Вікно підтвердження виглядає наступним чином:

![Вікно підтвердження](https://lh3.googleusercontent.com/pw/AP1GczPfsLu2he7PLRXYQKfv_IQjqglOb6PA6J1UG9d5ioMphJb2l00KDQP5HmGHEzOjyEIA_iKAgszl5rJh90NwtZyamcbo1ZdrT3GQ9wWiWM5btEcF2H6H5GWfAosP_H-cF71VleBEKoPttP9HIP2xgEqQ9Q=w363-h246-s-no?authuser=0)

Результати запиту наведено нижче у вигляді знімку з екрану.

![Query Results](https://lh3.googleusercontent.com/pw/AP1GczP_ofp2O0vEpNvLF1s4eJS0kTs5WxpG8IvZRwF2Weixn1DIFtqIMH8jGOhmX-0qEe6INV5imLK-M-JOykuS5TY-4HFFD8X5uWHS_6e1iY_eLoxhX269cufLDVhhdpNV6-kMJkreIYC7yORc2DY0IQ44kg=w726-h175-s-no?authuser=0)

Можемо бачити новододаний об'єкт в таблиці "Employee" під індексом 14.

##### Перейменування Аврама

###### Запит мовою SQL

```sql
UPDATE Employee
SET Employee_Name = "Abraham"
WHERE Employee_Name = "Abram"
```

###### Результати запиту

Аналогічна процедура виконання запиту на зміну елементу - натискаємо двічі на запит у списку об'єктів Microsoft Access і підтверджуємо наші наміри у відповідному вікні.

Результати запиту наведено нижче у вигляді знімку з екрану.

![Query Results](https://lh3.googleusercontent.com/pw/AP1GczPkE9MpAoq1rmfDP7InpFYYBGVVYBbW4hxEg0J2Xtsi9Zv029LvHptZUIpLxvg1dE8ZT_dB-uBDlsopyrksu1HdgNtVK5leR_OkdIIaNrXyNnlHTZ9pYfLdjbdouUjiwgYZ4hIWGo5FFUTUhPD11FXdmA=w724-h176-s-no?authuser=0)

Можемо бачити об'єкт в таблиці "Employee" під індексом 14 зі зміненою властивістю "Employee_Name" на "Abraham".

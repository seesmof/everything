<div align="center">
  <h3>Звіт з Лабораторної Роботи №2</h3>
  <p>Виконав <strong>Онищенко Олег</strong>, студент групи <strong>КНТ-122</strong></p>
</div>

#### Резюме

В рамках лабораторної роботи 2 було спроектовано 4 запити до схеми даних з предметної області **автоматизована система розрахунку заробітної плати**. Деталі запитів наведені нижче.

- Відібрати всіх співробітників, якщо вони працюють в офісі
- Відібрати всіх працівників, якщо їхня базова зарплатня менша за 200
- Відібрати всіх співробітників, які є менеджерами
- Відібрати всіх співробітників-жінок

#### Запити до бази даних

##### Працівники з офісу

###### Запит мовою SQL

```sql
SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Department_Name
FROM [Position]
INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.Department_Name = 1
```

Оскільки Department_Name є зовнішнім ключем, то зазначаємо індекс департаменту, який нас цікавить. Таблиця Department виглядає наступним чином:
![Таблиця департаментів](https://lh3.googleusercontent.com/pw/AP1GczNjxyqDNDV3z9xPDUX-JWcQ6XlIQa0ypPS3aDSc-9gt-Oo09ERwQJOkzIIAhv80qquFamaidSpsDIbqjkm5fwY0CUTdu-QRFKiXkk9kp1AcBI4FEcMQf7M245dvtFEkl6xWuEfOIzpYkRywP40mS9R09Q=w1393-h46-s-no?authuser=0)

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат](https://lh3.googleusercontent.com/pw/AP1GczM6mj4nxBotDTDeTVxgxislaXAQMRtQ6TKsi7AKhY29dOlPvLvp5yoWGLST4RX22AUSYXSAhV-8hSy5Gj9zop7LLMew4X8c-pfTZOw-4tqiwPQghqCw9-7YqR-dq_odcV3XCuwM0QCAzvt4F0cIeVfnHw=w986-h128-s-no?authuser=0)

##### Працівники з нижчою базовою зарплатой

###### Запит мовою SQL

```sql
SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Base_Pay_per_Day
FROM [Position]
INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.[Base_Pay_per_Day] < 200
```

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат]()

##### Працівники які є менеджерами

###### Запит мовою SQL

```sql

```

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат]()

##### Працівники жінки

###### Запит мовою SQL

```sql

```

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат]()

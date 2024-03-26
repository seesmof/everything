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

Таблиця Position має наступний вигляд:

![Таблиця позицій](https://lh3.googleusercontent.com/pw/AP1GczNb4LjpmimhsCUtnKxTniBoRqvd-GkTUPC6cF6xCAILejW6RbB-Hlt0_Yc6jlvrYxYpjY9MhFccNds7e9CfNbRoMibkT-UoiQmas26N5XrzTzelD3X2039zawuw8ScEzG1eG0v-oT9uhKXLZUqTEKmCCQ=w1393-h90-s-no?authuser=0)

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат](https://lh3.googleusercontent.com/pw/AP1GczM9CDSIElPjoVNCzQEv0GIEM1MGzsVrkS1KPZWDPIKB57tRl1ftFFTAO27Wl-kaYozcmxCJZ28Idr_edwXDTBDjBFgDLj2mwsEdreM0bIw-RfCLsQsPN9jOV3IEsNfoLuNmrlluprStcHM8dEufQ8hwow=w832-h192-s-no?authuser=0)

##### Працівники які є менеджерами

###### Запит мовою SQL

```sql
SELECT Employee.Employee_Name, Employee.Employee_Position, Position.Position_ID
FROM [Position]
INNER JOIN Employee ON Position.[Position_ID] = Employee.[Employee_Position]
WHERE Position.[Position_ID] = 2 OR Position.[Position_ID] = 4
```

Де 2 та 4 є ідексами позицій Office Manager та Field Supervisor.

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат](https://lh3.googleusercontent.com/pw/AP1GczOZ2Eo4WQGIMPFA0YUntFvZ-BI51lWkf6AZDtaECLBPokvDD7IMCauyw9UHOfamYvK_FSSx3l3HJ_tukrtYWisdTV7PMrs6kXqbtnSFVFU5qwRauy07tkZE7oNKTISRgfITT_NS_MTRCispr2zZzlOTSw=w741-h96-s-no?authuser=0)

##### Працівники жінки

###### Запит мовою SQL

```sql
SELECT Employee.Employee_Name, Employee.Employee_Position, Employee.Gender
FROM Employee
WHERE Employee.Gender = 'Female'
```

###### Результати запиту

В результаті запиту отримуємо таблицю наступного вигляду:

![Результат](https://lh3.googleusercontent.com/pw/AP1GczMqI7rAcNeThyQP06TElohYpCMovd_R-G-dASE_hjY3-xjNfZz8YFGLv46TIPLQGMlZTkSnwXgodF7XN0Rwo6DVZWeRg7RsHFTAfYgYCoLvbjwqvWtwRd1m4n-hcSYWVTHJnnHkuZH6-PiYgaus3V3y2A=w667-h116-s-no?authuser=0)

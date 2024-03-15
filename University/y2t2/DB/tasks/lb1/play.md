## Мета роботи

Ознайомитися з системою керування базами даних PostgreSQL, набути початкових навичок роботи з нею та створити схему бази даних.

## Завдання до роботи

- Ознайомитися зі змістом теоретичних відомостей
- Відповідно до індивідуального завдання розробити схему бази даних за допомогою інструментів PgAdmin та мови SQL
- Ввести необхідні дані

---

- window installation company
  - departments
    - material acquirers
    - window installers
  - employees
    - name
    - department
    - position
    - birth date
    - address
    - gender
    - age

---

- employee
  - name
  - age
  - gender
  - position
  - department
- salary
  - total
  - -ЄСВ (Єдиний Соціальний Внесок) = 22%
  - gross
  - -НДФЛ = 18%
  - -Військовий Збір = 1.5%
  - net
- company
  - name
  - description
  - departments
  - website
  - phone
- departments
  - name
  - description
  - employees
  - manager

---

### Office Administration Department (OAD)

**Description**: This department is responsible for the internal functioning of the company. They handle contracts, procurement of materials, scheduling of jobs, and overall management of office tasks.

- **Positions**:
  - **Administrative Assistant**
    - **Base Pay**: $120/day
    - **Role**: Assists in daily office needs and managing general administrative activities.
  - **Office Manager (Supervisor)**
    - **Base Pay**: $200/day
    - **Role**: Oversees the entire office operations, supervises staff, and ensures compliance with company policies.

### Field Operations Department (FOD)

**Description**: The FOD is the backbone of the company, where the actual installation of windows takes place. They are responsible for on-site work, customer interactions, and ensuring installations are completed efficiently.

- **Positions**:
  - **Installation Technician**
    - **Base Pay**: $150/day
    - **Role**: Performs the installation of windows at various job sites, following safety and quality standards.
  - **Field Supervisor**
    - **Base Pay**: $230/day
    - **Role**: Manages the installation teams, coordinates with the OAD for materials, and ensures project deadlines are met.

---

Francis Beck
Brent Arnold
Lettie Alexander
Glenn Fernandez

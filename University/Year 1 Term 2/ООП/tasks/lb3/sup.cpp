#include <bits/stdc++.h>
#include "../../../lib.h"
#include "sup.h"
using namespace std;

// Варіант 4.Створити базовий клас Людина. Кожний об’єкт класу повинен містити наступні дані: ПІБ, рік народження, стать.
// Клас повинен виконувати наступні дії: ініціалізація інформації, введення-виведення інформації.
// Варіант 5.Створити базовий клас Людина, відповідно до варіанту 4.
// Створити похідний клас Інженер, що містить додаткові дані: рік закінчення, ВУЗ, спеціальність, тип диплому, тип навчання, перекваліфікація (динамічний масив), місце роботи, заробітня платня.
// Клас повинен містити наступні методи: ініціалізації інформації, розрахунок заробітної платні, розрахунок щорічного доходу, додавання інформацій щодо перекваліфікації.

// base class human
class Human
{
protected:
    string fullName;
    ll birthYear;
    char gender;

public:
    // default constructor
    Human() {}

    // parameterized constructor
    Human(string const &inputName, ll inputYear, char inputGender)
        : fullName(inputName), birthYear(inputYear), gender(inputGender) {}

    // copy constructor
    Human(const Human &other)
        : fullName(other.fullName), birthYear(other.birthYear), gender(other.gender) {}

    // setters and getters for gender
    char getGender() const { return gender; }
    void setGender(char inputGender) { gender = inputGender; }

    // setters and getters for birth year
    ll getBirthYear() const { return birthYear; }
    void setBirthYear(ll inputBirthYear) { birthYear = inputBirthYear; }

    // setters and getters for name
    string getFullName() const { return fullName; }
    void setFullName(string inputFullName) { fullName = inputFullName; }

    // default destructor
    ~Human() {}
};

// derived class Engineer
class Engineer : public Human
{
private:
    ll graduationYear;
    string universityName;
    string specialtyName;
    string typeOfDiploma;
    string typeOfStudy;
    vector<string> retrainingsVector;
    string placeOfWork;
    ll salaryAmount;

public:
    // default constructor
    Engineer() {}

    // parameterized constructor
    Engineer(string const &name, ll bYear, char gender, ll gradYear, string const &uni, string const &specialty, string const &diploma, string const &study, const vector<string> &retrainings, string const &work, ll salary)
        : Human(name, bYear, gender),
          graduationYear(gradYear),
          universityName(uni),
          specialtyName(specialty),
          typeOfDiploma(diploma),
          typeOfStudy(study),
          retrainingsVector(retrainings),
          placeOfWork(work),
          salaryAmount(salary)
    {
    }

    // copy constructor
    Engineer(const Engineer &other)
        : Human(other), graduationYear(other.graduationYear),
          universityName(other.universityName),
          specialtyName(other.specialtyName),
          typeOfDiploma(other.typeOfDiploma),
          typeOfStudy(other.typeOfStudy),
          retrainingsVector(other.retrainingsVector),
          placeOfWork(other.placeOfWork),
          salaryAmount(other.salaryAmount)
    {
    }

    // setters and getters for graduation year
    ll getGraduationYear() const { return graduationYear; }
    void setGraduationYear(ll gradYear) { graduationYear = gradYear; }

    // setters and getters for university name
    string getUniversityName() const { return universityName; }
    void setUniversityName(string const &uni) { universityName = uni; }

    // setters and getters for specialty name
    string getSpecialty() const { return specialtyName; }
    void setSpecialty(string const &specialty) { specialtyName = specialty; }

    // setters and getters for type of diploma
    string getDiploma() const { return typeOfDiploma; }
    void setDiploma(string const &diploma) { typeOfDiploma = diploma; }

    // setters and getters for type of study
    string getStudyType() const { return typeOfStudy; }
    void setStudyType(string const &studyType) { typeOfStudy = studyType; }

    // setters and getters for retrainings
    vector<string> getRetrainings() const { return retrainingsVector; }
    void setRetrainings(const vector<string> &retrainings) { retrainingsVector = retrainings; }

    // setters and getters for work place
    string getWorkPlace() const { return placeOfWork; }
    void setWorkPlace(string const &workPlace) { placeOfWork = workPlace; }

    // setters and getters for salary
    ll getSalary() const { return salaryAmount; }
    void setSalary(ll salary) { salaryAmount = salary; }

    // default desctructor
    ~Engineer() {}
};

// for outputting all added engineers
void showPeople(vector<unique_ptr<Engineer>> &engineersVector)
{
    // get engineers amount and check if the vector is empty
    ll engineersCount = engineersVector.size();
    if (engineersCount == 0)
    {
        // if so output the message and stop function execution
        cout << GRAY << "No people found\n"
             << UNGRAY;
        return;
    }

    // else output all the engineers using a loop
    cout << BOLD << "Engineers (" << engineersCount << "):\n\n"
         << UNBOLD;
    for (ll i = 0; i < engineersCount; i++)
    {
        // process gender by getting the gender letter and converting it to a string with a corresponding name
        string genderHolder;
        if (engineersVector[i]->getGender() == 'M' || engineersVector[i]->getGender() == 'm')
            genderHolder = "Male";
        else
            genderHolder = "Female";

        // output all the information, utilize different functions and perform various calculations
        cout << "(" << i + 1 << ") " << engineersVector[i]->getFullName() << "- " << 2023 - engineersVector[i]->getBirthYear() << " years old • " << genderHolder << endl
             << "    Graduated " << engineersVector[i]->getGraduationYear() << " from " << engineersVector[i]->getUniversityName() << "on " << engineersVector[i]->getSpecialty() << "with a diploma of " << engineersVector[i]->getDiploma() << endl
             << "    Studied " << engineersVector[i]->getStudyType() << "and now works at " << engineersVector[i]->getWorkPlace() << "where gets $" << engineersVector[i]->getSalary() << " a month or $" << engineersVector[i]->getSalary() * 12 << " a year\n";
        // check if the engineer has retrainings
        if (engineersVector[i]->getRetrainings().size() > 0)
        {
            // if so output them using a loop
            cout << "\n    List of retrainings (" << engineersVector[i]->getRetrainings().size() << "):\n";
            for (ll k = 0; k < engineersVector[i]->getRetrainings().size(); k++)
                cout << "    • " << engineersVector[i]->getRetrainings().at(k) << endl;
        }
        cout << endl;
    }
}

// for adding engineers into the container
void addPeople(vector<unique_ptr<Engineer>> &engineersVector)
{
    // ask how many people to add and validate the input
    cout << "Amount to add: ";
    ll amount = getNum();
    cout << endl;
    // check if the amount is more than one
    if (amount < 1)
    {
        // if so output the error and stop function execution
        cout << RED << "\nERROR: Amount must be positive\n"
             << UNRED;
        return;
    }

    // for the specified amount of people
    for (ll i = 0; i < amount; i++)
    {
        // ask user to enter engineer's full name
        cin.ignore();
        cout << "(" << i + 1 << ") ";
        string fullNameHolder;
        cout << "Full Name: ";
        getline(cin, fullNameHolder);
        // and validate it
        fullNameHolder = validateName(fullNameHolder);

        // ask user to enter engineer's gender
        cout << "    ";
        char genderHolder;
        cout << "Gender (M | F): ";
        cin >> genderHolder;

        // ask user to enter engineer's university name
        cout << "    ";
        cin.ignore();
        string universityNameHolder;
        cout << "University Name: ";
        getline(cin, universityNameHolder);
        // and validate it
        universityNameHolder = validateName(universityNameHolder);

        // ask user to enter engineer's specialty name
        cout << "    ";
        string specialtyNameHolder;
        cout << "Specialty Name: ";
        getline(cin, specialtyNameHolder);
        // and validate it
        specialtyNameHolder = validateName(specialtyNameHolder);

        // ask user to enter engineer's diploma type
        cout << "    ";
        string diplomaTypeHolder;
        cout << "Diploma Type (Bachelor | Master): ";
        getline(cin, diplomaTypeHolder);
        // and validate it
        diplomaTypeHolder = validateName(diplomaTypeHolder);

        // ask user to enter engineer's study type
        cout << "    ";
        string studyTypeHolder;
        cout << "Study Type (Full-Time | Part-Time): ";
        getline(cin, studyTypeHolder);
        // and validate it
        studyTypeHolder = validateName(studyTypeHolder);

        // ask user to enter engineer's work place
        cout << "    ";
        string workPlaceHolder;
        cout << "Work Place: ";
        getline(cin, workPlaceHolder);
        // and validate it
        workPlaceHolder = validateName(workPlaceHolder);

        // ask user to enter engineer's retrainings amount
        vector<string> retrainingsVectorHolder;
        cout << "    ";
        cout << "Enter the amount of retrainings: ";
        ll retrainingsAmount = getNum();
        cin.ignore();
        // for the specified amount
        for (ll k = 0; k < retrainingsAmount; k++)
        {
            // ask user to enter engineer's retrainings one by one
            string retrainingHolder;
            cout << "    ";
            cout << "    ";
            cout << "• ";
            getline(cin, retrainingHolder);
            // validate them and add them to the retrainings vector
            retrainingHolder = validateName(retrainingHolder);
            retrainingsVectorHolder.eb(retrainingHolder);
        }

        // ask user to enter engineer's monthy salary
        cout << "    ";
        ll montlySalaryHolder;
        cout << "Monthy Salary: $";
        montlySalaryHolder = getNum();

        // ask user to enter engineer's birth year
        cout << "    ";
        ll birthYearHolder;
        cout << "Birth Year: ";
        birthYearHolder = getNum();
        // check if the birth year is invalid
        if (birthYearHolder > 2023)
            // if so output the message
            cout << RED << "\nERROR: Birth year cannot be greater than 2023\n\n"
                 << UNRED;

        // ask user to enter engineer's gradution year
        cout << "    ";
        ll gradYearHolder;
        cout << "Graduation Year: ";
        gradYearHolder = getNum();

        // add new object to vector and continue
        engineersVector.eb(make_unique<Engineer>(fullNameHolder, birthYearHolder, genderHolder, gradYearHolder, universityNameHolder, specialtyNameHolder, diplomaTypeHolder, studyTypeHolder, retrainingsVectorHolder, workPlaceHolder, montlySalaryHolder));
        cout << endl;
    }

    // output success message
    cout << GREEN << endl
         << amount << " objects successfully added\n\n"
         << UNGREEN;
}

// for removing people from the vector
void removePeople(vector<unique_ptr<Engineer>> &engineersVector)
{
    // check if there are people in the vector at all
    if (engineersVector.size() == 0)
    {
        // if not output the message and stop function exectuion
        cout << GRAY << "No objects to delete\n"
             << UNGRAY;
        return;
    }

    // ask user to enter number of student ot delete
    cout << "Enter number to delete: ";
    ll number = getNum();
    // fit the number to indices
    number--;
    // check if the number is out of range of the vector
    if (number < 0 || number > engineersVector.size())
    {
        // if so output the error and stop function execution
        cout << RED << "\nERROR: Invalid number entered\n"
             << UNRED;
        return;
    }

    // delete vector object at the index and ouput the message
    engineersVector.erase(engineersVector.begin() + number);
    cout << GREEN << "\nObject successfully deleted\n\n"
         << UNGREEN;
}

// for editing properties of the people in a vector
void editPeople(vector<unique_ptr<Engineer>> &engineersVector)
{
    // check if there are people in the vector
    if (engineersVector.size() == 0)
    {
        // if not output the message and stop function execution
        cout << GRAY << "No people to edit\n"
             << UNGRAY;
        return;
    }

    // ask user to enter number of object to edit
    cout << "Enter number to edit: ";
    ll number = getNum();
    // fit it to the indeces
    number--;
    // check if the number is out of range of the vector
    if (number < 0 || number > engineersVector.size())
    {
        // output the message and stop function execution
        cout << RED << "\nERROR: Invalid number entered\n"
             << UNRED;
        return;
    }
    // if not
    else
    {
        // output the message and continue execution
        cout << GRAY << endl
             << engineersVector[number]->getFullName() << "is now being edited\n\n"
             << UNGRAY;
    }

    // output local menu to user
    cout << BOLD << "What property would you like to edit?\n"
         << UNGRAY;
    cout << "1. Full Name\n";
    cout << "2. Gender\n";
    cout << "3. University Name\n";
    cout << "4. Specialty Name\n";
    cout << "5. Diploma Type\n";
    cout << "6. Study Type\n";
    cout << "7. Work Place\n";
    cout << "8. Retrainings\n";
    cout << "9. Salary\n";
    cout << "10. Birth Year\n";
    cout << "11. Graduation Year\n";
    // ask user to make a choice from the menu options
    cout << "Enter: ";
    ll choice = getNum();
    cout << endl;

    // below process the different choices
    if (choice == 1)
    {
        // ask user to enter the new full name
        cin.ignore();
        string newName;
        cout << "Enter new name: ";
        getline(cin, newName);
        // and validate it
        newName = validateName(newName);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getFullName() << "is now " << newName << endl
             << UNGREEN;
        engineersVector[number]->setFullName(newName);
    }
    else if (choice == 2)
    {
        // ask user to enter the new gender
        char newGender;
        cout << "Enter new gender (M | F): ";
        cin >> newGender;

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getGender() << "is now " << newGender << endl
             << UNGREEN;
        engineersVector[number]->setGender(newGender);
    }
    else if (choice == 3)
    {
        // ask user to enter the new university name
        cin.ignore();
        string newUniversityName;
        cout << "Enter new university name: ";
        getline(cin, newUniversityName);
        // and validate it
        newUniversityName = validateName(newUniversityName);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getUniversityName() << "is now " << newUniversityName << endl
             << UNGREEN;
        engineersVector[number]->setUniversityName(newUniversityName);
    }
    else if (choice == 4)
    {
        // ask user to enter the new specialty name
        cin.ignore();
        string newSpecialtyName;
        cout << "Enter new specialty name: ";
        getline(cin, newSpecialtyName);
        // and validate it
        newSpecialtyName = validateName(newSpecialtyName);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getSpecialty() << "is now " << newSpecialtyName << endl
             << UNGREEN;
        engineersVector[number]->setSpecialty(newSpecialtyName);
    }
    else if (choice == 5)
    {
        // ask user to enter the new diploma type
        cin.ignore();
        string newDiplomaType;
        cout << "Enter new diploma type (Bachelor | Master): ";
        getline(cin, newDiplomaType);
        // and validate it
        newDiplomaType = validateName(newDiplomaType);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getDiploma() << "is now " << newDiplomaType << endl
             << UNGREEN;
        engineersVector[number]->setDiploma(newDiplomaType);
    }
    else if (choice == 6)
    {
        // ask user to enter the new study type
        cin.ignore();
        string newStudyType;
        cout << "Enter new study type (Full-Time | Part-Time): ";
        getline(cin, newStudyType);
        // and validate it
        newStudyType = validateName(newStudyType);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getStudyType() << "is now " << newStudyType << endl
             << UNGREEN;
        engineersVector[number]->setStudyType(newStudyType);
    }
    else if (choice == 7)
    {
        // ask user to enter the new work place
        cin.ignore();
        string newWorkPlace;
        cout << "Enter new work place: ";
        getline(cin, newWorkPlace);
        // and validate it
        newWorkPlace = validateName(newWorkPlace);

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getSpecialty() << "is now " << newWorkPlace << endl
             << UNGREEN;
        engineersVector[number]->setSpecialty(newWorkPlace);
    }
    else if (choice == 8)
    {
        // ask user to enter the amount of new retrainings
        vector<string> newRetrainingsHolder;
        cout << "Enter the amount of new retrainings: ";
        ll retrainingsAmount = getNum();
        cin.ignore();

        // for the specified amount of retrainings
        for (ll k = 0; k < retrainingsAmount; k++)
        {
            // ask user to enter the new retrainings one by one
            string retrainingHolder;
            cout << "• ";
            getline(cin, retrainingHolder);
            // validate them and add to the vector
            retrainingHolder = validateName(retrainingHolder);
            newRetrainingsHolder.eb(retrainingHolder);
        }

        // output the success message and change the property
        cout << GREEN << "Retrainings successfully updated\n"
             << UNGREEN;
        engineersVector[number]->setRetrainings(newRetrainingsHolder);
    }
    else if (choice == 9)
    {
        // ask user to enter the new salary
        cout << "Enter new salary: $";
        ll newSalary = getNum();

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getSalary() << "is now " << newSalary << endl
             << UNGREEN;
        engineersVector[number]->setSalary(newSalary);
    }
    else if (choice == 10)
    {
        // ask user to enter the new birth year
        cout << "Enter new birth year: ";
        ll newBirthYear = getNum();

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getBirthYear() << "is now " << newBirthYear << endl
             << UNGREEN;
        engineersVector[number]->setBirthYear(newBirthYear);
    }
    else if (choice == 11)
    {
        // ask user to enter the new graduation year
        cout << "Enter new graduation year: ";
        ll newGradYear = getNum();

        // output the success message and change the property
        cout << GREEN << engineersVector[number]->getGraduationYear() << "is now " << newGradYear << endl
             << UNGREEN;
        engineersVector[number]->setGraduationYear(newGradYear);
    }
    cout << endl;
}

// for showing the main menu of the application
void outputMenu(vector<unique_ptr<Engineer>> &engineersVector)
{
    // output the menu
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Show people\n";
    cout << "2. Add people\n";
    cout << "3. Remove people\n";
    cout << "4. Edit people\n";
    cout << "5. Exit\n";
    // ask user to enter their choice
    cout << "Enter: ";
    // and validate it
    ll userDecision = getNum();
    cout << endl;

    // if user chose to just show people
    if (userDecision == 1)
    {
        showPeople(engineersVector);
    }
    // if user chose to add people to the vector
    else if (userDecision == 2)
    {
        showPeople(engineersVector);
        addPeople(engineersVector);
        showPeople(engineersVector);
    }
    // if user chose to remove people from the vector
    else if (userDecision == 3)
    {
        showPeople(engineersVector);
        removePeople(engineersVector);
        showPeople(engineersVector);
    }
    // if user chose to edit people in the vector
    else if (userDecision == 4)
    {
        showPeople(engineersVector);
        editPeople(engineersVector);
        showPeople(engineersVector);
    }
}
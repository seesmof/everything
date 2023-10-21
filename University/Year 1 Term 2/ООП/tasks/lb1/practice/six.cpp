// include necessary libraries
#include "../../../../lib.h"
using namespace std;

class Employee
{
private:
    string name;
    string company;
    ll age;

public:
    Employee(string name, string company, ll age) : name(name), company(company), age(age) {}

    string getName() const { return name; }
    string getCompany() const { return company; }
    ll getAge() const { return age; }
};

void addEmployees(vector<unique_ptr<Employee>> &employees)
{
    ll userInput;
    cout << "Amount of employees: ";
    cin >> userInput;

    ll subCounter = 1;
    for (ll i = 0; i < userInput; i++)
    {
        string name;
        string company;
        ll age;

        cout << i + 1 << "." << subCounter << ". Name: ";
        cin >> name;
        if (islower(name[0]))
            name[0] = toupper(name[0]);
        subCounter++;

        cout << i + 1 << "." << subCounter << ". Company: ";
        cin >> company;
        if (islower(company[0]))
            company[0] = toupper(company[0]);
        subCounter++;

        cout << i + 1 << "." << subCounter << ". Age: ";
        cin >> age;
        if (cin.fail())
        {
            cout << RED << "\nERROR: Enter an integer...\n\n"
                 << UNRED;
            cin.clear();
            cin.ignore();
            continue;
        }
        else if (age < 18)
        {
            cout << RED << "\nERROR: Age must be greater than 18.\n\n"
                 << UNRED;
            continue;
        }
        subCounter++;

        Employee *employee = new Employee(name, company, age);
        employees.push_back(unique_ptr<Employee>(employee));
        subCounter = 1;
        cout << endl;
    }
}

void deleteEmployees(vector<unique_ptr<Employee>> &employees)
{
    ll numToDelete;
    cout << "Index: ";
    cin >> numToDelete;
    cout << endl;

    auto it = employees.begin() + numToDelete;
    cout << GREEN << employees[numToDelete]->getName() << " successfully deteled\n"
         << UNGREEN;
    employees.erase(it);
}

void outputEmployees(vector<unique_ptr<Employee>> &employees)
{
    ll vectorSize = employees.size();
    ll subCounter = 1;

    cout << BOLD << "Employees (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
    {
        cout << i + 1 << "." << subCounter << ". Name: " << employees[i]->getName() << endl;
        subCounter++;

        cout << i + 1 << "." << subCounter << ". Age: " << employees[i]->getAge() << endl;
        subCounter++;

        cout << i + 1 << "." << subCounter << ". Company: " << employees[i]->getCompany() << endl;
        subCounter++;

        cout << endl;
        subCounter = 1;
    }
}

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    ll userDecision;
    /////////////////////////////

    // project intro
    cout << "\n";
    do
    {
        ///////////////////////////////////////

        // for manipulating program flow
        char doReturnToMenu;
        vector<unique_ptr<Employee>> employees;

        do
        {

            // output menu to user
            cout << BOLD << "Choose an option\n"
                 << UNBOLD;
            cout << "1. Add employees\n";
            cout << "2. Fire employees\n";
            cout << "3. Print employees\n";
            cout << "4. Exit\n";
            cout << "Enter your choice: ";
            cin >> userDecision;
            cout << endl;

            // anticipate different menu options
            if (userDecision == 1)
            {
                addEmployees(employees);
                outputEmployees(employees);
            }
            else if (userDecision == 2)
            {
                outputEmployees(employees);
                deleteEmployees(employees);
            }
            else if (userDecision == 3)
            {
                outputEmployees(employees);
            }

            // ask user if they would like to return to menu
            cout << "\nWould you like to return to menu? (Y | N): ";
            cin >> doReturnToMenu;
            // if so, continue loop execution
            if (doReturnToMenu == 'Y' || doReturnToMenu == 'y')
            {
                cout << endl
                     << endl;
                continue;
            }
            // if not, break out of loop
            else
                break;

        } while (doReturnToMenu == 'y' || doReturnToMenu == 'Y');
        // execute while user chooses to return to menu

        ///////////////////////////////////////

        // ask user if they would like to continue execution of program
        cout << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // stop main function execution
    cout << "\nThanks for using this program\n\n";
    return 0;
}
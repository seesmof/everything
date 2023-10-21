#include "D:\repos\university\lib.h"
#include "sup.h"

// Створити клас Delta таким чином, щоб кожний об’єкт вміщував свій персональний номер (дескриптор об’єкта) та функцію, яка повертає його значення. Дескриптор об’єкта – унікальне для об’єктів даного типу ціле число.
// Виконати завдання з лабораторної роботи №1, де тип елементу заданої структури даних довільний. Використати шаблонні функції.

int main()
{
    srand(time(NULL));
    char doContinue;
    char doReturnToMenu;

    cout << "\n";
    do
    {
        ///////////////////////////////////////

        vector<string> menuItems = {
            "Integer",
            "Double",
            "String",
            "Exit"};
        ll userDecision = showMenu(menuItems);

        if (userDecision == 1)
        {
            vector<unique_ptr<Delta<int>>> deltaObjectsVector;
            outputMenu(deltaObjectsVector);
        }
        else if (userDecision == 2)
        {
            vector<unique_ptr<Delta<double>>> deltaObjectsVector;
            outputMenu(deltaObjectsVector);
        }
        else if (userDecision == 3)
        {
            vector<unique_ptr<Delta<string>>> deltaObjectsVector;
            outputMenu(deltaObjectsVector);
        }
        else if (userDecision == 4)
        {
            vector<unique_ptr<Delta<>>> deltaObjectsVector;
            outputMenu(deltaObjectsVector);
        }

        ///////////////////////////////////////

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

    cout << "\nThanks for using this program\n\n";
    return 0;
}
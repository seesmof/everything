#include "D:\repos\university\lib.h"
#include "sup.h"

// Виконати завдання з лабораторної роботи #1 використавши, для зберігання даних класи Standard Template Library (STL) або list або vector. Поясніть різницю в використанні цих класів.

int main()
{
    srand(time(NULL));
    char doContinue;
    char doReturnToMenu;

    vector<unique_ptr<Delta>> container;
    list<unique_ptr<Delta>> container_list;

    cout << "\n";
    vector<string> menuItems = {
        "Vector",
        "List",
        "Exit"};
    ll userDecision = showMenu(menuItems);
    do
    {
        do
        {
            ///////////////////////////////////////

            if (userDecision == 1)
            {
                outputMenu(container);
            }
            else if (userDecision == 2)
            {
                outputMenu(container_list);
            }

            ///////////////////////////////////////

            cout << "\nWould you like to return to menu? (Y | N): ";
            cin >> doReturnToMenu;
            if (doReturnToMenu == 'Y' || doReturnToMenu == 'y')
            {
                cout << endl
                     << endl;
                continue;
            }
            else
                break;

        } while (doReturnToMenu == 'y' || doReturnToMenu == 'Y');

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
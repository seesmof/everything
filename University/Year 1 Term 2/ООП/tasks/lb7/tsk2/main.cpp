#include "D:\repos\university\lib.h"
#include "sup.h"
using namespace std;

// Виконати завдання з лабораторної роботи #5 з довільним типом даних

int main()
{
    srand(time(NULL));
    char doContinue;
    vector<unique_ptr<DynamicString>> container;
    char doReturnToMenu;

    cout << "\n";
    do
    {
        ///////////////////////////////////////

        do
        {
            outputMenu(container);

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
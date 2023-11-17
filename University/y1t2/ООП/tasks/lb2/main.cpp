// include necessary libraries
#include "../../../lib.h"
#include "sup.h"
using namespace std;

// Створити динамічний клас Route на основі двозв’язного списку, де кожний елемент типа Stop (зупинка). Клас повинен містити наступні операції:
// add_stop() – додавання зупинки;
// len_route() – розрахунок довжини маршруту;
// time_route() – розрахувати час руху.

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    /////////////////////////////

    // project intro
    cout << "\n";
    do
    {
        ///////////////////////////////////////

        // for storing class object pointers
        Route routeContainer;
        // for manipulating program flow
        char doReturnToMenu;

        do
        {
            // output menu to user
            outputMenu(routeContainer);

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
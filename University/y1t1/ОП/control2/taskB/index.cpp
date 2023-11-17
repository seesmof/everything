// include necessary libraries
#include <bits/stdc++.h>
#include "supplementary.h"
#include "menu.h"
using namespace std;

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    vector<Letter> lettersVector;
    string inFileName;
    string inEmailAddress;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task B\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // take email address and input file from user
        cout << BOLD << "Before we begin, let us take some important steps\n\n"
             << UNBOLD;
        inEmailAddress = getEmailAddress();
        inFileName = getFileName();
        fillVector(lettersVector, inFileName); // fill in the vector of struct using a corresponding function

        do
        {
            // output a menu
            outputMenu(lettersVector, inEmailAddress);

            // after user have worked in a menu and returned here, ask them to continue or not
            cout << BOLD << "\nWould you like to return to menu? (Y / N): " << UNBOLD;
            cin >> doContinue;

            if (doContinue == 'Y' || doContinue == 'y')
                continue;
            else
                break;

            // execute while the answer is yes
        } while (doContinue == 'Y' || doContinue == 'y');

        //////////////////////////////////////////////////////////////////////////////////
        cout << "\n/////////////////////////////////////////////////////////////\n"
             << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n/////////////////////////////////////////////////////////////\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // func main end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
}
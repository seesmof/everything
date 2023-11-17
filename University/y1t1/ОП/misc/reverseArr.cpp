// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// create a function that will reverse the given array and output the result
void reverseArray(vector<int> &x, int n)
{
    // create an array to hold the result
    vector<int> reversed(n);
    // declare counter
    int j = 0;
    // create a for loop for reverse
    for (int k = n - 1; k >= 0; k--)
    {
        // reverse the array
        reversed[j] = x[k];
        // output the result
        cout << reversed[j] << " ";
        // increment counter
        j++;
    }
    // end function
    return;
}

// declare main function
int main()
{
    char doContinue;
    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will reverse an array for you." << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    do
    {
        // declare variable for holding array size;
        int n;
        // ask user to input array size
        cout << "Enter array size: ";
        cin >> n;
        // declare input array
        vector<int> x(n);
        // ask a user to choose whether to generate or enter the array
        int choice;
        cout << "Would you like to enter the array yourself or let it be generated?" << endl;
        cout << "1 to enter | 2 to generate |: ";
        cin >> choice;
        // if enter is chosen => execute the following statement
        if (choice == 1)
        {
            // let user enter each array element
            for (int j = 0; j < n; j++)
            {
                cout << "Enter an element: ";
                cin >> x[j];
            }
        }
        // if generate or else are chosen => execute the following statement
        else
        {
            // generate the array
            for (int j = 0; j < n; j++)
                x[j] = rand() % 10;
        }
        // output the array
        cout << endl
             << "Initial array is: ";
        for (int j = 0; j < n; j++)
            cout << x[j] << " ";

        // reverse an array using a user-defined function
        cout << endl
             << "Your result is: ";
        //  call a function
        reverseArray(x, n);

        cout << endl
             << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'N' || doContinue == 'n')
        {
            cout << endl
                 << "Thanks for using this program." << endl
                 << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            break;
        }
        else
        {
            cout << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            continue;
        }
    } while (doContinue = 'Y' || doContinue == 'y');

    // end main function
    return 0;
}
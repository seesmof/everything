// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare main function
int main()
{
    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will output a string word by word" << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    char doContinue;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        long double sum = 0.0;
        long long int d1 = 5, d2 = 8, d3 = 11, n;

        cout << "Enter N: ";
        cin >> n;
        cout << endl;

        int choice;
        cout << "Would you like to perform multiple operations or just one?" << endl;
        cout << "1 for multiple | 2 for one |: ";
        cin >> choice;

        if (choice == 1)
        {
            for (int i = 1; i <= n; i++)
            {
                while (d1 <= (2 + 3 * i) && d2 <= (5 + 3 * i) && d3 <= (8 + 3 * i))
                {
                    cout << endl
                         << 1 << " / (" << d1 << " * " << d2 << " * " << d3 << ")" << endl;
                    sum += (1.0 / (d1 * d2 * d3));

                    d1 += 3;
                    d2 += 3;
                    d3 += 3;
                }

                cout << "With N " << i << ": " << setprecision(200) << sum << endl;
            }
        }
        else
        {
            while (d1 <= (2 + 3 * n) && d2 <= (5 + 3 * n) && d3 <= (8 + 3 * n))
            {
                sum += (1.0 / (d1 * d2 * d3));

                d1 += 3;
                d2 += 3;
                d3 += 3;
            }

            cout << "With N " << n << ": " << setprecision(200) << sum << endl;
        }
        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        cin.ignore();
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
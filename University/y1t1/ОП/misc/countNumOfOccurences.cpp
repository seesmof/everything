// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
void countNumOfOccurences(int, vector<int> &);
/////////////////////////

// declare main function
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    /////////////////////////////

    // project intro
    cout << endl
         << "////////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will count number of occurences in arrray" << endl
         << endl
         << "////////////////////////////////////////////////////////////////" << endl
         << endl;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        int n;
        cout << "Enter the amount of elements in array: ";
        cin >> n;
        vector<int> arr(n);

        cout << endl;
        cout << "Would you like to generate or enter an array?" << endl;
        cout << "1 to generate | 2 to enter |: ";
        cin >> userDecision;

        if (userDecision == 1)
        {
            cout << endl;
            for (int i = 0; i < n; i++)
                arr[i] = rand() % 10;

            cout << "Array successfully generated" << endl;
        }
        else
        {
            cout << endl;
            for (int i = 0; i < n; i++)
            {
                cout << "#" << i + 1 << ": ";
                cin >> arr[i];
            }
        }

        cout << endl;
        for (int i = 0; i < n; i++)
        {
            if (i == 0)
                cout << arr[i];
            else
                cout << setw(3) << arr[i];
        }

        cout << endl
             << endl;
        countNumOfOccurences(n, arr);
        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
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

void countNumOfOccurences(int n, vector<int> &a)
{
    sort(a.begin(), a.end());
    for (int i = 0; i < n; i++)
    {
        int c = 0;
        if (a[i] == a[i - 1])
            continue;
        for (int j = 0; j < n; j++)
            if (a[i] == a[j])
                c++;
        cout << a[i] << " occured " << c << " times" << endl;
    }
    return;
}
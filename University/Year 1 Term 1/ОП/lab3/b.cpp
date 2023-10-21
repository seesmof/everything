// include necessary libraries
#include <iostream>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "************************* Task B ********************************" << endl
         << endl;

    // ask user to input array size
    int n, m;
    cout << "Enter the size of an array (n * m): ";
    cin >> n >> m;
    int arr[n][m];
    cout << endl;

    // create function for elements input
    for (int i = 0, count = 0; i < n; i++)
    {
        for (int j = 0, n = 1; j < m; j++, n++)
        {
            // ask user to input a value
            cout << "Enter a value: ";
            cin >> arr[i][j];
            if (arr[i][j] > 0) // if value is positive, output error and continue
            {
                cout << "Value should be negative only" << endl;
                continue;
            } // if element before is bigger, add to counter
            if (arr[i][j] > arr[i][j - n])
            {
                count++;
            }
            // output the number of elements that are less than input
            cout << "Number of elements that are less than input is " << count << endl;
        }
    }

    // output an array to the user
    cout << endl;
    cout << "Your array is: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    // output program outro
    cout << endl;
    cout << "*****************************************************************" << endl;

    // end main function
    return 0;
}
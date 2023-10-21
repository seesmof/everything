// include necessary libraries
#include <iostream>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "************************* Task C ********************************" << endl
         << endl;

    // ask user to input array size
    int n, m;
    cout << "Enter the size of an array (n * m): ";
    cin >> n >> m;
    int arr[n][m];
    cout << endl;
    srand(time(NULL));

    // create function to fill in the array and calculate a number of odd elements in each row
    for (int i = 0, count = 0; i < n; i++)
    {
        count = 0; // reset counter on each row
        for (int j = 0, n = 1; j < m; j++, n++)
        {
            arr[i][j] = rand() % 10;
            if (arr[i][j] % 3 == 0) // if element can be divided by 3 with no remainder => count it as odd
            {
                count++;
            }
        }
        // output number of odd elements
        cout << "Number of odd elements in a row is " << count << endl;
    }

    // output program outro
    cout << endl;
    cout << "*****************************************************************" << endl;

    // end main function
    return 0;
}
// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    srand(time(NULL));
    // declare variable for storing array size and ask user to input it
    int n;
    cout << "Enter matrix size N: ";
    cin >> n;

    // declare a vector for storing minimum values
    vector<int> localArr(n);
    // declare an array of pointers for storing array values
    int **arr = new int *[n];

    // create a function for creating columns for each row
    for (int i = 0; i < n; i++)
        arr[i] = new int[n];

    // create a function that will ask user to input each element of the array
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // cout << "Enter matrix element: ";
            // cin >> arr[i][j];

            arr[i][j] = rand() % 10;
        }
    }

    // create a function that will output the matrix
    cout << endl;
    cout << "Your matrix is " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // if outputs the first column => output without spaces in front
            if (j == 0)
            {
                cout << arr[i][j];
            }
            // in any other cases, output with 3 spaces in front
            else
            {
                cout << setw(4) << arr[i][j];
            }
        }
        cout << endl;
    }

    // declare a local maximums counter
    int localMaximumCount = 0;
    int k = 0;

    // create a function that will loop through the whole array and look for the local maximums
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // create a case for top left corner of the array
            if (i == 0 && j == 0)
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i + 1][j + 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for top right corner
            else if (i == 0 && j == n - 1)
            {
                if (arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i + 1][j - 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for bottom left corner
            else if (i == n - 1 && j == 0)
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i - 1][j + 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for bottom right corner
            else if (i == n - 1 && j == n - 1)
            {
                if (arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i - 1][j - 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for elements on the top edge of the array
            else if (i == 0)
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i + 1][j - 1] && arr[i][j] > arr[i + 1][j + 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for elements on the left edge of the array
            else if (j == 0)
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i + 1][j + 1] && arr[i][j] > arr[i - 1][j + 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for elements on the bottom edge of the array
            else if (i == n - 1)
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i - 1][j + 1] && arr[i][j] > arr[i - 1][j - 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for elements on the right edge of the array
            else if (j == n - 1)
            {
                if (arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i - 1][j + 1] && arr[i][j] > arr[i + 1][j - 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
            // create a case for elements in the middle of the array
            else
            {
                if (arr[i][j] > arr[i][j + 1] && arr[i][j] > arr[i][j - 1] && arr[i][j] > arr[i + 1][j] && arr[i][j] > arr[i - 1][j] && arr[i][j] > arr[i - 1][j + 1] && arr[i][j] > arr[i - 1][j - 1] && arr[i][j] > arr[i + 1][j + 1] && arr[i][j] > arr[i + 1][j - 1])
                {
                    // if all conditions are met => increase a local maximum counter and add this element to local maximums array
                    localMaximumCount++;
                    localArr[k] = arr[i][j];
                    k++;
                }
            }
        }
    }

    // declare a fariable for storing the minimum value of all the local maximums and assign it a value of the first element of local maximums array
    int minFromLocalMax = localArr[0];
    for (int i = 0; i < k; i++)
    {
        // if current element is less than the minimum => assign it to the minFromLocalMax var
        if (localArr[i] < minFromLocalMax)
        {
            minFromLocalMax = localArr[i];
        }
    }

    // output results to the user
    cout << endl;
    cout << "The number of local maximums in this matrix is " << localMaximumCount << endl;
    cout << "The least value of those local maximums is " << minFromLocalMax << endl;

    // clear memroy buffer from dynamic array
    for (int i = 0; i < n; i++)
        delete[] arr[i];

    delete[] arr;
    arr = NULL;

    // output project outro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // end main function
    return 0;
}
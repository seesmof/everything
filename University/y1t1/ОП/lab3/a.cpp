// include necessary libraries
#include <iostream>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task A *************************************" << endl
         << endl;

    // ask user to enter the size of an array
    int n;
    cout << "Enter the amount of elements you want in array: ";
    cin >> n;
    int *arr = new int(n); // create new array
    srand(time(NULL));

    // output randomly generated array
    cout << "You array is: ";
    for (int i = 0; i < n; i++)
    {
        arr[i] = rand() % 10;
        cout << arr[i] << " ";
    }
    cout << endl
         << endl;

    // create a loop for checking if two numbers dont monotonically increase
    for (int i = 0; i < n; i++)
    {
        int count = 0;
        if (arr[i] == arr[i + 1]) // if number 1 equals to next number, execute the function below
        {
            count++;
            cout << "Sequence that contains numbers that don't monotonically increase: ";
            for (int k = 0; k <= count; k++) // output the number as many times as it repeats in an array
            {
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl;

    // end main function
    delete[] arr;
    arr = NULL;
    return 0;
}

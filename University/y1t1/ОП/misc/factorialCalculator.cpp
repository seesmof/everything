// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare main function
int main()
{
    // declare a variable for holding user inputed number
    int num;

    // ask user to input the number
    cout << "Enter the number you want a factorial of: ";
    cin >> num;

    // declare a variable for holding the result of the factorial
    double factorial = 1;

    // create for loop for calculating the factorial
    for (int i = 1; i <= num; i++)
    {
        factorial = factorial * i;
    }

    // output the factorial of the number
    cout << num << "! is " << factorial << endl;

    // end of main function
    return 0;
}
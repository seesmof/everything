// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// delcare main function
int main()
{
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // declare a variable for storing the user input
    int n;
    // welcome the user and tell them what the program does
    cout << endl
         << "Welcome! This program will tell you all the divisors of a given number." << endl
         << endl;
    //  ask user to input a number
    cout << "Enter: ";
    cin >> n;

    // create a vector for storing all the divisors
    vector<int> divisors;
    // push back 1 and the number itself
    divisors.push_back(1);
    divisors.push_back(n);

    // for numbers up to n / 2
    for (int d = 2; d <= (n / 2); d++)
    {
        // if the number of given iteration can be divided by the input
        if (n % d == 0)
        {
            // add it to the vector
            divisors.push_back(d);
        }
    }
    // sort the vector in the ascending order
    sort(divisors.begin(), divisors.end());

    // output the result to user
    cout << endl
         << "The divisors of " << n << " are: ";
    for (int i = 0; i < divisors.size(); i++)
        cout << divisors[i] << " ";
    cout << endl;

    // end main function
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    return 0;
}
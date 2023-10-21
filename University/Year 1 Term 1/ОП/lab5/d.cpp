// include necessary libraries
#include <iostream>
using namespace std;

// declare function prototype
double rec(int);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << "****************************** Task D *************************************" << endl
          << endl;

     // declare variable for storing N number
     int n;
     // ask user to enter N number
     cout << "Enter N: ";
     cin >> n;
     cout << endl;

     // create a function that will determine the correctness of the hypothesis by comparing the function output with the valeu given in a task description
     if (rec(n) == n / (n + 1))
     {
          // if comparison is correct => output correct message
          cout << "The hypothesis with given number is correct!" << endl;
     }
     else
     {
          // else output error message
          cout << "The hypothesis with given number is not correct." << endl;
     }

     // output project outro
     cout << endl
          << "***************************************************************************" << endl;

     // end main function
     return 0;
}

// create recursive function for determining whether the hypothesis is correct
double rec(int n)
{
     // add base point when n = 1
     if (n == 1)
     {
          // return base value
          return 1 / (1 * 2);
     }
     // else return last value + recall the function with n-1 as a value
     else
     {
          return 1 / (n * (n + 1)) + rec(n - 1);
     }
}
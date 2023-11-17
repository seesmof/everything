// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare function prototype
double sum(int, int);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << "****************************** Task A *************************************" << endl
          << endl;

     // create two necessary variables
     int x, n;

     // ask user to enter those two variables
     cout << "Enter number X: ";
     cin >> x;
     cout << "Enter number N: ";
     cin >> n;

     // output the result by using the earlier declared function
     cout << endl
          << "The result is " << sum(x, n) << endl;

     // output project outro
     cout << endl
          << "***************************************************************************" << endl;

     // end main function execution
     return 0;
}

// create function for calculating the sum
double sum(int x, int n)
{
     // declare local variables that will store values needed for calculation
     int numPow = 2, denomOne = 0, denomTwo = 1, denomThree = 2;
     double sum = 0.0;

     // execute while the values of denomOne, denomTwo and denomThree are less than specified ones
     do
     {
          // execute the formula
          sum += (pow(x, numPow)) / (denomOne + denomTwo * pow(denomThree, 2));

          // add increments
          numPow += 1;
          denomOne += 1;
          denomTwo += 1;
          denomThree += 1;
     } while (denomOne < (n - 1) && denomTwo < n && denomThree < (n + 1));

     // end function execution
     return sum;
}
// include necessary libraries
#include <iostream>
using namespace std;

// declare function prototype for finding Least Common Multiple
int findLCM(int, int);

// declare function prototype for finding Greatest Common Multiple
int findGCD(int, int);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << endl
          << "****************************** Task B *************************************" << endl
          << endl;

     // declare two number variables that we will be working with
     int m, n;

     // ask user to enter those two numbers
     cout << "Enter two numbers (N M): ";
     cin >> n >> m;

     // declare a local variable for storing the result of findLeastCommonMultiple function
     int LCM = findLCM(n, m);

     // output the Least Common Multiple to user
     cout << endl
          << "Least Common Multiple of " << n << " and " << m << " is " << LCM << endl;

     // output the result of dividing Least Common Multiple by each number
     cout << "LCM"
          << " / " << n << " = " << LCM / n << endl;
     cout << "LCM"
          << " / " << m << " = " << LCM / m << endl;

     // output project outro
     cout << endl
          << "***************************************************************************" << endl;

     // end main function
     return 0;
}

// create a recursive function that will calculate the Greatest Common Divisor (GCD)
int findGCD(int a, int b)
{
     // if the remainder of division is 0 => return second number
     if (a == 0)
          return b;
     // else return function with b % a and a as arguments
     return findGCD(b % a, a);
}

// create a function that will calculate the Least Common Multiple knowing that n(m) = GCD(n, m) * LCM(n, m)
int findLCM(int x, int y)
{
     // declare productOfTwoNums variable that will multiply two given numbers
     int productOfTwoNums = x * y;
     // declare output variable that will divide the product by LCD, thus finding the LCM
     int LCM = productOfTwoNums / findGCD(x, y);
     // return output variable, end function
     return LCM;
}
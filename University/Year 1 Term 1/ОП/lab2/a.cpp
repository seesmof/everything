// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // declare variables
    int A, B, i;

    // ask user to input A to B interval
    cout << "Please enter the beginning of interval: ";
    cin >> A;
    cout << "Please enter the end of interval: ";
    cin >> B;

    // create a for loop for going through interval and counting divisors
    for (A; A <= B; A++)
    {
        // set i to 2 by default because it is a minimum number of divisors a number has: 5 can only be divided by 1 and itself = 5, etc.
        i = 2;
        // create for loop for counting divisors
        for (int d = 2; d <= (A / 2); d++)
        {
            // if in result of division we get 0, it means this is a correct divisor
            if (A % d == 0)
            {
                // if divisors are equal then count only one of them
                if (A / d == d)
                {
                    i++;
                }
                // otherwise count both of them
                else
                {
                    i = i + 2;
                }
            }
        }
        // if the number of divisors equals to 5, that is what we need
        if (i == 5)
        {
            cout << A << " has 5 divisors" << endl;
        }
    }

    // end main function
    system("pause");
}
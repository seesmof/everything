// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // declare variables
    double sum = 0.0, x, s;
    int p = 0, f = 1, n, nf;

    // ask user to input number of times he wants a program to run
    cout << "Enter number of times you want a program to run: ";
    cin >> n;

    // ask user to input number X
    cout << "Enter number X: ";
    cin >> x;

    // create for loop for calculating the sum
    for (int i = 1; i <= n; i++)
    {
        // create a step
        s = pow(x, p) / f;

        // create a for loop for calculating factorial
        for (int j = 1; j <= nf; j++)
        {
            f = f * nf;
        }

        // add increments
        p++;
        nf += 2;
        sum += s;
    }

    // output result
    cout << "The sum is " << sum << endl;

    // end main function
    system("pause");
}

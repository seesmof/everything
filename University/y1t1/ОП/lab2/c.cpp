// include necessary libraries
#include <iostream>
#include <math.h>
using namespace std;

// start main function
int main(int argc, char **argv)
{
    // declare input variables
    int m, n;
    // ask user to input two numbers
    cout << "Please enter number one: ";
    cin >> n;
    cout << "Please enter number two: ";
    cin >> m;

    // declare loop variables
    double minInput = min(m, n), maxInput = max(m, n);
    double min = minInput, max = maxInput, sum = 0, s = 0;
    // create for loop for calculating the sum
    for (int i = 0; i <= (m - 1); i++)
    {
        // create for loop for calculating min and max
        for (int j = 1; j <= n; j++)
        {
            s = (i * n) + j;
            if (s > max)
            {
                max = s;
            }
            if (s < min)
            {
                min = s;
            }
        }
        sum += max / min; // adding values to the final sum
    }
    // output result
    cout << "Your sum is " << sum << endl;

    // end main function
    system("pause");
}
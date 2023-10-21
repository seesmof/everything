#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

int main(int argc, char **argv)
{
    double x, z, f;
    const double pi = atan(1) * 4;
    z = pow(asin(x), 3);

    cout << "Enter X: " << endl;
    cin >> x;

    if (z > -0.5)
    {
        f = pow((2 * z + 1), 2) / 2.75 - pow(2, x);
    }
    else if (z >= -0.5 && z <= 0.001)
    {
        f = pow(sin(z), 3) - sin(z / 3 * pi);
    }
    else if (z > 0.001)
    {
        f = (tan(z + x) - exp(x)) / (3.5 * x);
    }

    cout << "The result is: " << f << endl;

    return 0;
} // 1.3.2.22 г)
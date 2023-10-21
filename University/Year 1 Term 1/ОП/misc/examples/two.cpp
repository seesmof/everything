#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    double m, n, res = 0.0;

    for (m = 1; m <= 10; m++)
    {
        cout << "m = " << m << endl;
        for (n = 1; n <= m; n++)
        {
            res += (1 / ((2 * n) + (3 * m)));
        cout << "n = " << n << ", ";
        }
        cout << endl << endl;
    }
    cout << "Res = " << res << endl;

    return 0;
}
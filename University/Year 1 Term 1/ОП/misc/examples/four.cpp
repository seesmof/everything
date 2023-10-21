#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    float e, x;
    float res = 0;
    int step = 2;
    float fact = 1;

    do
    {
        cout << "Enter X: ";
        cin >> x;
        if (x > 1 || x < -1)
        {
            cout << "Invalid." << endl;
        }
    } while (x > 1 || x < -1);
    cout << "Enter E: ";
    cin >> e;
    while (e > res)
    {
        for (int j = 1; j <= step; j++)
        {
            fact *= j;
        }
        res += (pow(x, step) / fact);
        step += 2;
    }
    cout << "Result = " << res << endl;
}
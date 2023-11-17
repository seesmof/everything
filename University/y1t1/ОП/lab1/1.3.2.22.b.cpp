#include <string.h>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int x, y;

    cout << "Enter X value: " << endl;
    cin >> x;
    cout << "Enter Y value: " << endl;
    cin >> y;

    if (x >= y)
    {
        cout << x - y << endl;
    }
    else if (x <= y)
    {
        cout << y - x << endl;
    }
    else
    {
        cout << "Invalid values entered!" << endl;
    }

    return 0;
}
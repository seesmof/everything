#include "D:\repos\university\lib.h"

template <typename T1, typename T2>
T1 _max(T1 a, T2 b)
{
    return a > b ? a : b;
}

int main()
{
    ll a, b;
    cin >> a >> b;
    cout << _max(a, b);
    double c, d;
    cin >> c >> d;
    cout << _max(c, d);
}
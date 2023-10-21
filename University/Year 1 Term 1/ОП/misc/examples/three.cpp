#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int num;
    double neg = 0.0, pos = 0.0, in;

    cout << "Enter number of numbers: " << endl;
    cin >> num;

    for (int i = 0; i < num; i++)
    {
        cout << "Enter number of whatever: " << endl;
        cin >> in;
        if (in < 0.0)
        {
            neg++;
        }
        else
        {
            pos++;
        }
    }
    if (neg > pos)
    {
        cout << "More positives" << endl;
    }
    else if (neg < pos)
    {
        cout << "More negatives" << endl;
    }
    else
    {
        cout << "They're equal" << endl;
    }

    return 0;
}
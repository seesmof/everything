#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int input, result;

    cout << "Enter the day number: " << endl;
    cin >> input;

    if (input > 366)
    {
        cout << "Please enter a correct number" << endl;
    }
    else
    {
        result = input % 7;
        switch (result)
        {
        case 1:
            cout << "Tuesday" << endl;
            break;
        case 2:
            cout << "Wednesday" << endl;
            break;
        case 3:
            cout << "Thursday" << endl;
            break;
        case 4:
            cout << "Friday" << endl;
            break;
        case 5:
            cout << "Saturday" << endl;
            break;
        case 6:
            cout << "Sunday" << endl;
            break;
        case 0:
            cout << "Monday" << endl;
            break;
        }
    }

    return 0;
} // 1.3.2.22 в)
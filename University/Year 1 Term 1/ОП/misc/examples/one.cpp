#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int students;
    double male = 0.0, fem = 0.0, out, in;

    cout << "Enter students count in a group: " << endl;
    cin >> students;

    for (int i = 0; i < students; i++)
    {
        cout << "Enter student height: " << endl;
        cin >> in;
        if (in < 0)
        {
            male += in;
        }
        else
        {
            fem += in;
        }
    }
    out = fem - (-male);
    cout << "Average height is " << out << endl;

    return 0;
}
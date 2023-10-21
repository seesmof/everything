// include necessary libraries
#include <iostream>
#include <iomanip>
#include <string.h>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task A *************************************" << endl
         << endl;

    // declare two strings - input and output
    string input, output;
    int j = 0;

    // ask user to enter an input string
    cout << "Enter a string: ";
    getline(cin, input);

    // create a function that will double any non asterisk characters
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] != '*')
        {
            output.push_back(input[i]);
            output.push_back(input[i]);
            j++;
        }
    }

    // create a function that will output the final string
    cout << endl;
    cout << "The result is: " << endl;
    for (int i = 0; i < output.length(); i++)
    {
        cout << setw(2) << output[i];
    }
    cout << endl;

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl;

    // end main function
    return 0;
}
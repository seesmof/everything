// include necessary libraries
#include <iostream>
#include <string.h>
using namespace std;

// declare global variable
char input[1024];

// declare function for ++ replacement
void plusReplacer();

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task B *************************************" << endl
         << endl;

    // ask user to enter a string
    cout << "Enter a string: ";
    cin.getline(input, sizeof(input));

    // call a function for ++ replacement
    plusReplacer();

    // output a resulting string
    cout << endl;
    cout << "Your final string is: " << input << endl;

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl;

    // end main function
    return 0;
}

// write a function below for better readability
void plusReplacer()
{
    // create a for loop that will loop through the whole string and look for ++ combination
    for (int i = 0, size = strlen(input); i < size; i++)
    {
        // when it finds the combination, it just replaces a second plus with a 1
        if (input[i] == '+' && input[i + 1] == '+')
        {
            input[i + 1] = '1';
        }
    }
}

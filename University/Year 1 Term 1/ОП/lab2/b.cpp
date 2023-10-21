// include necessary libraries
#include <iostream>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // declare variable for storing user input
    int input, result;

    // add note for user to input 0 for program to stop
    cout << "Quick note, enter 0 to stop program execution." << endl;

    // create do while loop for calculating the sum of all inputs
    do
    {
        // ask user to enter input
        cout << "Enter the number: ";
        cin >> input;

        // create condition: if input is more than 0 => continue, otherwise output error
        if (input < 0)
        {
            cout << "Please enter a positive number." << endl;
        }
        else if (input > 0)
        {
            result += input;
        }
    } while (input != 0); // execute loop as long as input is positive

    // output result
    cout << "The sum of all inputs is " << result << endl;

    // end main function
    system("pause");
}
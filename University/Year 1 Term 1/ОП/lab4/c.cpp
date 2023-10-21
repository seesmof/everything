// include necessary libraries
#include <iostream>
#include <string.h>
using namespace std;

// declare global variables
bool isDialogue, isCorrect = false;
char input[1024];

// declare a function for inputting string
void stringInput();

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "****************************** Task C *************************************" << endl
         << endl;

    // call a function for string input
    stringInput();

    // checking a valid sentence for being a part of a dialogue
    // create a for loop for looping through the whole string
    for (int i = 0, size = strlen(input); i < size; i++)
    {
        // if we found a coma, which is usually a part of an appeal, we create a new loop
        if (input[i] == ',')
        {
            // this loop will look for exclemation points
            for (int j = 0; j < size; j++)
            {
                // if it have found one, we change a value of isCorrect to true
                if (input[j] == '!')
                {
                    isCorrect = true;
                }
            }
        }
    }

    // create a condition that depends on the isCorrect value
    if (!isCorrect) // if isCorrect == false, it will output a message saying that this sentence is not a part of the dialogue
    {
        cout << endl;
        cout << "Unfortunately, the inputted sentence is not exclamatory." << endl;
    }
    else // is isCorrect == true, it will output a message saying that this sentence is a part of the dialogue
    {
        cout << endl;
        cout << "Congatuations! The entered sentence is indeed a part of the dialogue!" << endl;
    }

    // output project outro
    cout << endl;
    cout << "***************************************************************************" << endl
         << endl;

    // end main function
    return 0;
}

// write a function at the end for better readability
void stringInput()
{
    // execute as long as user enters not a valid sentence, meaning just one word, with no spaces
    do
    {
        // ask user to enter a sentence
        cout << "Enter a string: ";
        cin.getline(input, sizeof(input));

        // create a for loop for checking input for spaces
        for (int i = 0, size = strlen(input); i < size; i++)
        {
            if (input[i] == ' ')
            {
                isDialogue = true;
            }
        }
        if (!isDialogue) // if user entered one word => output an error message and continue loop execution
        {
            cout << "This doesn't seem to be a dialogue sentence, try again." << endl
                 << endl;
        }
    } while (!isDialogue);
}

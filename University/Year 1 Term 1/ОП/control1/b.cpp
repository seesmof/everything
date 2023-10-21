// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare function prototypes
string doCeasar(int, string);

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // creater necessary variables
    string input;
    int decision;

    do
    {
        // ask user to choose an option he likes
        cout << "Choose the operation type" << endl;
        cout << "1 = encrypt | 2 = decrypt | 3 = exit" << endl;
        cin >> decision;
        cin.ignore(); // clears the buffer

        // if user chose option 1, which is encrypt => execute the following function
        if (decision == 1)
        {
            // ask user to enter the text he wants to encrypt
            cout << endl;
            cout << "Enter your text: ";
            getline(cin, input);

            // declare variable for storing an encryption key and ask user to enter it
            int key;
            cout << "Enter a key: ";
            cin >> key;
            cin.ignore(); // clears the buffer

            // output a result message by calling a function doCeasar with key and input message as arguments
            cout << endl;
            cout << "Your result is: " << doCeasar(key, input) << endl;
        }
        else if (decision == 2)
        {
            // ask user to enter the text he wants to decrypt
            cout << endl;
            cout << "Enter your text: ";
            getline(cin, input);

            // declare variable for storing an encryption key and ask user to enter it
            int key;
            cout << "Enter a key: ";
            cin >> key;
            cin.ignore(); // clears the buffer

            // output a result message by calling a function doCeasar with key and input message as arguments
            cout << endl;
            cout << "Your result is: " << doCeasar((26 - key), input) << endl;
        }

        // ask user whether he wants to continue program execution or not
        cout << endl;
        cout << "Enter 0 to continue program execution" << endl;
        cin >> decision;

        // if 0 was entered => continue program execution
        if (decision == 0)
        {
            cout << endl
                 << endl;
            continue;
        }
        // if anything else was entered => stop program execution
        else
        {
            break;
        }
    } while (decision == 0);

    // output project outro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;

    // end main function
    return 0;
}

// write down a function for text encryption
string doCeasar(int key, string text)
{
    // declare a variable for storing the encrypted message
    string output = "";

    // create a for loop that will loop through the string
    for (int i = 0; i < text.length(); i++)
    {
        // look for uppercase letters by using a function called isupper
        if (isupper(text[i]))
        {
            // if found => execute the (x + n) % 26 formula and add the result to output
            output += char(int(text[i] + key - 65) % 26 + 65);
        }
        // look for lowecase letters by using a function called islower
        else if (islower(text[i]))
        {
            // if found => execute the (x + n) % 26 formula and add the result to output
            output += char(int(text[i] + key - 97) % 26 + 97);
        }
        // for any other characters add them to output
        else
        {
            output += text[i];
        }
    }

    // end function
    return output;
}
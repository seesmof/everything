// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
string fileNameInput();
bool isReadable(const string &);
void cStringFinder(const string &, const string &);
/////////////////////////

// declare main function
int main()
{
    // declare local variables //
    srand(time(NULL));
    char userDecision;
    int randomNumOfLetters = rand() % 10;
    /////////////////////////////

    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will look for string in a file." << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    char doContinue;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        string inputFileName = fileNameInput();

        if (!isReadable(inputFileName))
        {
            cout << "ERROR: Could not read from " << inputFileName << endl;
            break; // break out of loop
        }

        cout << endl;
        string input;
        cout << "Input a text you want to look for: ";
        getline(cin, input);

        cStringFinder(input, inputFileName);
        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'N' || doContinue == 'n')
        {
            cout << endl
                 << "Thanks for using this program." << endl
                 << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            break;
        }
        else
        {
            cout << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            continue;
        }
    } while (doContinue = 'Y' || doContinue == 'y');
    return 0;
}

void cStringFinder(const string &in, const string &iFileName)
{
    // declare local variables
    const int MAX_LINE = 2048; // max number of characters in line
    char bufLine[MAX_LINE];    // buffer to hold current line
    vector<string> lines;      // vector to store all the lines
    int foundOnLine = 0;       // integer to hold line where given substring was found
    FILE *iFile;               // file itself

    // open given file for reading
    iFile = fopen(iFileName.c_str(), "r");

    // add all file lines to string vector using fgets function
    while (fgets(bufLine, MAX_LINE, iFile))
        lines.push_back(bufLine);
    fclose(iFile); // close file
    // number of lines equals to size of string vector
    int numOfLines = lines.size();

    // create for loop to look for string at each line
    for (int i = 0; i < numOfLines; i++)
    {
        // declare variable that will look for in substring in each file line
        size_t find = lines[i].find(in);
        // if found not on end of line
        if (find != string::npos)
        {
            // assign iterator value to variable, declared before
            foundOnLine = i + 1;
            break; // break out of loop
        }
    }

    cout << endl;
    // if string was found
    if (!(foundOnLine == 0))
    {
        // output success message
        cout << "\"" << in << "\" was found on line " << foundOnLine << "." << endl;
        return; // end function
    }
    // if string was not found
    else
    {
        // output error message
        cout << "\"" << in << "\" was never found in " << iFileName << "." << endl;
        return; // end function
    }
}

// create a function that will take file name from user
string fileNameInput()
{
    // declare local variables
    bool isExtensionFound = false;
    string input;

    // ask user to input file name
    cout << "Enter the name of the file: ";
    cin >> input;
    cin.ignore();

    // create for loop to look for extension
    for (int i = 0; i < input.length(); i++)
    {
        // dot is an indication of extension
        if (input[i] == '.')
        {
            // if found then change bool isExtensionFound to true
            isExtensionFound = true;
            break; // break out of loop
        }
    }

    // if the result is not found then
    if (!isExtensionFound)
    {
        // create a new string for holding the file extension
        string fileExtension;

        // ask user to enter a file extension
        cout << "Please specify a file extension: ";
        cin >> fileExtension;
        cin.ignore();

        // create a for loop
        for (int i = 0; i < fileExtension.length(); i++)
        {
            // look for a dot in input
            if (fileExtension[i] == '.')
            {
                // if found then add it to the result string
                input += fileExtension;
                break; // break out of loop
            }
            else
            {
                // if not found then add add a dot + input to the result string
                input += "." + fileExtension;
                break; // break out of loop
            }
        }
    }

    // return the result string
    return input;
}

// declare function to check whether a file is readable
bool isReadable(const string &fileName)
{
    // declare local variables for reading a file
    fstream file(fileName.c_str(), ios::in | ios::out);
    bool ans;

    // if result file is successfully opened
    if (file.good())
        // set answer to true
        ans = true;
    else
        // set answer to false
        ans = false;
    // return answer
    return ans;
}
// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
string randString(int);
string fileNameInput();
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This program will replace a given word in file\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        string inputFileName = fileNameInput(); // ask user to input file name for input file

        // ask user to input a string to look for in a file and replace later
        string toLookFor;
        cout << "\nEnter a string you want to replace: ";
        getline(cin, toLookFor);

        // ask user for a string to replace with
        string replaceWith;
        cout << "Enter a string that will replace the old one: ";
        getline(cin, replaceWith);

        fstream in(inputFileName, ios::in); // declare input file with a given name
        if (!in.is_open())                  // if not open
        {
            // output error and exit program
            cout << "\nERROR: Couldn't open input file " << inputFileName << "\n";
            continue;
        }

        // declare variables for manipulating lines
        cout << endl;
        vector<string> linesVector;
        string lineHolder;

        // ask user if they want to see each line
        cout << "Would you like to see every line in the input file? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'y' || doContinue == 'Y')
            cout << endl;
        // get each line from file
        while (getline(in, lineHolder))
        {
            // output the line if user chose so
            if (doContinue == 'Y' || doContinue == 'y')
                cout << lineHolder << "\n";
            linesVector.push_back(lineHolder); // push back the line to vector
        }
        in.close();
        cout << endl;

        // declare variables
        int foundAmount = 0;
        vector<string> outputVector;
        // start a for loop for looking up the line
        for (int i = 0; i < linesVector.size(); i++)
        {
            // declare variables
            string holder = linesVector.at(i);
            size_t index = holder.find(toLookFor);
            // if found not in the end
            if (index != string::npos)
            {
                // replace line with the one specified by user earlier
                holder.replace(index, toLookFor.size(), replaceWith);
                cout << i + 1 << ". " << holder << "\n";
                foundAmount++; // increment found amount
            }
            // push back the resulting line into the output vector
            outputVector.push_back(holder);
        }

        // declare variables
        int randLength = rand() % 10 + 3;
        string outputFileName = randString(randLength);
        // if found at least one line
        if (foundAmount > 0)
        {
            // output success message
            cout << "\nSuccessfully replaced " << foundAmount << " lines and outputed everything to " << outputFileName << "\n";
            // create output file
            fstream outputFile(outputFileName, ios::out);
            // where add each modified line
            for (int i = 0; i < outputVector.size(); i++)
                outputFile << outputVector.at(i) << endl;
            outputFile.close();
        }
        // if not found
        else
            // output error message
            cout << "\nNever found \"" << toLookFor << "\" in " << inputFileName << "\n";

        //////////////////////////////////////////////////////////////////////////////////
        cout << "\n/////////////////////////////////////////////////////////////\n"
             << "\nWould you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
        {
            cout << "\n/////////////////////////////////////////////////////////////\n\n";
            continue;
        }
        else
            break;
    } while (doContinue = 'Y' || doContinue == 'y');

    // func main end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
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

// create a function that will generate random string
string randString(int ch)
{
    // declare max array length
    const int maxArrSize = 25;
    // declare possible characters
    char possibleCharactersArr[maxArrSize] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                              'o', 'p', 'q', 'r', 's', 't', 'u',
                                              'v', 'w', 'x', 'y'};
    // declare result string
    string result = "";
    // create for loop
    for (int i = 0; i < ch; i++)
        // add random character from an earlier declared set to the string
        result += possibleCharactersArr[rand() % maxArrSize];

    // add file extension to result
    result += ".txt";
    // return result
    return result;
}
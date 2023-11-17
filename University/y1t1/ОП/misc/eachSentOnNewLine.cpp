// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
string fileNameInput();
string randString(int);
bool isReadable(const string &);
void generateRes(const string &, const string &);
/////////////////////////

// func main
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue, userDecision;
    int randLetterCount = rand() % 10 + 2;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This program will place every sentence in new line\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////
        string inputFileName = fileNameInput();
        string outputFileName = randString(randLetterCount);
        generateRes(inputFileName, outputFileName);
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

    // func end
    cout << "\nThanks for using this program\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    return 0;
}

// func place each sentence on its own line
void generateRes(const string &in, const string &out)
{
    // ~ local variables
    fstream iFile(in.c_str(), ios::in);
    fstream oFile(out.c_str(), ios::out);
    string buffer;
    vector<string> lines;
    int linesCount = 0;

    // get each line from file
    while (getline(iFile, buffer))
    {
        // declare holder of line
        string temp = buffer.c_str();
        // iterate through the whole line
        for (int i = 0; i < buffer.size(); i++)
            // if there is a space after dot, exclamation mark or a question mark
            if (temp[i] == '.' && temp[i + 1] == ' ' || temp[i] == '!' && temp[i + 1] == ' ' || temp[i] == '?' && temp[i + 1] == ' ')
                // replace space with new line
                temp[i + 1] = '\n';
        // push back that new line to lines vector
        lines.push_back(temp);
        // increase line count
        linesCount++;
    }

    // iterate over lines
    for (int i = 0; i < linesCount; i++)
    {
        // add lines from vector to file
        string temp = lines.at(i);
        oFile << temp << "\n";
    }

    // check if file is readable
    if (!(isReadable(out.c_str())))
        // if not, output error message
        cout << "ERROR: Could not write to file " << out << endl;
    else
        // if yes, output success message
        cout << "Successfully wrote to file " << out << endl;
    // func end
    return;
}

// func that will take file name from user
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

    // /Function
    return input;
}

// func that will generate random string
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

// func to check whether a file is readable
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
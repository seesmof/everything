// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// function prototypes //
string fileNameInput();
void generateRandFile(int, const string &);
string randString(int);
bool isReadable(const string &);
void resFileGenerator(const string &, const string &);
/////////////////////////

// declare main function
int main()
{
    // declare local variables //
    srand(time(NULL));
    char userDecision;
    string inFileName, outFileName;
    int numOfLets = rand() % 10 + 2;
    /////////////////////////////

    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will sort out numbers in file." << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    char doContinue;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // ask user if they have a file to read from
        cout << "Do you have a file to read from? (Y | N): ";
        cin >> userDecision;
        cin.ignore();

        // if they don't have a file
        if (userDecision == 'N' || userDecision == 'n')
        {
            // ask if they would want to generate it
            cout << endl;
            cout << "Would you like to generate one? (Y | N): ";
            cin >> userDecision;
            cout << endl;
            cin.ignore();

            // if the answer is no
            if (userDecision == 'N' || userDecision == 'n')
            {
                // end program
                cout << endl
                     << "Thanks for using this program." << endl
                     << endl
                     << "/////////////////////////////////////////////////////////////" << endl
                     << endl;
                break;
            }

            // ask user how many letters to put in file name
            cout << "How many letters do you want your file name to be?: ";
            cin >> numOfLets;
            int numOfNums;
            // create do while loop
            do
            {
                // ask user how many elements a file will contain
                cout << "How many numbers to generate? (4+): ";
                cin >> numOfNums;
                cin.ignore();

                // if the number is less than 4
                if (numOfNums < 4)
                {
                    // ask to enter again
                    cout << endl
                         << "Please enter a number that is or more than 4." << endl;
                    continue; // continue to next iteration
                }
            } while (numOfNums < 4); // do until they don't enter number more than 4

            // generate the input file name with given amount of letters
            inFileName = randString(numOfLets);
            // call a function that will generate the input file
            generateRandFile(numOfNums, inFileName);
            // check if the file is readable by calling a corresponding function
            if (!isReadable(inFileName))
                // output error if the file is not readable
                cout << "There were some problems generating the file " << inFileName << "." << endl;
            else
                // output success message if the file is readable
                cout << "The file " << inFileName << " was successfully generated." << endl;
        }
        // if they do haev a file
        else
        {
            // ask for a file name calling a corresponding function
            cout << endl;
            inFileName = fileNameInput();
        }

        // generate output file name calling a corresponding function
        outFileName = randString(numOfLets);
        // call a function to create an output file
        resFileGenerator(inFileName, outFileName);

        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << endl
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

// create a function that will generate file with random numbers
void generateRandFile(int n, const string &fileName)
{
    // declare local variables
    cout << endl;
    fstream file(fileName.c_str());
    // open the file to work with it
    file.open(fileName.c_str(), ios::out);

    // if file is not open
    if (!file.is_open())
    {
        // output error message
        cout << "ERROR: Couldn't open " << fileName << endl;
        return; // end function
    }

    // create a for loop
    for (int i = 0; i < n; i++)
    {
        int range = 10 - (-10) + 1;
        int randTemp = rand() % range + (-10);
        if (randTemp == 0)
        {
            randTemp += rand() % 10 + 1;
        }
        // output that buffer to file
        file << randTemp << endl;
    }

    // close the file
    file.close();
    // end function
    return;
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

    // return result
    result += ".txt";
    return result;
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

void resFileGenerator(const string &fileName, const string &resFile)
{
    // start function
    cout << endl;
    // declare local variables
    vector<int> negative;
    vector<int> positive;
    ifstream inFile(fileName.c_str(), ios::in);
    ofstream outFile(resFile.c_str(), ios::out);

    // declare variables for reading lines from input file
    int line;
    int n = 0;
    int pos = 0, neg = 0;
    // while we can read lines from input file
    while (!inFile.eof())
    {
        inFile >> line;
        // if given line, converted to integer, is less than 0
        if (line < 0)
        {
            // add it to negative array
            negative.push_back(line);

            // add increments
            n++;
            neg++;
        }
        // if given line, converted to integer, is greater than 0
        else
        {
            // add it to positive array
            positive.push_back(line);

            // add increments
            n++;
            pos++;
        }
    }
    // check if file is not readable using a corresponding function
    if (!isReadable(fileName))
        // output error message if not readable
        cout << "There were some problems reading " << fileName << endl;
    else
        // output success message if readable
        cout << "Reading from " << fileName << " ended successfully." << endl;

    // determine final counter by selecting the lesser counter
    int until = 0;
    if (pos > neg)
        until = neg;
    else
        until = pos;
    // if counter is not even
    if (!(until % 2 == 0))
        // subtract remainder from division by two from it
        until -= (until % 2);

    // create for loop to write the results to the output file
    for (int i = 0; i < until; i += 2)
    {
        // determine poistive pair
        int pos1 = positive[i];
        int pos2 = positive[i + 1];
        // write it to the output file
        outFile << pos1 << " " << pos2 << endl;

        // determine negative pair
        int neg1 = negative[i];
        int neg2 = negative[i + 1];
        // write it to the output file
        outFile << neg1 << " " << neg2 << endl;
    }

    // check if output file is readable using a corresponding function
    if (!isReadable(resFile))
        // output error if not
        cout << "There were some problems writing to " << resFile;
    else
        // output success if is
        cout << "Writing to " << resFile << " ended successfully.";
    // end function
    return;
}
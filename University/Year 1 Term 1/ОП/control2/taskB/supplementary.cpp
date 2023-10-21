// include necessary libraries
#include <bits/stdc++.h>
#include "supplementary.h"
using namespace std;

// create struct for holding emails data
struct Letter
{
    string outAddress;
    string inAddress;
    string recievedDate;
    string letterHeading;
    string letterText;
    int letterSize;
    bool isRead;
};

// for getting email address from user
string getEmailAddress()
{
    // ask user for email address
    string emailAddress;
    cout << "Please enter an email address: ";
    cin >> emailAddress;

    // validate email address
    if (emailAddress.find("@") == string::npos)
    {
        cout << "\nERROR: Invalid email address\n\n";
        getEmailAddress();
    }
    else
        return emailAddress;

    // should not reach this point
    return "";
}

// For getting text file inputted from user
string getFileName()
{
    // Declare local variables
    string fileName = "";         // for storing file name
    bool isExtensionFound = true; // for tracking file extension

    // Create do while loop for properly getting file name with extension
    do
    {
        // Ask user to enter file name
        cout << "Enter file name: ";
        cin >> fileName;

        // Create condition to check if file extension is found
        if (fileName.find(".") == string::npos)
        {
            // Execute if not found
            isExtensionFound = false; // set tracker state to false
            // Output error message
            cout << "\nERROR: File extension not found. Try again...\n\n";
            continue; // jump into next iteration
        }
        // If extension is found
        else
            break; // jump out of loop
    } while (isExtensionFound == false);

    // Return file name
    return fileName;
}

// For generating a random string of given length
string generateRandomString(int length)
{
    // Declare local variables
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy"; // characters pool to generate random string from
    string randomString = "";                                            // random string result holder

    // Generate a random character and add it to the string until it reaches the desired length
    for (int i = 0; i < length; i++)
    {
        // Generate a random index between 0 and the size of our character pool
        int index = rand() % chars.size();

        // Add the character at that index to our string
        randomString += chars[index];
    }

    return randomString + ".txt"; // Append ".txt" and return the generated string
}

// returns a vector containing only the unique elements from the input vector
vector<string> getUniqueElements(vector<string> &inputVector)
{
    vector<string> uniqueElements;      // to store unique elements as strings
    unordered_set<string> seenElements; // to store elements that have already been seen

    // iterate through each element of the inputVector
    for (string element : inputVector)
    {
        // check if the element is present in the seenElements container
        if (seenElements.find(element) == seenElements.end())
        {
            uniqueElements.push_back(element); // add the element to uniqueElements vector
            seenElements.insert(element);      // inserts the element into the seenElements set, if it is not already present
        }
    }

    // return a vector containing only the unique elements from the original vector
    return uniqueElements;
}

// for filling in the vector of emails
void fillVector(vector<Letter> &a, const string &FILE_NAME)
{
    // declare local variables
    fstream inFile(FILE_NAME.c_str(), ios::in);
    string lineReader;
    int numOfLetters = 1;
    vector<string> linesHolder;

    // check if we cannot read the file
    if (!inFile.is_open())
    {
        cout << "ERROR: Could not open file " << FILE_NAME << endl;
        return;
    }

    // read every line from the file
    while (getline(inFile, lineReader))
    {
        // when found empty line increase line number
        if (lineReader.empty())
            numOfLetters++;
        // in other cases add the line into a vector
        else
            linesHolder.push_back(lineReader);
    }

    // create a loop for sorting out each line and placing them into a correct spot
    for (int i = 0, j = 0; i < numOfLetters; i++, j += 5)
    {
        // create instance of struct in vector
        a.push_back(Letter());

        // fill out all the data from file
        a[i].outAddress = linesHolder[j];
        a[i].inAddress = linesHolder[j + 1];
        a[i].recievedDate = linesHolder[j + 2];
        a[i].letterHeading = linesHolder[j + 3];
        a[i].letterText = linesHolder[j + 4];

        // count words in letter text using another loop
        int lenHolder = 1;
        string strHolder = a[i].letterText;
        for (int i = 0; i < strHolder.length(); i++)
            if (strHolder[i] == ' ')
                lenHolder++;

        // add words count and status to vector as well
        a[i].letterSize = lenHolder;
        a[i].isRead = false;
    }

    // end function
    return;
}

// For making text bold
ostream &BOLD(ostream &os)
{
    return os << "\e[1m";
}

// For changing text back to normal
ostream &UNBOLD(ostream &os)
{
    return os << "\e[0m";
}

// For setting text color to red
ostream &RED(ostream &os)
{
    return os << "\033[1;31m";
}

// For changing text back to normal
ostream &UNRED(ostream &os)
{
    return os << "\033[0m";
}

// For setting text color to green
ostream &GREEN(ostream &os)
{
    return os << "\033[1;32m";
}

// For changing text back to normal
ostream &UNGREEN(ostream &os)
{
    return os << "\033[0m";
}
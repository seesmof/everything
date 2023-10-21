#include <bits/stdc++.h>
#include "menu.h"
#include "supplementary.h"
using namespace std;

// for offering user to make some actions on the letter
void letterManipulation(vector<Letter> &lettersVector, vector<int> &inboxLettersVector)
{
    char doContinue; // for indicating program continuation
    do
    {
        // declare necessary local variables
        int userDecision, inboxLettersCount = 0, index, input;
        string outAddress, recievedDate, inAddress, letterHeading, isRead, letterText;
        vector<int> inboxLettersVector;

        // output menu to user for choosing an action
        cout << BOLD << "\nWhat actions would you like to perform?\n"
             << UNBOLD;
        cout << "1. Read letter\n";
        cout << "2. Delete letter\n";
        cout << "3. Move to a file\n";
        cout << "4. Write letter\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> userDecision;

        // for reading letters
        if (userDecision == 1)
        {
            // ask user to choose a letter to read and check if its within range
            cout << "\nEnter a number of letter you would like to read: ";
            cin >> input;
            if (input > lettersVector.size())
            {
                cout << RED << "\nERROR: Invalid number of letter\n"
                     << UNRED;
                break;
            }

            // declare necessary variables
            index = input - 1;
            lettersVector[index].isRead = true;
            outAddress = lettersVector[index].outAddress;
            recievedDate = lettersVector[index].recievedDate;
            inAddress = lettersVector[index].inAddress;
            letterHeading = lettersVector[index].letterHeading;
            letterText = lettersVector[index].letterText;
            if (lettersVector[index].isRead == true)
                isRead = "Read";
            else
                isRead = "Unread";

            // output a letter
            cout << "\n=========================================\n\n";
            cout << "by " << outAddress << " - " << recievedDate << "\nto " << inAddress << " * " << letterHeading << " * " << isRead << "\n\n"
                 << letterText << endl;
            cout << "\n=========================================\n";
        }
        // for deleting letters
        else if (userDecision == 2)
        {
            // ask user to choose a letter to delete and validate it
            cout << "\nEnter a number of letter you would like to delete: ";
            cin >> input;
            if (input > lettersVector.size())
            {
                cout << RED << "\nERROR: Invalid number of letter\n"
                     << UNRED;
                break;
            }

            // delete a letter using erase function, pass an argument of vector size + letter index
            lettersVector.erase(lettersVector.begin() + input - 1);
        }
        // for moving letters to a file
        else if (userDecision == 3)
        {
            // ask user to choose a letter to move and validate it
            cout << "\nEnter a number of letter you would like to move: ";
            cin >> input;
            if (input > lettersVector.size())
            {
                cout << RED << "\nERROR: Invalid number of letter\n"
                     << UNRED;
                break;
            }

            // declare necessary variables
            index = input - 1;
            string fileName;
            lettersVector[index].isRead = true;

            // ask user if they already have a file to work with
            cout << BOLD << "\nSelect how exactly would you like to work with a file\n"
                 << UNBOLD;
            cout << "1. Create a new file\n";
            cout << "2. Add to an existing file\n";
            cout << "3. Exit\n";
            cout << "Enter your choice: ";
            cin >> userDecision;
            cout << endl;

            // get file name and declare a file variable
            fileName = getFileName();
            fstream file(fileName.c_str(), ios::out | ios::app);

            // check if file can be opened
            if (!file.is_open())
            {
                cout << RED << "\nERROR: Cannot open file " << fileName << endl
                     << UNRED;
                return;
            }

            // declare even more variables
            outAddress = lettersVector[index].outAddress;
            inAddress = lettersVector[index].inAddress;
            recievedDate = lettersVector[index].recievedDate;
            letterHeading = lettersVector[index].letterHeading;
            letterText = lettersVector[index].letterText;

            // if its a new file
            if (userDecision == 1)
                // add stripes at the top of the file
                file << "=========================================\n\n";

            // output letter information into it
            file << "by " << outAddress << " - " << recievedDate << "\n";
            file << "to " << inAddress << " * " << letterHeading << "\n";
            file << "\n"
                 << letterText << "\n";
            file << "\n=========================================\n\n";

            if (file.good())
                cout << GREEN << fileName << " successfully generated\n"
                     << UNGREEN;
        }
        // for writing letters
        else if (userDecision == 4)
        {
            // declare an instance of Letter struct
            Letter letter;

            // ask user for his email address
            cout << "\nEnter your email address\n";
            letter.outAddress = getEmailAddress();

            // ask user for recipient's address
            cout << "\nEnter recipient's email address\n";
            letter.inAddress = getEmailAddress();

            // create variables for getting current time
            time_t now = time(0);           // get the current time in seconds
            tm *ltm = localtime(&now);      // convert the current time to a local time structure
            int day = ltm->tm_mday;         // get the day of the month from the tm structure
            int month = 1 + ltm->tm_mon;    // get the month from struct and increment by 1 to get the correct value
            int year = 1900 + ltm->tm_year; // calculate the current year based on the localtime structure
            int hour = ltm->tm_hour;        // get the hour from the tm structure
            int min = ltm->tm_min;          // assigns the minute value from the ltm struct to the min variable

            stringstream recievedDateHolder; // holds the recieved date from the input stream
            // concatenates the day, month, year, hour, and minute into a formatted date string.
            recievedDateHolder << (day < 10 ? "0" : "") << day << "."
                               << (month < 10 ? "0" : "") << month << "."
                               << year << " "
                               << (hour < 10 ? "0" : "") << hour << ":"
                               << (min < 10 ? "0" : "") << min;
            // set the recievedDate property of the letter object to the value of the recievedDateHolder string
            letter.recievedDate = recievedDateHolder.str();

            // ask user to enter a letter heading
            string letterHeading;
            cin.ignore();
            cout << "\nEnter the topic of your letter: ";
            getline(cin, letterHeading);
            letter.letterHeading = letterHeading;

            // ask user to enter the letter text
            string letterText;
            cout << "\nEnter the text of your letter: ";
            getline(cin, letterText);
            letter.letterText = letterText;

            // add letter object into the global array
            lettersVector.push_back(letter);
        }
        else // if user chose to exit
            break;

        // ask user if they want to continue
        cout << "\nWould you like to continue manipulating letters? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'y' || doContinue == 'Y')
            continue;
        else
            break;
    } while (doContinue == 'y' || doContinue == 'Y');

    return;
}

// for outputting search results
void searchResults(int inboxLettersCounter, vector<int> &inboxLettersVector, vector<Letter> &lettersVector)
{
    // indicate how many letters were found
    cout << GREEN << "\nEmails found (" << inboxLettersCounter << "):\n"
         << UNGREEN;
    // output all of them
    for (int i = 0; i < inboxLettersVector.size(); i++)
    {
        // declare variables for easy access
        int index = inboxLettersVector[i];
        string outAddress = lettersVector[index].outAddress;
        string recievedDate = lettersVector[index].recievedDate;
        string inAddress = lettersVector[index].inAddress;
        string letterHeading = lettersVector[index].letterHeading;
        string isRead;
        if (lettersVector[index].isRead == true)
            isRead = "Read";
        else
            isRead = "Unread";

        // output each letter, indicating its number for convenience
        cout << "(" << index + 1 << ")"
             << " by " << outAddress << " - " << recievedDate << "\n    to " << inAddress << " * " << letterHeading << " * " << isRead << "\n";
    }

    // end function execution
    return;
}

// For outputting emails from the inbox
void outputLetters(vector<Letter> &lettersVector, string inEmailAddress)
{
    char doContinue; // for indicating program continuation
    do
    {
        // declare local variables
        int index, inboxLettersCount = 0, sentLettersCount = 0;
        string outAddress, recievedDate, inAddress, letterHeading, isRead;
        vector<int> inboxLettersVector;
        vector<int> sentLettersVector;

        // For identifying emails in the inbox
        for (int i = 0; i < lettersVector.size(); i++)
        {
            // declare variables for easier access
            string inEmailHolder = lettersVector[i].inAddress;
            string outEmailHolder = lettersVector[i].outAddress;

            // check if the letter is directed to us, but not sent by us
            if (inEmailHolder == inEmailAddress && outEmailHolder != inEmailAddress)
            {
                // if so add its index to vector and increase inbox letters count
                inboxLettersVector.push_back(i);
                inboxLettersCount++;
            }
            // check if the letter is sent by us, but not directed to us
            else if (outEmailHolder == inEmailAddress && inEmailHolder != inEmailAddress)
            {
                // if so add its index to vector and increase sent letters count
                sentLettersVector.push_back(i);
                sentLettersCount++;
            }
        }

        // check if the inbox letter counter is at 0
        if (inboxLettersCount == 0)
        {
            // if so output an error and stop the loop
            cout << RED << "\nNo emails in the inbox\n"
                 << UNRED;
            break;
        }

        // create a loop for outputting each letter's information
        cout << BOLD << "\nInbox (" << inboxLettersCount << "):\n"
             << UNBOLD;
        for (int i = 0; i < inboxLettersVector.size(); i++)
        {
            // declare local variables for outputting the letter's information
            index = inboxLettersVector[i];
            outAddress = lettersVector[index].outAddress;
            recievedDate = lettersVector[index].recievedDate;
            inAddress = lettersVector[index].inAddress;
            letterHeading = lettersVector[index].letterHeading;
            if (lettersVector[index].isRead == true)
                isRead = "Read";
            else
                isRead = "Unread";

            // output letter information and nubmer to user
            cout << "(" << index + 1 << ")"
                 << " by " << outAddress << " - " << recievedDate << "\n    to " << inAddress << " * " << letterHeading << " * " << isRead << "\n";
        }

        // check if sent letters counter is more than 0
        if (sentLettersCount > 0)
        {
            // create a loop for outputting each sent letter's info
            cout << BOLD << "\nSent (" << sentLettersCount << "):\n"
                 << UNBOLD;
            for (int i = 0; i < sentLettersVector.size(); i++)
            {
                // declare local variables
                index = sentLettersVector[i];
                outAddress = lettersVector[index].outAddress;
                recievedDate = lettersVector[index].recievedDate;
                inAddress = lettersVector[index].inAddress;
                letterHeading = lettersVector[index].letterHeading;
                if (lettersVector[index].isRead == true)
                    isRead = "Read";
                else
                    isRead = "Unread";

                // output letter information and nubmer to user
                cout << "(" << index + 1 << ")"
                     << " by " << outAddress << " - " << recievedDate << "\n    to " << inAddress << " * " << letterHeading << " * " << isRead << "\n";
            }
        }

        // call a function to offer user to make some actions on letter
        letterManipulation(lettersVector, inboxLettersVector);

        // ask user to continue working in inbox
        cout << "\nWould you like to continue working in inbox? (Y / N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
            continue;
        else
            break;

    } while (doContinue == 'y' || doContinue == 'Y');

    // end function execution
    return;
}

// for searching for a letter by different parameters
void searchLetters(vector<Letter> &lettersVector)
{
    char doContinue; // to indicate program continuation
    do
    {
        // declare local variables
        int userDecision, inboxLettersCount = 0;
        string outAddress, recievedDate, inAddress, letterHeading, isRead, input;
        vector<int> inboxLettersVector;

        // output a menu for user to choose what parameter they would like to search on
        cout << BOLD << "\nWhat parameter would you like to search by?\n"
             << UNBOLD;
        cout << "1. Recieved Date\n";
        cout << "2. Out Address\n";
        cout << "3. In Address\n";
        cout << "4. Letter Topic\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> userDecision;

        // create a switch statement for processing user input
        switch (userDecision)
        {
        case 1: // for searching based on received date
        {
            // ask user to enter a date
            cout << "\nEnter the date you would like to search for: ";
            cin >> input;

            // create a loop for iterating over the vector and looking for that date
            for (int i = 0; i < lettersVector.size(); i++)
            {
                // declare local variable for easier access
                string letterDateOrig = lettersVector[i].recievedDate;
                recievedDate = letterDateOrig.substr(0, letterDateOrig.find_last_of(" "));

                // check if current letter's date corresponds to inputter one
                if (recievedDate == input)
                {
                    // if so increment the counter and add index to indeces vector
                    inboxLettersCount++;
                    inboxLettersVector.push_back(i);
                }
            }

            // call the function to output the results of a search
            searchResults(inboxLettersCount, inboxLettersVector, lettersVector);

            // if no results were found break out of switch
            if (inboxLettersCount == 0)
                break;

            // prompt user to make some actions on the letter
            letterManipulation(lettersVector, inboxLettersVector);

            // stop swtich execution
            break;
        }
        case 2: // for searching based on senders email address
        {
            // ask user to enter an email address and validate it by looking for @ sign in it
            cout << "\nEnter the address you would like to search for: ";
            cin >> input;
            if (input.find('@') == string::npos)
            {
                cout << "\nERROR: Invalid email address. Try again...\n";
                break;
            }

            // create a loop for searching for a letter with this address
            int inboxLettersCounter = 0;
            for (int i = 0; i < lettersVector.size(); i++)
            {
                // for easier access
                outAddress = lettersVector[i].outAddress;

                // if current letter's address corresponds with the input
                if (outAddress == input)
                {
                    // increase the counter and add index to indeces vector
                    inboxLettersCounter++;
                    inboxLettersVector.push_back(i);
                }
            }

            // call a function to output the search resutls
            searchResults(inboxLettersCounter, inboxLettersVector, lettersVector);

            // if no results were found break out of switch
            if (inboxLettersCounter == 0)
                break;

            // prompt user to make some actions on a letter
            letterManipulation(lettersVector, inboxLettersVector);

            // break out of switch
            break;
        }
        case 3: // for searching letters based on a reciever's email address
        {
            // ask user to enter an email address and validate it by looking for @ sign in it
            cout << "\nEnter the address you would like to search for: ";
            cin >> input;
            if (input.find('@') == string::npos)
            {
                cout << RED << "\nERROR: Invalid email address. Try again...\n"
                     << UNRED;
                break;
            }

            // create a loop for searching for a letter with an inputted address
            int inboxLettersCounter = 0;
            for (int i = 0; i < lettersVector.size(); i++)
            {
                // for easier access
                inAddress = lettersVector[i].inAddress;

                // if current letters in adress corresponds to an input
                if (inAddress == input)
                {
                    // increase a counter and add letter index into a vector
                    inboxLettersCounter++;
                    inboxLettersVector.push_back(i);
                }
            }

            // call a function to ouput the resutls
            searchResults(inboxLettersCounter, inboxLettersVector, lettersVector);

            // if no results were found break out of switch
            if (inboxLettersCounter == 0)
                break;

            // prompt user to manipulate a letter
            letterManipulation(lettersVector, inboxLettersVector);

            // break out of switch
            break;
        }
        case 4: // for searching based on a letter heading
        {
            // prompt user to enter a letter heading
            cin.ignore();
            cout << "\nEnter the heading you would like to search for: ";
            getline(cin, input);

            // create a loop for looking for a letter with the inputted heading
            int inboxLettersCounter = 0;
            for (int i = 0; i < lettersVector.size(); i++)
            {
                // for easier access
                letterHeading = lettersVector[i].letterHeading;

                // check if current letter's heading corresponds to the inputed one
                if (letterHeading == input)
                {
                    // if so increase the counter and add letter's index to vector
                    inboxLettersCounter++;
                    inboxLettersVector.push_back(i);
                }
            }

            // call a function to output the search results to user
            searchResults(inboxLettersCounter, inboxLettersVector, lettersVector);

            // check if no results were found, then stop the switch execution
            if (inboxLettersCounter == 0)
                break;

            // call a function to manipulate the letter
            letterManipulation(lettersVector, inboxLettersVector);

            // break out of switch
            break;
        }
        default: // for any other case
        {
            // break out of switch
            break;
        }
        }

        // ask user if they wanna continue or not
        cout << "\nWould you like to continue searching for letters? (Y / N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
            continue;
        else
            break;

    } while (doContinue == 'y' || doContinue == 'Y');

    // end function execution
    return;
}

// for searching letters by keyword
void searchLetters(vector<Letter> &lettersVector, string keyword)
{
    char doContinue; // to indicate program continuation
    do
    {
        // declare local variables
        int inboxLettersCount = 0;
        string letterHeading, letterText;
        vector<int> inboxLettersVector;

        // create a loop that will look for keywords in letter's heading and body
        int inboxLettersCounter = 0;
        for (int i = 0; i < lettersVector.size(); i++)
        {
            // for easier access
            letterText = lettersVector[i].letterText;
            letterHeading = lettersVector[i].letterHeading;

            // declare pos variable and look for keyword in those two strings
            size_t pos = 0;
            if (((pos = letterText.find(keyword, pos)) != string::npos) || ((pos = letterHeading.find(keyword, pos)) != string::npos))
            {
                // if found increment the counter, increase pos and add letter index into indeces vector
                inboxLettersCounter++;
                inboxLettersVector.push_back(i);
                pos += keyword.length();
            }
        }

        // call function to output the search results
        searchResults(inboxLettersCounter, inboxLettersVector, lettersVector);

        // if no letters were found stop the loop
        if (inboxLettersCounter == 0)
            break;

        // else offer user to execute some actions on the letter
        letterManipulation(lettersVector, inboxLettersVector);

        // ask user if they would like to continue
        cout << "\nWould you like to continue searching for letters? (Y / N): ";
        cin >> doContinue;
        if (doContinue == 'Y' || doContinue == 'y')
            continue;
        else
            break;

    } while (doContinue == 'y' || doContinue == 'Y');

    // end function execution
    return;
}

// for outputting main menu to user
void outputMenu(vector<Letter> &lettersVector, string inEmailAddress)
{
    int choice; // for holding user choice
    // ask user what action to perform
    cout << BOLD << "\nWhat would you like to do?\n"
         << UNBOLD;
    cout << "1. Check you inbox\n";
    cout << "2. Search for letters\n";
    cout << "3. Search by keywords\n";
    cout << "4. Actions with letters\n";
    cout << "5. Exit\n";
    cout << "Enter your choice: ";
    cin >> choice;

    // for checking and inbox
    if (choice == 1)
    {
        // call a corresponding function
        outputLetters(lettersVector, inEmailAddress);
    }
    // for searching for letters
    else if (choice == 2)
    {
        // call a corresponding function
        searchLetters(lettersVector);
    }
    // for searching by keywords
    else if (choice == 3)
    {
        // ask user to enter a keyword
        string keyword;
        cout << "\nEnter a keyword you would like to search by: ";
        cin >> keyword;

        // call a corresponding function
        searchLetters(lettersVector, keyword);
    }
    // for manipulating letters
    else if (choice == 4)
    {
        // call a corresponding function
        vector<int> foo;
        letterManipulation(lettersVector, foo);
    }

    // end function execeution
    return;
}
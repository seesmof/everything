// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// ~ function prototypes //
string fileNameInput();
void generateBinaryFile(int, const string &);
string randString(int);
void filesCompare(const string &, const string &, const string &, int);
int countLines(const string &);
void isReadable(const string &);
///////////////////////////

// declare main function
int main()
{
     // ~ declares local variables //
     srand(time(NULL));
     char userDecision;
     string fileNameHolder, fileOne, fileTwo, fileResult;
     int numberOfElements, numberOfLetters = rand() % 10;
     vector<int> lineCountVec(2);
     ////////////////////////////////

     // project intro
     cout << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl
          << "Welcome! This program will manipulate binary files." << endl
          << endl
          << "/////////////////////////////////////////////////////////////" << endl
          << endl;
     char doContinue;
     do
     {
          //////////////////////////////////////////////////////////////////////////////////

          // ~ ask user whether they have files to read from
          cout << "Do you have a file to read from? (Y | N) ";
          cin >> userDecision;

          // if answer is no
          if (userDecision == 'N' || userDecision == 'n')
          {
               // ask if they would like to generate those
               cout << "Would you like to create a binary file with random numbers? (Y | N) ";
               cin >> userDecision;

               // if they answer no
               if (userDecision == 'N' || userDecision == 'n')
                    // stop program execution
                    return 0;

               // repeat for two files
               for (int i = 0; i < 2; i++)
               {
                    // output file number
                    cout << endl
                         << "Generating file " << i + 1 << endl;

                    // declare local variables
                    numberOfElements = 0, numberOfLetters = 0;

                    // ask user how many elements to generate
                    cout << "How many elements to generate? ";
                    cin >> numberOfElements;
                    // ask user how many letters the file name will consist of
                    cout << "Number of letters in a file name: ";
                    cin >> numberOfLetters;

                    // call function to generate random file name with given number of letters and assign the result to file name holder
                    fileNameHolder = randString(numberOfLetters);
                    // if we are generating file one
                    if (i == 0)
                         // assign file name holder to file one name
                         fileOne = fileNameHolder;
                    else
                         // else assign file name holder to file two name
                         fileTwo = fileNameHolder;

                    // generate the file itself by calling the corresponding function
                    generateBinaryFile(numberOfElements, fileNameHolder);
               }
          }
          // if they answer !no
          else
          {
               // repeat two times for two files
               cout << endl;
               for (int i = 0; i < 2; i++)
               {
                    // output file number
                    cout << i + 1 << ". ";
                    // file name holder is inputted by user using a corresponding function
                    fileNameHolder = fileNameInput();

                    // if we are generating file one
                    if (i == 0)
                         // assign file name holder to file name one
                         fileOne = fileNameHolder;
                    else
                         // else assign file name holder to file name two
                         fileTwo = fileNameHolder;
                    cout << endl;
               }
          }

          // regardless of choice, repeat twice
          for (int i = 0; i < 2; i++)
          {
               // if we are working with file one, then count the number of lines in it
               if (i == 0)
                    lineCountVec[i] = countLines(fileOne);
               else
                    // else count number of lines in file two
                    lineCountVec[i] = countLines(fileTwo);

               // determine which one has less lines and assign it to number of lines that the resulting file will have
               if (lineCountVec[0] < lineCountVec[1])
                    numberOfElements = lineCountVec[0];
               else
                    numberOfElements = lineCountVec[1];
          }

          // generate the name of resulting file using a random letters count
          fileResult = randString(numberOfLetters);
          // compare those two files using a corresponding function
          filesCompare(fileOne, fileTwo, fileResult, numberOfElements);
          fstream resFile(fileResult.c_str(), ios::binary | ios::in);

          isReadable(fileResult);

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

// Function that will take file name from user
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

// create a function that will generate the binary file with random numbers
void generateBinaryFile(int n, const string &fileName)
{
     // declare local variables
     cout << endl;
     fstream file(fileName.c_str(), ios::binary);
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
          // fill buffer with random number
          int randTemp = rand() % 100;
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

     // add file extension to result
     result += ".bin";
     // return result
     return result;
}

// declare function that will count lines in file
int countLines(const string &a)
{
     // declare local variables
     int count = 0;
     string line;
     ifstream aFile(a.c_str(), ios::in | ios::binary);

     // while we can get a line from the file
     while (getline(aFile, line))
          // increment count
          count++;
     // return number of lines
     return count; // end function
}

// declare function to check whether a file is readable
void isReadable(const string &fileName)
{
     // declare local variables for reading a file
     fstream file(fileName, ios::in | ios::out);

     // if result file is successfully opened
     if (file.good())
          // output successs message
          cout << fileName << " is working properly.";
     else
          // if not, output failure message
          cout << "ERROR: Could not open file " << fileName;
}

// create a function for comparing two files and generating the result
void filesCompare(const string &a, const string &b, const string &r, int n)
{
     // declare local variables
     fstream rFile(r.c_str(), ios::out | ios::binary);
     ifstream aFile(a.c_str(), ios::in | ios::binary);
     ifstream bFile(b.c_str(), ios::in | ios::binary);
     int res;
     string lineA, lineB, lineR;

     // create a for loop
     for (int i = 0; i < n; i++)
     {
          // get numbers from the two lines into local string
          getline(aFile, lineA);
          getline(bFile, lineB);

          // if when converted to int line one > line two
          if (stoi(lineA.c_str()) > stoi(lineB.c_str()))
               // add it to buffer
               res = stoi(lineA.c_str());
          else
               // else add line two to buffer
               res = stoi(lineB.c_str());

          // output buffer to result file
          rFile << res << endl;
     }

     // end function
     return;
}
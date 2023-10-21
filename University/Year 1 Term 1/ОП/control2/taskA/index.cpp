// include necessary libraries
#include "../../lib.h"
using namespace std;

// function prototypes //
void fillVector(int, int, const string &, vector<vector<int>> &);
void fillVector(int, int, vector<vector<int>> &);
void outputVector(int, int, vector<vector<int>> &);
void getGameResults(int, int, vector<vector<int>> &, int, int);
void getGameResults(int, int, vector<vector<int>> &, int, int, const string &);
int getMaxPoints(vector<vector<int>> &, int, int);
/////////////////////////

// Declare struct with coordinates for easier access
struct Coordinate
{
    int I, J;
};

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    string inFileName, outFileName;
    Coordinate matrixSize;
    vector<vector<int>> matrixVector;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task A\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // Ask user how they want to get the matrix to console
        cout << BOLD << "Would you like to enter field data from file or from command line?\n"
             << UNBOLD;
        cout << "1. Enter from file\n";
        cout << "2. Get from command line\n";
        cout << "3. Exit\n";
        cout << "Choice: ";
        cin >> userDecision;
        cout << endl;

        // Ask user to enter the number of rows and columns of the matrix
        cout << "Enter number of rows and columns in matrix (Rows Cols): ";
        cin >> matrixSize.I >> matrixSize.J;

        // If user chose to enter the matrix from file
        if (userDecision == 1)
        {
            // ask user to enter file name using a corresponding function
            inFileName = getFileName();

            // Call a function to fill in the matrix from the input file
            fillVector(matrixSize.I, matrixSize.J, inFileName, matrixVector);

            // Output the matrix to the screen using a corresponding function
            cout << "\nYour array is: \n";
            outputVector(matrixSize.I, matrixSize.J, matrixVector);
        }
        // If user chose to get matrix from command line
        else if (userDecision == 2)
        {
            // Call a function to either manually fill in or randomly generate matrix
            fillVector(matrixSize.I, matrixSize.J, matrixVector);

            // Output the resulting matrix to the screen
            cout << "\nYour array is: \n";
            outputVector(matrixSize.I, matrixSize.J, matrixVector);
        }
        // If user entered anything else
        else
            break; // stop program execution

        // declare local variables for storing finish point coordinates
        Coordinate finishPoint;

        // Create a do while loop and execute it until the values entered are within the field range
        do
        {
            // Ask user to enter finish point coordinates
            cout << "\nEnter finish point coordinates (Row Col): ";
            cin >> finishPoint.I >> finishPoint.J;

            // If given coordinates are exceeding the field range
            if (finishPoint.I > matrixSize.I || finishPoint.J > matrixSize.J)
            {
                // Output error message
                cout << RED << "\nERROR: Such point does not exist. Try again\n"
                     << UNRED;
                continue; // jump to next iteration
            }
            // If given coordinates are within the field range
            else
                break; // jump out of the loop
        } while (finishPoint.I > matrixSize.I || finishPoint.J > matrixSize.J);

        // Decrement the coordinates to correctly manipulate them in the field
        finishPoint.I -= 1;
        finishPoint.J -= 1;

        // Ask user if they would like to play the game live or just get the results
        cout << BOLD << "\nWould you like to play the game here or just get the answer?\n"
             << UNBOLD;
        cout << "1. Play live\n";
        cout << "2. Get the answer\n";
        cout << "3. Exit\n";
        cout << "Choice: ";
        cin >> userDecision;

        // If user chose to play live
        if (userDecision == 1)
            // Execute the corresponding function that will play the game in console
            getGameResults(matrixSize.I, matrixSize.J, matrixVector, finishPoint.I, finishPoint.J);
        else if (userDecision == 2)
        {
            // Ask user if they want to enter or generate a file name
            cout << BOLD << "\nWould you like to enter or randomly generate an output file name?\n"
                 << UNBOLD;
            cout << "1. Enter the file name\n";
            cout << "2. Randomly generate an output file name\n";
            cout << "3. Exit\n";
            cout << "Choice: ";
            cin >> userDecision;

            // If user chose to enter a file name by themselves
            if (userDecision == 1)
            {
                // ask user to enter a file name using the corresponding function
                cout << endl;
                outFileName = getFileName();
            }
            // If user chose to generate a random file name
            else if (userDecision == 2)
            {
                int numOfLetters; // for storing number of letters
                // Ask user to enter a number of letters in the file name
                cout << "\nEnter the number of letters you want in file name: ";
                cin >> numOfLetters;

                // Generate a random file name using the corresponding function
                outFileName = generateRandomString(numOfLetters);
            }
            // If use entered anything else
            else
                break; // stop program execution

            getGameResults(matrixSize.I, matrixSize.J, matrixVector, finishPoint.I, finishPoint.J, outFileName);
        }
        // If use entered anything else
        else
            break; // stop program execution

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

// For playing the game inside console in live mode
void getGameResults(int n, int m, vector<vector<int>> &a, int finishPosI, int finishPosJ)
{
    // Declare local variables
    const int STARTING_POSITION_I = 0, STARTING_POSITION_J = m - 1;           // for holding the starting position
    int currentPosI = STARTING_POSITION_I, currentPosJ = STARTING_POSITION_J; // for holding the current position
    bool doWin = false;                                                       // for checking if the game is won or not
    int score = a[currentPosI][currentPosJ];                                  // for holding the score with initial value of the current position
    string oFileName;                                                         // in case the program needs to use the file
    vector<char> answers;                                                     // for holding the answers

    // Outputting a note to the console, utilizing the stilizational functions
    cout << "\nNOTE: Current position is displayed in " << BOLD << "bold" << UNBOLD << ", legal moves in " << RED << "red" << UNRED << " and destination in " << GREEN << "green.\n\n"
         << UNGREEN;

    // Ask user to make some decisions
    cout << "Before we begin, please make an importnat choice\n";
    char doUseAutopilot; // for holding the answer
    char doOutputToFile; // for holding the answer

    // Ask user if they want to use the autopilot
    cout << "Would you like to play the game on autopilot? (Y / N): ";
    cin >> doUseAutopilot;

    if (doUseAutopilot == 'y' || doUseAutopilot == 'Y')
    {
        cout << GRAY << "\nKeep in mind that the path offered by this version of autopilot might not be optimal.\n\n"
             << UNGRAY;
    }

    // Ask user if they want to output the results of the game to a file
    cout << "Would you like output the results to the file? (Y / N): ";
    cin >> doOutputToFile;
    cout << endl;

    int maxPoints = getMaxPoints(a, finishPosI, finishPosJ);
    cout << YELLOW << "Maximum achieavable number of points: " << maxPoints << endl
         << endl
         << UNYELLOW;

    // Start do while loop and execute it until the game is over
    do
    {
        // Declare local variables necessary for the game
        char nextMoveHolder = 'l';                              // for holding the answer regarding the next move
        int leftPosI = currentPosI, leftPosJ = currentPosJ - 1; // for holding left move position
        int downPosI = currentPosI + 1, downPosJ = currentPosJ; // for holding down move position
        int leftPosValue, downPosValue;                         // for holding left and down move values

        // Creating for loops for outputting the board
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                // Creating conditions for outputting the right elements
                if (i == currentPosI && j == currentPosJ)         // if element is in current position
                    cout << YELLOW << a[i][j] << UNYELLOW << " "; // output it in bold
                else if (i == finishPosI && j == finishPosJ)      // if element is in the destination position
                    cout << GREEN << a[i][j] << UNGREEN << " ";   // output it in green
                else if (i == leftPosI && j == leftPosJ)          // if element is to the left of the current position
                    cout << RED << a[i][j] << UNRED << " ";       // output it in red
                else if (i == downPosI && j == downPosJ)          // if element is below the current position
                    cout << RED << a[i][j] << UNRED << " ";       // output it in red
                else                                              // if element is any other element
                    cout << a[i][j] << " ";                       // output it

                if (i == leftPosI && j == leftPosJ)      // if element
                    leftPosValue = a[i][j];              // assign its value to left holder
                else if (i == downPosI && j == downPosJ) // if element
                    downPosValue = a[i][j];              // assign its value to down holder
            }
            cout << endl;
        }

        // Creating conditions for checking if the user won or lost the game

        // If current position is the same as the finish position
        if (currentPosI == finishPosI && currentPosJ == finishPosJ)
        {
            doWin = true; // change win state to true
            // Output win message to screen
            cout << GREEN << "\nCongatulations! You won the game\n"
                 << UNGREEN;
            cout << "Your total score is " << score << endl;
            break; // stop program execution
        }
        // If user has either exceeded the limits or made a move in wrong direction
        else if ((finishPosJ == STARTING_POSITION_J && currentPosJ < finishPosJ) || (finishPosI == STARTING_POSITION_I && currentPosI > finishPosI) || (currentPosJ < finishPosJ) || (currentPosI > finishPosI))
        {
            doWin = false; // change win state to false
            // Output lose message to screen
            cout << RED << "\nYou lost the game. Please try again later\n"
                 << UNRED;
            break; // stop program execution
        }

        // Creating condition for calculating the next move
        if (finishPosJ == STARTING_POSITION_J)      // if finish point is at the same column as starting position
            nextMoveHolder = 'd';                   // next move will always be down
        else if (finishPosI == STARTING_POSITION_I) // if finish point is at the same row as starting position
            nextMoveHolder = 'l';                   // next move will always be left
        else
        {
            if (currentPosJ == finishPosJ)      // if current position is at the same column as finish point
                nextMoveHolder = 'd';           // next move is down
            else if (currentPosI == finishPosI) // if current position is at the same row as finish point
                nextMoveHolder = 'l';           // next move is left

            // If non of those are met, then choose the one with the most points
            else if (leftPosValue >= downPosValue) // if left position value is greater or equal to down position value
                nextMoveHolder = 'l';              // next move is left
            else
                nextMoveHolder = 'd'; // next move is down
        }
        answers.push_back(nextMoveHolder);

        // After calculating the next move, move on to playing the game itself

        // If user chose to use autopilot
        if (doUseAutopilot == 'y' || doUseAutopilot == 'Y')
        {
            // create a delay of 2 seconds for user to be able to track the game state
            this_thread::sleep_for(chrono::seconds(2));

            // If calculated next move is to the left
            if (nextMoveHolder == 'l' || nextMoveHolder == 'L')
            {
                // output prompt with a corresponding message
                cout << "\nYour next move is " << BOLD << "left" << UNBOLD << endl
                     << endl;
                // add left position value to global score
                score += leftPosValue;
                // move current position to the left and move over to the next iteration
                currentPosJ -= 1;
                continue;
            }
            // In any other case
            else
            {
                // output prompt with a corresponding message
                cout << "\nYour next move is " << BOLD << "down" << UNBOLD << endl
                     << endl;
                //  add down position value to global score
                score += downPosValue;
                // move current position down and move over to the next iteration
                currentPosI += 1;
                continue;
            }
        }
        // If user didn't choose to use the autopilot
        else
        {
            // Creating conditions that will check the next calculated move and output corresponding text to user as a hint
            if (nextMoveHolder == 'l' || nextMoveHolder == 'L')
                cout << "\nYour next move should be " << BOLD << "left\n"
                     << UNBOLD;
            else
                cout << "\nYour next move should be " << BOLD << "down\n"
                     << UNBOLD;

            // Ultimately the decision itself is to be made by user only
            char move;
            cout << "Your next move is? (L / D): ";
            cin >> move;

            // If user decided to move to the left
            if (move == 'L' || move == 'l')
            {
                // output a message with a correspoding text
                cout << "Made a move to the left\n\n";
                // add left move value to general score
                score += leftPosValue;
                // change current position and continue
                currentPosJ -= 1;
                continue;
            }
            // If user decided to move down
            else if (move == 'D' || move == 'd')
            {
                // output a message with a correspoding text
                cout << "Made a move down\n\n";
                // add down move value to general score
                score += downPosValue;
                // change current position and continue
                currentPosI += 1;
                continue;
            }
        }
    } while (!doWin);

    if (doOutputToFile == 'y' || doOutputToFile == 'Y')
    {
        cout << endl;
        oFileName = getFileName();
        fstream oFile(oFileName.c_str(), ios::out);

        if (!oFile.is_open())
            cout << RED << "ERROR: Could not open file " << oFileName << UNRED << endl;

        oFile << "======================================================\n";
        oFile << "\t\t\tThank you for using this program\n";
        oFile << "======================================================\n";
        oFile << "\nYour matrix:\n";
        // Creating for loops for outputting the board
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                oFile << a[i][j] << " "; // output matrix element
            }
            oFile << endl;
        }
        oFile << "\n======================================================\n";
        oFile << "\nThe moves you should take to win it:\n";

        for (int i = 0; i < answers.size(); i++)
        {
            if (answers[i] == 'l' || answers[i] == 'L')
                oFile << "Move left\n";
            else
                oFile << "Move down\n";
        }

        oFile << "\n======================================================\n";
        oFile << "\nThe game is won with " << answers.size() << " moves\n";
        oFile << "The total score is " << score << " points\n";

        if (oFile.good())
            cout << GREEN << "\nSuccessfully generated " << oFileName << ".\n"
                 << UNGREEN;

        oFile.close();
    }

    // End function execution
    return;
}

// For getting the game results outputted in a file
void getGameResults(int n, int m, vector<vector<int>> &a, int finishPosI, int finishPosJ, const string &OUTPUT_FILENAME)
{
    // Declare local variables
    const int STARTING_POSITION_I = 0, STARTING_POSITION_J = m - 1;           // for holding the starting position
    int currentPosI = STARTING_POSITION_I, currentPosJ = STARTING_POSITION_J; // for holding the current position
    bool doWin = false;                                                       // for checking if the game is won or not
    int score = a[currentPosI][currentPosJ];                                  // for holding the score with initial value of the current position
    fstream oFile(OUTPUT_FILENAME.c_str(), ios::out);                         // for writing output file
    int iterator = 1;                                                         // for iterating over the matrix

    // Create condition for checking if the file exists
    if (!oFile.is_open())
    {
        // Output error message
        cout << RED << "ERROR: Could not open file " << OUTPUT_FILENAME << UNRED << endl;
        return; // end function execution
    }
    // If file exists
    else
    {
        // Write relevant information
        oFile << "======================================================\n";
        oFile << "\t\t\tThank you for using this program\n";
        oFile << "======================================================\n";
        oFile << "\nYour matrix:\n";

        // Creating for loops for outputting the board
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                oFile << a[i][j] << " "; // output matrix element
            }
            oFile << endl;
        }

        // Write necessary information
        oFile << "\n======================================================\n";
        int maxPoints = getMaxPoints(a, finishPosI, finishPosJ);
        oFile << "\nMaximum achieavable number of points: " << maxPoints << endl;
        oFile << "\nThe moves you should take to win it:\n";
    }

    // Start do while loop and execute it until the game is over
    do
    {
        // Declare local variables necessary for the game
        char nextMoveHolder = 'l';                              // for holding the answer regarding the next move
        int leftPosI = currentPosI, leftPosJ = currentPosJ - 1; // for holding left move position
        int downPosI = currentPosI + 1, downPosJ = currentPosJ; // for holding down move position
        int leftPosValue, downPosValue;                         // for holding left and down move values

        // Create for loops for assigning values
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (i == leftPosI && j == leftPosJ)      // if element is to the left of the current position
                    leftPosValue = a[i][j];              // assign its value to left holder
                else if (i == downPosI && j == downPosJ) // if element is below the current position
                    downPosValue = a[i][j];              // assign its value to down holder
            }
        }

        // If current position is the same as the finish position
        if (currentPosI == finishPosI && currentPosJ == finishPosJ)
        {
            doWin = true; // change win state to true

            // Write relevant information into a file
            oFile << "\n======================================================\n";
            oFile << "\nThe game is won with " << iterator - 1 << " moves\n";
            oFile << "The total score is " << score << " points\n";
            break; // break out of loop
        }

        // Creating condition for calculating the next move
        if (finishPosJ == STARTING_POSITION_J)      // if finish point is at the same column as starting position
            nextMoveHolder = 'd';                   // next move will always be down
        else if (finishPosI == STARTING_POSITION_I) // if finish point is at the same row as starting position
            nextMoveHolder = 'l';                   // next move will always be left
        else
        {
            if (currentPosJ == finishPosJ)      // if current position is at the same column as finish point
                nextMoveHolder = 'd';           // next move is down
            else if (currentPosI == finishPosI) // if current position is at the same row as finish point
                nextMoveHolder = 'l';           // next move is left

            // If non of those are met, then choose the one with the most points
            else if (leftPosValue >= downPosValue) // if left position value is greater or equal to down position value
                nextMoveHolder = 'l';              // next move is left
            else
                nextMoveHolder = 'd'; // next move is down
        }

        // Create conditions for making a move

        // If calculated next move is to the left
        if (nextMoveHolder == 'l' || nextMoveHolder == 'L')
        {
            // Write a prompt with an answer
            oFile << iterator << ". Move left\n";

            // Add increments and move to the next iteration
            score += leftPosValue;
            currentPosJ -= 1;
            ++iterator;
            continue;
        }
        // In any other case
        else
        {
            // Write a prompt with an answer
            oFile << iterator << ". Move down\n";

            // Add increments and move to the next iteration
            score += downPosValue;
            currentPosI += 1;
            ++iterator;
            continue;
        }

    } while (!doWin);

    // Create condition to check if file opens properly
    if (oFile.good())
        cout << GREEN << "\nSuccessfully generated " << OUTPUT_FILENAME << ".\n"
             << UNGREEN;

    // Close file and end function execution
    oFile.close();
    return;
}

// For outputting the matrix to the console
void outputVector(int n, int m, vector<vector<int>> &a)
{
    // Create for loops for iterating over the matrix
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            // Output each element of the matrix
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    // End function execution
    return;
}

// For generating or entering the matrix from console
void fillVector(int n, int m, vector<vector<int>> &a)
{
    // Declare local variables
    int userDecision; // for storing user decision
    int element;      // for storing current element

    // Ask user would they like to generate or enter matrix
    cout << BOLD << "\nWould you like to enter or generate a matrix?\n"
         << UNBOLD;
    cout << "1. Enter matrix by yourself\n";
    cout << "2. Generate random matrix\n";
    cout << "Choice: ";
    cin >> userDecision;
    cout << endl;

    // Create for loop to iterate over the matrix and get each element
    for (int i = 0; i < n; i++)
    {
        vector<int> row; // for holding current row elements
        for (int j = 0; j < m; j++)
        {
            // If user chose to enter elements by themselves
            if (userDecision == 1)
            {
                // Ask user to enter a current element
                cout << "Enter element: ";
                cin >> element;
            }
            else
                // Generate a random element from 1 to 10
                element = rand() % 10;

            // Add current element into the row array
            row.push_back(element);
        }

        // Add row array to vector
        a.push_back(row);
    }

    // End function execution
    return;
}

// For reading matrix from a file
void fillVector(int n, int m, const string &FILENAME, vector<vector<int>> &a)
{
    // Declare local variables
    int element;                          // for storing current element
    fstream f(FILENAME.c_str(), ios::in); // for reading file

    // If file does not exist
    if (!f.is_open())
    {
        // Output error message
        cout << RED << "\nERROR: Could not open file " << FILENAME << endl
             << UNRED;
        return; // stop program execution
    }

    // Create for loop for getting each element of matrix from a file
    for (int i = 0; i < n; i++)
    {
        vector<int> row; // for holding current row elements
        for (int j = 0; j < m; j++)
        {
            // Read each element from file
            f >> element;

            // Add current element into a row array
            row.push_back(element);
        }

        // Add current row to vector
        a.push_back(row);
    }

    // Close file and end function execution
    f.close();
    return;
}

// for getting the maximum number of points from a field
int getMaxPoints(vector<vector<int>> &matrixVector, int i, int j)
{
    // declare base cases

    // check if the border of a matrix is reached
    if (j < 0 || i < 0)
        // if so return
        return 0;
    // check if the specified point is within a matrix field
    if (i >= matrixVector.size() || j >= matrixVector[0].size())
        // if not return
        return 0;

    // recursive call to determine the best path with a given point in both directions
    return matrixVector[i][j] + max(getMaxPoints(matrixVector, i - 1, j),
                                    getMaxPoints(matrixVector, i, j + 1));
}
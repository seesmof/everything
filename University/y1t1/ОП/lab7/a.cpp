// include necessary libraries
#include "../strings.h"
#include "../algorithms.h"

// declare struct for holding coordinates
struct Coordinate
{
    int I, J;
};

// function prototypes //
void fillVector(int, int, const string &, vector<vector<int>> &);
void fillVector(int, int, vector<vector<int>> &);
void outputVector(int, int, vector<vector<int>> &);
void bubbleSort(vector<vector<int>> &, const int, const int, int);
void performSort(vector<vector<int>> &, const int, const int);
void writeFile(vector<vector<int>> &, const int, const int, const string &);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    Coordinate matrixSize;
    vector<vector<int>> matrixVector;
    string inFileName, outFileName;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task A\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // ask user how they would like to get the matrix
        cout << "How would you like to get the matrix?\n";
        cout << "1. From command line\n";
        cout << "2. From file\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> userDecision;

        // prompt user to enter the number of rows and columns of the matrix
        cout << "\nEnter number of rows and columns in matrix (Rows Cols): ";
        cin >> matrixSize.I >> matrixSize.J;

        // if user chose to get matrix from command line
        if (userDecision == 1)
        {
            // Call a function to either manually fill in or randomly generate matrix
            fillVector(matrixSize.I, matrixSize.J, matrixVector);

            // Output the resulting matrix to the screen
            cout << "Your array is: \n";
            outputVector(matrixSize.I, matrixSize.J, matrixVector);
        }
        // if user chose to enter the matrix from file
        else if (userDecision == 2)
        {
            // ask user to enter file name using a corresponding function
            inFileName = getFileName();

            // Call a function to fill in the matrix from the input file
            fillVector(matrixSize.I, matrixSize.J, inFileName, matrixVector);

            // Output the matrix to the screen using a corresponding function
            cout << "Your array is: \n";
            outputVector(matrixSize.I, matrixSize.J, matrixVector);
        }
        // if user entered anything else
        else
            break; // stop program execution

        // call a function to sort out the matrix and output it
        performSort(matrixVector, matrixSize.I, matrixSize.J);

        // ask user to generate a result file
        cout << "\nWould you like to write the results into a file? (Y / N): ";
        cin >> doContinue;
        if (doContinue == 'y' || doContinue == 'Y')
        {
            outFileName = generateRandomString(6);
            writeFile(matrixVector, matrixSize.I, matrixSize.J, outFileName);
        }

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

// for writing the resulting matrix into a file
void writeFile(vector<vector<int>> &matrixVector, const int I, const int J, const string &OUT_FILE)
{
    fstream f(OUT_FILE.c_str(), ios::out); // for handling a file

    // check if file can be opened
    if (!f.is_open())
    {
        // if not stop the program and output the error
        cout << "\nERROR: Couldn't open file " << OUT_FILE << "\n";
        return;
    }
    else
    {
        // write relevant information
        f << "======================================================\n";
        f << "\t\t\tThank you for using this program\n";
        f << "======================================================\n";
        f << "\nYour sorted matrix:\n";

        // create for loops for outputting the matrix
        for (int i = 0; i < I; i++)
        {
            for (int j = 0; j < J; j++)
            {
                f << matrixVector[i][j] << " "; // output matrix element
            }
            f << endl;
        }
        f << "\n======================================================\n";

        cout << "\n"
             << OUT_FILE << " successfully generated\n";
    }

    // end function execution and close file
    f.close();
    return;
}

// for performing bubble sort
void bubbleSort(vector<vector<int>> &matrixVector, const int I, const int J, int order)
{
    // execute bubble sort algorithm
    for (int i = 0; i < I; i++)
        for (int j = 0; j < J; j++)
            for (int k = 0; k < J - 1; k++)
            {
                // check what order the user chose to sort the matrix
                if (order == 1)
                {
                    if (matrixVector[i][k] > matrixVector[i][k + 1])
                        swap(matrixVector[i][k], matrixVector[i][k + 1]);
                }
                else
                {
                    if (matrixVector[i][k] < matrixVector[i][k + 1])
                        swap(matrixVector[i][k], matrixVector[i][k + 1]);
                }
            }

    // stop function execution
    return;
}

// for sorting out the matrix in non-decreasing order
void performSort(vector<vector<int>> &matrixVector, const int I, const int J)
{
    // create for loop for getting each row's maximum value
    for (int i = 0; i < I; i++)
    {
        // declare variable for storing the maximum value of each row and set it to first element value
        int max = matrixVector[i][0];
        for (int j = 1; j < J; j++)
            if (matrixVector[i][j] > max)
                max = matrixVector[i][j];
    }

    // ask user in what order to sort the matrix rows
    int userDecision;
    cout << "\nWhat order would you like to sort the matrix in?\n";
    cout << "1. In a descending order (low to high)\n";
    cout << "2. In an ascending order (high to low)\n";
    cout << "3. Exit\n";
    cout << "Enter your choice: ";
    cin >> userDecision;

    // if user chose to exit, exit
    if (userDecision > 2)
        return;

    // call a function to perform a bubble sort
    bubbleSort(matrixVector, I, J, userDecision);

    // output the resulting matrix
    cout << "\nThe resulting matrix is\n";
    outputVector(I, J, matrixVector);

    // end function execution
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
    srand(time(NULL));

    // Ask user would they like to generate or enter matrix
    cout << "\nWould you like to enter or generate a matrix?\n";
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
        cout << "\nERROR: Could not open file " << FILENAME << endl;
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
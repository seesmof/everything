#include "../strings.h"
#include "../algorithms.h"

// function prototypes //
void measureRes(vector<char> &, vector<double> &, vector<long long> &);
void outRes(vector<long long> &);
void fillVector(vector<char> &, int);
void fillVector(vector<double> &, int);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    vector<char> charVector;
    vector<double> floatVector;
    vector<long long> timeVector;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task C\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // call function for getting results
        measureRes(charVector, floatVector, timeVector);

        // call function for outputting results
        outRes(timeVector);

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

// for outputting the results
void outRes(vector<long long> &timeVector)
{
    cout << "\nMaking some additional calculations...\n"; // output a message
    vector<long double> msVector;                         // for storing execution times converted into miliseconds

    // iterate through timeVector and convert each element of it
    for (int i = 0; i < timeVector.size(); i++)
    {
        // convert element to long double using static cast
        long double input = static_cast<long double>(timeVector[i]);
        // make that element a milisecond value
        long double element = input / 1000000;
        // add element to new vector
        msVector.push_back(element);
    }

    // declare for storing averages
    long double char10 = 0.0, float10 = 0.0, char50 = 0.0, float50 = 0.0;
    // iterate through new array and add each value to averages
    for (int j = 0; j < msVector.size(); j += 4)
    {
        char10 += msVector[j];
        float10 += msVector[j + 1];
        char50 += msVector[j + 2];
        float50 += msVector[j + 3];
    }
    // calculate average of each by dividing by the number of iterations
    char10 /= 5;
    float10 /= 5;
    char50 /= 5;
    float50 /= 5;

    // output a table with results
    cout << "\n-------------------------------------------------" << endl;
    cout << setw(10) << left << "Type"
         << " | " << setw(10) << left << "Data Set"
         << " | " << setw(10) << left << "Algorithm"
         << " | " << setw(10) << left << "Time" << endl;
    cout << "-------------------------------------------------" << endl;
    cout << setw(10) << left << "float"
         << " | " << setw(10) << left << "10"
         << " | " << setw(10) << left << "exchange"
         << " | " << setw(10) << left << float10 << endl;
    cout << "-------------------------------------------------" << endl;
    cout << setw(10) << left << ""
         << " | " << setw(10) << left << "50,000"
         << " | " << setw(10) << left << "merge"
         << " | " << setw(10) << left << float50 << endl;
    cout << "-------------------------------------------------" << endl;
    cout << setw(10) << left << "char"
         << " | " << setw(10) << left << "10"
         << " | " << setw(10) << left << "exchange"
         << " | " << setw(10) << left << char10 << endl;
    cout << "-------------------------------------------------" << endl;
    cout << setw(10) << left << ""
         << " | " << setw(10) << left << "50,000"
         << " | " << setw(10) << left << "merge"
         << " | " << setw(10) << left << char50 << endl;
    cout << "-------------------------------------------------" << endl;

    // output a note for clearer output
    cout << "\n* Type = data type used\n* Data Set = number of instances in a data set\n* Algorithm = sorting algorithm used\n* Time = average sorting time\n";

    // ask user to put table into a file
    char input;
    cout << "\nWould you like to output the results into a file? (Y | N): ";
    cin >> input;

    // if user agrees
    if (input == 'Y' || input == 'y')
    {
        // generate random file with random name
        string fname = generateRandomString(6);
        fstream f(fname.c_str(), ios::out);

        // check if file is not opening
        if (!f.is_open())
        {
            // output error and return
            cout << "\nERROR: Could not open file " << fname << endl;
            return;
        }

        // output necessary information to file
        f << "======================================================\n";
        f << "\t\t\tThank you for using this program\n";
        f << "======================================================\n";
        f << "\nYour resulting table\n";
        f << "\n-------------------------------------------------" << endl;
        f << setw(10) << left << "Type"
          << " | " << setw(10) << left << "Data Set"
          << " | " << setw(10) << left << "Algorithm"
          << " | " << setw(10) << left << "Time" << endl;
        f << "-------------------------------------------------" << endl;
        f << setw(10) << left << "float"
          << " | " << setw(10) << left << "10"
          << " | " << setw(10) << left << "exchange"
          << " | " << setw(10) << left << float10 << endl;
        f << "-------------------------------------------------" << endl;
        f << setw(10) << left << ""
          << " | " << setw(10) << left << "50,000"
          << " | " << setw(10) << left << "merge"
          << " | " << setw(10) << left << float50 << endl;
        f << "-------------------------------------------------" << endl;
        f << setw(10) << left << "char"
          << " | " << setw(10) << left << "10"
          << " | " << setw(10) << left << "exchange"
          << " | " << setw(10) << left << char10 << endl;
        f << "-------------------------------------------------" << endl;
        f << setw(10) << left << ""
          << " | " << setw(10) << left << "50,000"
          << " | " << setw(10) << left << "merge"
          << " | " << setw(10) << left << char50 << endl;
        f << "-------------------------------------------------" << endl;

        // output success message
        if (f.good())
            cout << "\nFile " << fname << " successfully generated.\n";

        // close file and return
        f.close();
        return;
    }
    // if user declines return
    else
        return;
}

// to measure performance of each algorithm on each data set
void measureRes(vector<char> &charVector, vector<double> &floatVector, vector<long long> &timeVector)
{
    cout << "\nMeasuring results...\n"; // output a message

    // for calculating the results
    for (int i = 0; i < 5; i++)
    {
        int n; // for holding number of elements
        // set to 10
        n = 10;
        // clear both vectors
        charVector.clear();
        floatVector.clear();
        // fill char and float vectors with random values
        fillVector(charVector, n);
        fillVector(floatVector, n);

        // start measuring algorithm execution time
        auto start = chrono::high_resolution_clock::now();
        // call a function to execute exchange sorting algorithm on char vector
        exchangeSort(charVector);
        // stop time measurment
        auto end = chrono::high_resolution_clock::now();
        // convert the measured time into nanoseconds
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        // add time into a vector
        timeVector.push_back(duration);

        // start measuring algorithm execution time
        start = chrono::high_resolution_clock::now();
        // call a function to execute exchange sorting algorithm on float vector
        exchangeSort(floatVector);
        // stop time measurment
        end = chrono::high_resolution_clock::now();
        // convert the measured time into nanoseconds
        duration = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        // add time into a vector
        timeVector.push_back(duration);

        // change data set to 50 000
        n = 50000;
        // clear both vectors
        charVector.clear();
        floatVector.clear();
        // fill in both vectors once again, but with a different number of elements
        fillVector(charVector, n);
        fillVector(floatVector, n);

        // start measuring algorithm execution time
        start = chrono::high_resolution_clock::now();
        // call a function to execute merge sorting algorithm on char vector
        mergeSort(charVector);
        // stop time measurment
        end = chrono::high_resolution_clock::now();
        // convert the measured time into nanoseconds
        duration = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        // add time into a vector
        timeVector.push_back(duration);

        // start measuring algorithm execution time
        start = chrono::high_resolution_clock::now();
        // call a function to execute merge sorting algorithm on float vector
        mergeSort(floatVector);
        // stop time measurment
        end = chrono::high_resolution_clock::now();
        // convert the measured time into nanoseconds
        duration = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        // add time into a vector
        timeVector.push_back(duration);
    }
}

// to fill the array with random numbers
void fillVector(vector<char> &arr, int size)
{
    // fill the vector with random numbers
    for (int i = 0; i < size; i++)
    {
        // generate a random number between 48 and 57 (inclusive)
        // 48 and 57 are the ASCII codes for 0 and 9 respectively
        int randomNumber = rand() % (57 - 48 + 1) + 48;
        arr.push_back(static_cast<char>(randomNumber));
    }
}

// to fill the array with random numbers
void fillVector(vector<double> &arr, int size)
{
    // fill the vector with random numbers
    for (int i = 0; i < size; i++)
    {
        int element = rand() % 10;
        arr.push_back(element);
    }
}
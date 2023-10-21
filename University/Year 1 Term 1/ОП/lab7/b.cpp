// include necessary libraries
#include "../strings.h"
#include "../algorithms.h"

// declare struct for processing student's name
struct Name
{
    string P, I, B;
};

// declare struct for processing student's information
struct Student
{
    Name name;
    vector<int> score;
    string university;
    string specialty;
    int avgScore;
};

// function prototypes //
int fillData(vector<Student> &, const string &, vector<string> &, vector<int> &);
void fillData(vector<Student> &, int, vector<string> &, vector<int> &);
void outStudents(vector<Student> &);
void getPlaces(vector<pair<string, int>> &);
void exchangeSort(vector<pair<string, int>> &);
void outRes(vector<pair<string, int>> &, vector<Student> &);
void exchangeSort(vector<Student> &);
/////////////////////////

// func main start
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    int userDecision;
    string inFileName, outFileName;
    vector<Student> studentVector;
    vector<pair<string, int>> placesVector;
    vector<string> universityVector;
    int numOfStud;
    /////////////////////////////

    // project intro
    cout << "\n/////////////////////////////////////////////////////////////\n"
         << "\nWelcome! This is task B\n"
         << "\n/////////////////////////////////////////////////////////////\n\n";
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // ask user how would they like to enter student information
        cout << "How would you like to enter students' data?\n";
        cout << "1. From command line\n";
        cout << "2. From file\n";
        cout << "3. Exit\n";
        cout << "Enter your choise: ";
        cin >> userDecision;
        cout << endl;

        // if chose to enter from command line
        if (userDecision == 1)
        {
            // ask the number of students
            int numOfStud;
            cout << "Enter a number of students you would like to enter: ";
            cin >> numOfStud;

            // fill in the student vector calling a corresponding function
            fillData(studentVector, numOfStud, universityVector);
        }
        // if chose to enter from file
        else if (userDecision == 2)
        {
            // get input file name by calling a corresponding function
            inFileName = getFileName();

            // get number of students and fill in the student vector by calling the corresponding function
            numOfStud = fillData(studentVector, inFileName, universityVector);
        }
        else
            break;

        // output all the students
        cout << "All the applicable students are listed below\n";
        outStudents(studentVector);

        // get only unique universities by calling a corresponding function
        universityVector = getUniqueVector(universityVector);
        // iterate throught university vector
        for (int i = 0; i < universityVector.size(); i++)
            // form pairs for places vector with universities and number of places, set 0 as default
            placesVector.push_back(make_pair(universityVector[i], 0));

        // get the number of places by calling a corresponding function
        getPlaces(placesVector);

        // sort out the students vector by calling the corresponding function
        exchangeSort(studentVector);

        // output the results of a competition by callign the corresponding function
        outRes(placesVector, studentVector);

        //////////////////////////////////////////////////////////////////////////////////
        cout << "/////////////////////////////////////////////////////////////\n"
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

// function that implements an exchange sort to a student vector
void exchangeSort(vector<Student> &studentVector)
{
    // declare size variable
    int size = studentVector.size();
    // implement exchange sort in ascending order based on average score
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (studentVector[i].avgScore < studentVector[j].avgScore)
            {
                swap(studentVector[i], studentVector[j]);
            }
        }
    }
}

// for outputting the results of a competition
void outRes(vector<pair<string, int>> &placesVector, vector<Student> &studentVector)
{
    // output corresponding message
    cout << "\nThe results of the competition are shown below\n\n";
    // for all univesities
    for (int i = 0; i < placesVector.size(); i++)
    {
        // declare string for easier access
        string uniHolder = placesVector[i].first;
        // for each student
        for (int j = 0, k = 0; j < studentVector.size(); j++)
        {
            // check if student's university corresponds with the one in holder
            if (studentVector[j].university == uniHolder)
            {
                // check if it was outputted more or equal times than the nubmer of places
                if (k >= placesVector[i].second)
                    continue;
                // if not
                else
                {
                    // output student's data
                    cout << "(" << uniHolder << ") " << studentVector[j].name.P << " " << studentVector[j].name.I << " " << studentVector[j].name.B << " * " << studentVector[j].avgScore << endl;
                    k++;
                }
            }
        }
        cout << endl;
    }

    // end function execution
    return;
}

// for getting user input on university places
void getPlaces(vector<pair<string, int>> &placesVector)
{
    // declare local variables
    int numOfUnis = placesVector.size();
    cout << endl;

    // get number of places for each university
    for (int i = 0; i < numOfUnis; ++i)
    {
        // ask user to enter number of places
        cout << "Enter the number of places for " << placesVector[i].first << " university\n";
        cout << "Input: ";
        cin >> placesVector[i].second;
        cout << endl;
    }

    // end functino execution
    return;
}

// for outputting students information from student vector
void outStudents(vector<Student> &studentVector)
{
    // declare local variables
    cout << endl;
    int numOfStud = studentVector.size();

    // output info of each student
    for (int i = 0; i < numOfStud; ++i)
    {
        cout << "(" << i + 1 << ") " << studentVector[i].name.P << " " << studentVector[i].name.I << " " << studentVector[i].name.B << " * " << studentVector[i].avgScore << endl;
        cout << "    " << studentVector[i].university << " * " << studentVector[i].specialty << endl;
    }

    // end function execution
    return;
}

// to fill in the student vector with data from the command line
void fillData(vector<Student> &studentVector, int numOfStud, vector<string> &universityVector)
{
    // loop through the number of students
    for (int i = 0; i < numOfStud; i++)
    {
        // declare an instance of struct
        Student obj;

        // ask user to enter student's full name and validate it
        cout << "\nEnter student's full name: ";
        cin >> obj.name.P >> obj.name.I >> obj.name.B;
        if (islower(obj.name.P[0]))
            obj.name.P[0] = toupper(obj.name.P[0]);
        if (islower(obj.name.I[0]))
            obj.name.I[0] = toupper(obj.name.I[0]);
        if (islower(obj.name.B[0]))
            obj.name.B[0] = toupper(obj.name.B[0]);

        // ask user to enter student's score and add them to object
        int score1, score2, score3;
        cout << "Enter student's score: ";
        cin >> score1 >> score2 >> score3;
        obj.score.push_back(score1);
        obj.score.push_back(score2);
        obj.score.push_back(score3);

        // ask user to enter student's university and add it to university vector
        cout << "Enter student's university: ";
        cin >> obj.university;
        universityVector.push_back(obj.university);

        // ask user to enter student's specialty
        cout << "Enter student's specialty: ";
        cin >> obj.specialty;

        // calculate student's average score
        obj.avgScore = (score1 + score2 + score3) / 3;

        // add object to students vector
        studentVector.push_back(obj);
    }

    // end function execution
    return;
}

// for filling in the students vector with data from file
int fillData(vector<Student> &studentVector, const string &IN_FILE, vector<string> &universityVector)
{
    // declare local variables
    fstream inFile(IN_FILE.c_str(), ios::in);
    string lineReader;
    int numOfStud = 1;
    vector<string> linesHolder;

    // check if file can be opened
    if (!inFile.is_open())
    {
        // if not output error and return
        cout << "\nERROR: Couldn't open file " << IN_FILE << endl;
        return -1;
    }

    // read every line from the file
    while (getline(inFile, lineReader))
    {
        // when found empty line increase line number
        if (lineReader.empty())
            numOfStud++;
        // in other cases add the line into a vector
        else
            linesHolder.push_back(lineReader);
    }

    // create a loop for sorting out each line and placing them into a correct spot
    for (int i = 0, j = 0; i < numOfStud; i++, j += 8)
    {
        // create instance of struct in vector
        studentVector.push_back(Student());

        // fill out all the data from file
        studentVector[i].name.P = linesHolder[j];
        studentVector[i].name.I = linesHolder[j + 1];
        studentVector[i].name.B = linesHolder[j + 2];
        studentVector[i].score.push_back(stoi(linesHolder[j + 3]));
        studentVector[i].score.push_back(stoi(linesHolder[j + 4]));
        studentVector[i].score.push_back(stoi(linesHolder[j + 5]));
        studentVector[i].university = linesHolder[j + 6];
        studentVector[i].specialty = linesHolder[j + 7];
        studentVector[i].avgScore = (stoi(linesHolder[j + 3]) + stoi(linesHolder[j + 4]) + stoi(linesHolder[j + 5])) / 3;

        // add student's university into a university vector
        universityVector.push_back(studentVector[i].university);
    }

    // end function
    return numOfStud;
}
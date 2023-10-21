// include necessary libraries
#include <iostream>
#include <string>
using namespace std;

// create a structure to hold the semi truck's information
struct futureStudent
{
     // declare variables for storing Прізвище Ім'я По-батькові
     string P;
     string I;
     string B;
     // declare variable for storing age
     int age;
     // declare variable for storing school GPA
     double schoolGPA;
     // declare variables for storing NMT results and additional scores
     int resultNMT[3];
     double additionalScore;
     // declare variable for storing whether the student has originals of documents
     bool hasOriginalDocs;
     // declare variables for storing university name and specialization
     string universityName;
     string specialization;
     // declare variables for storing total and average NMT scores
     double totalNMTscore;
     double averageNMTscore;
};

// declare function prototypes
void studentInput(int n, futureStudent *student);
void studentSearch(int n, futureStudent *student);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << "****************************** Task B *************************************" << endl
          << endl;

     // ask user to enter the amount of students
     int n;
     cout << "Enter the amount of students you want to enter: ";
     cin >> n;

     // declare 1d array with students' information of N size
     futureStudent student[n];

     // call a function for students' data input
     studentInput(n, student);

     // call a function for students' search
     studentSearch(n, student);

     // declare confirmation char variable
     char confirmation;

     // ask user whether he would like to make any changes to earlier inputted data
     cout << endl
          << "Would you like to make any changes to any of the students? (Y / N): ";
     cin >> confirmation;

     // if the answer was yes => execute following function
     if (confirmation == 'y' || confirmation == 'Y')
     {
          // declare variable for students search
          int i = 0;

          // ask user to input a number of student that he wants to edit
          cout << "Pick a student by number (M): ";
          cin >> i;
          i -= 1;

          // declare variable for storing user input
          int choice;

          // ask user to choose an option to change
          cout << endl;
          cout << "What parameter you would like to change?" << endl;
          cout << "1. Age" << endl;
          cout << "2. School GPA" << endl;
          cout << "3. NMT Result" << endl;
          cout << "4. University" << endl;
          cout << "5. Specialization" << endl;
          cout << "Input: ";
          cin >> choice;

          // start a switch statement with all of the parameters above
          cout << endl;
          switch (choice)
          {
          // if age is chosen => execute the following statement
          case 1:
          {
               cout << "Enter an age: ";
               cin >> student[i].age;
               cout << "Congratulations! The change was successful made." << endl;
               break;
          }
          // if school GPA is chosen => execute the following statement
          case 2:
          {
               cout << "Enter a school GPA: ";
               cin >> student[i].schoolGPA;
               cout << "Congratulations! The change was successful made." << endl;
               break;
          }
          // if NMT result is chosen => execute the following statement
          case 3:
          {
               cout << "Enter a NMT result: ";
               cin >> student[i].resultNMT[0] >> student[i].resultNMT[1] >> student[i].resultNMT[2];
               cout << "Congratulations! The change was successful made." << endl;
               break;
          }
          // if university is chosen => execute the following statement
          case 4:
          {
               cout << "Enter a university: ";
               cin >> student[i].universityName;
               cout << "Congratulations! The change was successful made." << endl;
               break;
          }
          // if specialization is chosen => execute the following statement
          case 5:
          {
               cout << "Enter a specialization: ";
               cin >> student[i].specialization;
               cout << "Congratulations! The change was successful made." << endl;
               break;
          }
          // add an exception if none of the above statements were executed
          default:
          {
               break;
          }
          }

          // call a function for student search
          studentSearch(n, student);
     }

     // output project outro
     cout << endl
          << "***************************************************************************" << endl;

     // end main function
     return 0;
}

// create a function for student search
void studentSearch(int n, futureStudent *student)
{
     // declare local variable for storing the user input
     string input;

     // ask user to input the student's last name
     cout << endl;
     cout << "Enter student's last name: ";
     cin >> input;

     // create a function for changing the first letter of the student's last name to uppercase if it was inputted using lowercase
     if (islower(input[0]))
     {
          input[0] = toupper(input[0]);
     }
     // create a counter for storing the amount of search results
     int resultCount = 0;
     // create a for loop to loop through the student's array
     for (int i = 0; i < n; i++)
     {
          // if inputted last name == last name of current iteration => execute the following code
          if (input == student[i].P)
          {
               // declare a variable for displaying the result number
               int subCount = 0;
               // ouput student's ПІБ
               cout << i + 1 << "." << subCount << " " << student[i].P << " " << student[i].I << " " << student[i].B << endl;
               subCount++;
               // output student's age
               cout << i + 1 << "." << subCount << " Age - " << student[i].age << endl;
               subCount++;
               // output student's average GPA
               cout << i + 1 << "." << subCount << " Average school mark - " << student[i].schoolGPA << endl;
               subCount++;
               // output student's average NMT score
               cout << i + 1 << "." << subCount << " Average NMT score - " << student[i].averageNMTscore << endl;
               subCount++;
               // output student's university
               cout << i + 1 << "." << subCount << " University - " << student[i].universityName << endl;
               subCount++;
               // output student's specialization
               cout << i + 1 << "." << subCount << " Specialization - " << student[i].specialization << endl;
               // increment result counter
               resultCount++;
          }
     }
     // if result counter is still at 0
     if (resultCount == 0)
     {
          // output error message
          cout << "Unfortunately, there are no students with last name " << input << ". Try again with a different name." << endl;
     }
     // end function
     return;
}

// create function that will ask user to input information for each of the vehicles
void studentInput(int n, futureStudent *student)
{
     // create a local variable for storing user's answer to yes/no questions
     char confirmation;
     // create for loop for looping through an array and asking user to input each student's data
     for (int i = 0; i < n; i++)
     {
          // declare local variable for storing the result number
          int subCount = 1;

          // ask user to enter student's ПІБ
          cout << endl;
          cout << i + 1 << "." << subCount << " Enter student's PIB: ";
          cin >> (student + i)->P >> student[i].I >> student[i].B;
          // create 3 functions for converting first lowercase letters of students name to uppercase
          if (islower(student[i].P[0]))
          {
               student[i].P[0] = toupper(student[i].P[0]);
          }
          if (islower(student[i].I[0]))
          {
               student[i].I[0] = toupper(student[i].I[0]);
          }
          if (islower(student[i].B[0]))
          {
               student[i].B[0] = toupper(student[i].B[0]);
          }
          subCount++;

          // ask user to enter student's age
          cout << i + 1 << "." << subCount << " Enter student's age: ";
          cin >> student[i].age;
          subCount++;

          // ask user to enter student's school GPA
          cout << i + 1 << "." << subCount << " Enter student's school GPA: ";
          cin >> student[i].schoolGPA;
          subCount++;

          // ask user to enter student's NMT results
          cout << i + 1 << "." << subCount << " Enter student's NMT results (1 2 3): ";
          cin >> student[i].resultNMT[0] >> student[i].resultNMT[1] >> student[i].resultNMT[2];
          subCount++;

          // ask user to enter student's additional scores
          cout << i + 1 << "." << subCount << " Enter student's additional scores: ";
          cin >> student[i].additionalScore;
          subCount++;

          // ask user to enter if student has originals of documents or not
          cout << i + 1 << "." << subCount << " Does the student has the originals of all the documents? (Y / N): ";
          cin >> confirmation;
          // if the input == Y
          if (confirmation == 'y' || confirmation == 'Y')
          {
               // assign true value
               student[i].hasOriginalDocs = true;
          }
          // in any other cases
          else
          {
               // assign false value
               student[i].hasOriginalDocs = false;
          }
          subCount++;

          // ask user to enter student's university
          cout << i + 1 << "." << subCount << " Enter university this student will be going to: ";
          cin >> student[i].universityName;
          subCount++;

          // ask user to enter student's specialization
          cout << i + 1 << "." << subCount << " Enter the future specialization of the student: ";
          cin >> student[i].specialization;

          // calculate total NMT score by combining three inputted NMT results and multiply them by additional score
          student[i].totalNMTscore = (student[i].resultNMT[0] + student[i].resultNMT[1] + student[i].resultNMT[2]) * student[i].additionalScore;
          // calculate average NMT score by dividing the total score by the amount of scores, 3 in our case
          student[i].averageNMTscore = student[i].totalNMTscore / 3;

          // output student's total and average scores
          cout << student[i].I << " has a total score of " << student[i].totalNMTscore << " and an average score of " << student[i].averageNMTscore << "." << endl;

          // create a function for calculating the amount of students who have the same university and specialization inputted
          // declare local variable for storing student count
          int studentCount = 0;
          // declare variable for storing global average score
          double globalAvgScore = 0.0;
          // create for loop for iterating through an array
          for (int j = 0; j < n; j++)
          {
               // if we are on the first iteration
               if (i == 0)
               {
                    // skip iteration
                    continue;
               }
               // in any other cases
               else
               {
                    // if we are on the same iteration as we just inputed
                    if (j == i)
                    {
                         // skip iteration
                         continue;
                    }
                    // in any other cases
                    else
                    {
                         // if students' univesities and specialization match
                         if (student[i].universityName == student[j].universityName && student[i].specialization == student[j].specialization)
                         {
                              // increase counter
                              studentCount++;
                              // add this student's NMT score to global average
                              globalAvgScore += student[j].averageNMTscore;
                         }
                    }
               }
          }
          // divide global average score by student count to get the average
          globalAvgScore /= studentCount;

          // if student count > 0
          if (studentCount > 0)
          {
               // output the amount of students found
               cout << endl;
               cout << "There are " << studentCount << " students who are going to the same University." << endl;
               // and their average score
               cout << "Their average score is " << globalAvgScore << endl;
          }
     }
     // end function
     return;
}
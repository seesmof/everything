// include necessary libraries
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

// declare global variables
const double PI = 3.14159;
const double E = 2.71828;
vector<double> X;
double G = 0.0;

// declare function prototype
void resultCalc(int n);

// declare main function
int main(int argc, char **argv)
{
     // output program intro
     cout << "****************************** Task C *************************************" << endl
          << endl;

     // create int variable for holding matrix size
     int n;
     // ask user for matrix size
     cout << "Enter the matrix size (N): ";
     cin >> n;
     // declare matrix and assign it a size inputted from user
     double input[n][n];

     // output matrix to user
     cout << endl
          << "Your matrix is: " << endl;
     for (int i = 0; i < n; i++)
     {
          for (int j = 0; j < n; j++)
          {
               // apply formula given in the task description
               input[i][j] = pow(2, (i + j - 1)) * exp(2 * i - j) - pow((PI / E), (i - j)) * log10(exp((j + 5) / (i + 1)));
               // output matrix element of current iteration to user
               cout << input[i][j] << " ";
          }
          cout << endl;
     }

     // create for loop that will look for smallest elements in each col
     for (int i = 0; i < n; i++)
     {
          // declare variable for holding current col's minimum value
          double minFromCol = 200;
          for (int j = 0; j < n; j++)
          {
               // if element of current iteration is less than current col's minimum value
               if (abs(input[j][i]) < minFromCol)
               {
                    // assign its value to minFromCol
                    minFromCol = abs(input[j][i]);
               }
          }
          // add a final value from col to X vector
          X.push_back(minFromCol);
     }

     // output vector X to user
     cout << endl
          << "Minimal values of each column are: " << endl;
     for (int i = 0, vecSize = X.size(); i < vecSize; i++)
     {
          cout << X[i] << " ";
     }

     // output G value to user
     resultCalc(n);
     G = sqrt(abs(G));
     cout << endl
          << endl
          << "G value is " << G << endl;

     // output project outro
     cout << endl
          << "***************************************************************************" << endl
          << endl;

     // end main function
     return 0;
}

// create function for applying G formula from task description
void resultCalc(int n)
{
     // declare local variable for storing P value
     double pHolder;
     // create for loop for calculating Σ value
     for (int q = 1; q < n; q++)
     {
          // create for loop for calculating P value
          for (int k = 1; k < q; k++)
          {
               // add P value to pHolder variable
               pHolder *= X[k] / E;
          }
          // add Σ value to G
          G += X[q] + pHolder;
     }
     // end function
     return;
}
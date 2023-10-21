// include necessary libraries
#include <iostream>
using namespace std;

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << endl;
    cout << "************************* Task D ********************************" << endl
         << endl;

    // ask user to input array size
    int n, m;
    cout << "Enter matrix size (n * m): ";
    cin >> n >> m;
    cout << endl;

    int matrixA[n][m];
    int matrixB[n][m];
    srand(time(NULL));

    // create function to fill and output array
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            matrixA[i][j] = rand() % 10;
            cout << matrixA[i][j] << " ";
            matrixB[j][i] = matrixA[i][j];
        }
        cout << endl;
    }
    cout << endl;

    // create function to output a result matrix
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << matrixB[i][j] << " ";
        }
        cout << endl;
    }

    // output program outro
    cout << endl;
    cout << "*****************************************************************" << endl;

    // end main function
    return 0;
}
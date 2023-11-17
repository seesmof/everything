// include necessary libraries
#include <bits/stdc++.h>
#include "lib.h"
using namespace std;

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define pb push_back
#define mp make_pair
#define ull unsigned long long
#define endl "\n"

// implements the Quick Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void quickSort(vector<T> &arr, int left, int right)
{
    int i = left, j = right;             // initialize two variables, i and j, to the values of left and right respectively.
    int pivot = arr[(left + right) / 2]; // find the pivot element by taking the average of the left and right

    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    // iterate through the values of i and j
    while (i <= j)
    {
        // iterate through the array until finds an element that is greater than the pivot value
        while (arr[i] > pivot)
            i++; // increment i
        // iterate through the array until finds an element that is less than the pivot value
        while (arr[j] < pivot)
            j--; // decrement j

        // check if the value of i is <= j.
        if (i <= j)
        {
            // swap the values of arr[i] and arr[j], then increment i and decrement j
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    };

    // recursively sort the left part of the array
    if (left < j)
        quickSort(arr, left, j);
    // recursively sort the right part of the array
    if (i < right)
        quickSort(arr, i, right);
}

// implements the Exchange Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void exchangeSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size() - 1; i++)
        for (int j = i + 1; j < arr.size(); j++)
            if (arr[i] < arr[j])
                swap(arr[i], arr[j]);
}

// implements the Bubble Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void bubbleSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size(); i++)
        for (int j = 0; j < arr.size() - i - 1; j++)
            if (arr[j] < arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

// implements the Merge Sort algorithm to sort the elements of the given vector in ascending order
template <typename T>
void mergeSort(vector<T> &arr)
{
    // check if size of array is <= 1, if so stop function
    if (arr.size() <= 1)
        return;

    vector<int> left, right;     // for partitioning the array
    int middle = arr.size() / 2; // calculate the middle index of the array

    // iterate through the array from start to middle and add each element to left vector
    for (int i = 0; i < middle; i++)
        left.push_back(arr[i]);
    // iterate through the array from middle to end and add each element to right vector
    for (int i = middle; i < arr.size(); i++)
        right.push_back(arr[i]);

    // recursively sort left and right vectors
    mergeSort(left);
    mergeSort(right);

    int i = 0, j = 0, k = 0; // declare indeces

    // iterate through the left and right vectors until the end of either vector
    while (i < left.size() && j < right.size())
    {
        if (left[i] > right[j])
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // merge left and input vectors
    while (i < left.size())
    {
        arr[k] = left[i];
        i++;
        k++;
    }

    // merge right and input vectors
    while (j < right.size())
    {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// to output one dimensional vector
template <typename T>
void outputArray(vector<T> arr)
{
    for (auto i : arr)
        cout << i << " ";
    cout << endl;
}

// to output one dimensional array
void outputArray(int *arr)
{
    int n = sizeof(arr) / sizeof(int);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// to output two dimensional vector
template <typename T>
void outputArray(vector<vector<T>> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << arr[i][j] << " ";
        cout << "\n";
    }
}

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
vector<string> getUniqueVector(vector<string> &inputVector)
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

// For changing text color to gray
ostream &GRAY(ostream &os)
{
    return os << "\033[1;30m";
}

// For changing text back to normal
ostream &UNGRAY(ostream &os)
{
    return os << "\033[0m";
}

// For changing text color to yellow
ostream &YELLOW(ostream &os)
{
    return os << "\033[1;33m";
}

// For changing text back to normal
ostream &UNYELLOW(ostream &os)
{
    return os << "\033[0m";
}
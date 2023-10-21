#include <bits/stdc++.h>
#include "lib.h"
using namespace std;

#define ll long long
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define endl "\n"
void dbg_out()
{
    cerr << endl;
}
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T)
{
    cerr << ' ' << H;
    dbg_out(T...);
}
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

void bad(const string &INPUT)
{
    stringstream ss;
    ss << "\033[1;31mERROR: " << INPUT << "\033[0m";
    cerr << ss.str() << endl;
}

void good(const string &INPUT)
{
    stringstream ss;
    ss << "\033[1;32mSUCCESS: " << INPUT << "\033[0m";
    cerr << ss.str() << endl;
}

ll getNum()
{
    ll number;
    while (!(cin >> number))
    {
        cin.clear();
        cin.ignore(256, '\n');
        cout << endl;
        bad("Enter an integer");
        cout << endl;
    }
    return number;
}

ostream &BOLD(ostream &os)
{
    return os << "\e[1m";
}
ostream &UNBOLD(ostream &os)
{
    return os << "\e[0m";
}

ostream &RED(ostream &os)
{
    return os << "\033[1;31m";
}
ostream &UNRED(ostream &os)
{
    return os << "\033[0m";
}

ostream &GREEN(ostream &os)
{
    return os << "\033[1;32m";
}
ostream &UNGREEN(ostream &os)
{
    return os << "\033[0m";
}

ostream &GRAY(ostream &os)
{
    return os << "\033[1;30m";
}
ostream &UNGRAY(ostream &os)
{
    return os << "\033[0m";
}

ostream &YELLOW(ostream &os)
{
    return os << "\033[1;33m";
}
ostream &UNYELLOW(ostream &os)
{
    return os << "\033[0m";
}

ll showMenu(const vector<string> &MENU_OPTIONS)
{
    cout << BOLD << "Choose one option from the menu below\n"
         << UNBOLD;
    for (ll i = 0; i < MENU_OPTIONS.size(); i++)
    {
        cout << i + 1 << ". " << MENU_OPTIONS[i] << endl;
    }
    cout << "Enter your choice: ";
    ll userDecision = getNum();
    cout << endl;
    return userDecision;
}

string validateName(string inputString)
{
    stringstream stringProcessor(inputString);
    string wordHolder;
    string resultHolder;
    while (stringProcessor >> wordHolder)
    {
        if (!isupper(wordHolder[0]))
        {
            wordHolder[0] = toupper(wordHolder[0]);
        }
        resultHolder += wordHolder + " ";
    }
    return resultHolder;
}

string getEmailAddress()
{
    string emailAddress;
    cout << "Please enter an email address: ";
    cin >> emailAddress;
    if (emailAddress.find("@") == string::npos)
    {
        cout << "\nERROR: Invalid email address\n\n";
        getEmailAddress();
    }
    else
        return emailAddress;
    return "";
}

string getFileName()
{
    string fileName = "";
    bool isExtensionFound = true;
    do
    {
        cout << "Enter file name: ";
        cin >> fileName;

        if (fileName.find(".") == string::npos)
        {
            isExtensionFound = false;
            cout << "\nERROR: File extension not found. Try again...\n\n";
            continue;
        }
        else
            break;
    } while (isExtensionFound == false);
    return fileName;
}

string generateRandomString(int length)
{
    string chars = "abcdefghijklmnopqrstuvwxy";
    string randomString = "";
    for (int i = 0; i < length; i++)
    {
        int index = rand() % chars.size();
        randomString += chars[index];
    }
    return randomString;
}

string generateRandomPassword(int length)
{
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxy1234567890!@#$%^&*()_+=-[]{}`~';/.,";
    string randomPass = "";
    for (int i = 0; i < length; i++)
    {
        int index = rand() % chars.size();
        randomPass += chars[index];
    }
    return randomPass;
}

template <typename T>
vector<T> getUniqueVector(vector<T> &inputVector)
{
    vector<T> uniqueElements;
    unordered_set<T> seenElements;
    for (T element : inputVector)
    {
        if (seenElements.find(element) == seenElements.end())
        {
            uniqueElements.push_back(element);
            seenElements.insert(element);
        }
    }
    return uniqueElements;
}

template <typename T>
void quickSort(vector<T> &arr, int left, int right)
{
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];

    if (arr.size() <= 1)
        return;

    while (i <= j)
    {
        while (arr[i] > pivot)
            i++;
        while (arr[j] < pivot)
            j--;

        if (i <= j)
        {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    };

    if (left < j)
        quickSort(arr, left, j);
    if (i < right)
        quickSort(arr, i, right);
}

template <typename T>
void exchangeSort(vector<T> &arr)
{
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size() - 1; i++)
        for (int j = i + 1; j < arr.size(); j++)
            if (arr[i] < arr[j])
                swap(arr[i], arr[j]);
}

template <typename T>
void bubbleSort(vector<T> &arr)
{
    if (arr.size() <= 1)
        return;

    for (int i = 0; i < arr.size(); i++)
        for (int j = 0; j < arr.size() - i - 1; j++)
            if (arr[j] < arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

template <typename T>
void mergeSort(vector<T> &arr)
{
    if (arr.size() <= 1)
        return;

    vector<int> left, right;
    int middle = arr.size() / 2;

    for (int i = 0; i < middle; i++)
        left.push_back(arr[i]);
    for (int i = middle; i < arr.size(); i++)
        right.push_back(arr[i]);

    mergeSort(left);
    mergeSort(right);

    int i = 0, j = 0, k = 0;

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

    while (i < left.size())
    {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < right.size())
    {
        arr[k] = right[j];
        j++;
        k++;
    }
}

template <typename T>
void outputArray(vector<T> arr)
{
    for (auto i : arr)
        cout << i << " ";
    cout << endl;
}

void outputArray(int *arr)
{
    int n = sizeof(arr) / sizeof(int);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

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

string toLower(string str)
{
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

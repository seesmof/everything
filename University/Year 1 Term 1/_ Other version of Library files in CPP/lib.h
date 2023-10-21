#pragma once
#include <bits/stdc++.h>
#include "lib.cpp"
using namespace std;

ll showMenu(const vector<string> &menuOptions);

string toLower(string str);

void bad(const string &INPUT);

void good(const string &INPUT);

ll getNum();

string validateName(string inputString);

template <typename T>
void quickSort(vector<T> &arr, int left, int right);

template <typename T>
void exchangeSort(vector<T> &arr);

template <typename T>
void bubbleSort(vector<T> &arr);

template <typename T>
void mergeSort(vector<T> &arr);

template <typename T>
void outputArray(vector<T> arr);

void outputArray(int *arr);

void outputArray(vector<vector<int>> &arr);

string getEmailAddress();

string getFileName();

string generateRandomString(int length);

string generateRandomPassword(int length);

template <typename T>
vector<T> getUniqueVector(vector<T> &inputVector);

ostream &BOLD(ostream &os);

ostream &UNBOLD(ostream &os);

ostream &RED(ostream &os);

ostream &UNRED(ostream &os);

ostream &GREEN(ostream &os);

ostream &UNGREEN(ostream &os);

ostream &GRAY(ostream &os);

ostream &UNGRAY(ostream &os);

ostream &YELLOW(ostream &os);

ostream &UNYELLOW(ostream &os);
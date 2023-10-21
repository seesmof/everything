#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"
using namespace std;

// delta class declaration
template <typename T>
class Delta;

// object deletion function
template <typename T>
void createObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector);

// object creation function
template <typename T>
void printObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector);

// printing objects function
template <typename T>
void deleteObjects(vector<unique_ptr<Delta<T>>> &deltaObjectsVector);

// for showing the main menu of the application
template <typename T>
void outputMenu(vector<unique_ptr<Delta<T>>> &deltaObjectsVector);
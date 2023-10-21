#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"

class DynamicString;

// for showing the main menu of the application
void outputMenu(vector<DynamicString> &container);

// define an output stream operator function
ostream &operator<<(ostream &outputStream, const DynamicString &OUTPUT);

// define an input stream operator function
istream &operator>>(istream &inputStream, DynamicString &inputHolder);

// define an output stream operator function for file
ofstream &operator<<(ofstream &outputStream, const DynamicString &OUTPUT);

// define an input stream operator function for file
ifstream &operator>>(ifstream &inputStream, DynamicString &inputHolder);

#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"

class DynamicString;
void showStrings(vector<DynamicString> &container);
void showStrings(vector<DynamicString> &container, const string &FILE);
void addStrings(vector<DynamicString> &container);
void addStrings(vector<DynamicString> &container, const string &FILE);
void removeString(vector<DynamicString> &container);
void outputMenu(vector<DynamicString> &container);
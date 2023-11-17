#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"

class DynamicString;

void showStrings(vector<unique_ptr<DynamicString>> &container);

void addStrings(vector<unique_ptr<DynamicString>> &container);

void removeString(vector<unique_ptr<DynamicString>> &container);

void outputMenu(vector<unique_ptr<DynamicString>> &container);
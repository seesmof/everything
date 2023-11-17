#pragma once
#include "sup.cpp"
#include "D:\repos\university\lib.h"

class Delta;
void showObjs(vector<unique_ptr<Delta>> &container);
void addObjs(vector<unique_ptr<Delta>> &container);
void delObjs(vector<unique_ptr<Delta>> &container);
void outputMenu(vector<unique_ptr<Delta>> &container);
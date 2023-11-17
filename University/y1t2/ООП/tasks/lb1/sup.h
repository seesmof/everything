#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../../lib.h"
using namespace std;

// delta class declaration
class Delta;

// object deletion function
void deleteObjects(vector<unique_ptr<Delta>> &deltaObjectsVector);

// object creation function
void createObjects(vector<unique_ptr<Delta>> &deltaObjectsVector);

// printing objects function
void printObjects(vector<unique_ptr<Delta>> &deltaObjectsVector);

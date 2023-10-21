#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../../lib.h"
using namespace std;

class Human;
class Engineer;

void showPeople(vector<unique_ptr<Human>> &container);

void addPeople(vector<unique_ptr<Human>> &container);

void removePeople(vector<unique_ptr<Human>> &container);

void editPeople(vector<unique_ptr<Human>> &container);

void outputMenu(vector<unique_ptr<Human>> &container);
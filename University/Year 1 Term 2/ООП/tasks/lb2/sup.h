#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../../lib.h"
using namespace std;

// delta class declaration
class Stud;

// for showing the main menu of the application
void outputMenu(vector<unique_ptr<Stud>> &studentVector);

// object deletion function
void deleteStudent(vector<unique_ptr<Stud>> &studentVector);

// for editing student information
void editStudent(vector<unique_ptr<Stud>> &studentVector);

// printing objects function
void showStudents(vector<unique_ptr<Stud>> &studentVector);

// object creation function
void addStudents(vector<unique_ptr<Stud>> &studentVector);

// for calculating student age
ll calculateStudentAge(unique_ptr<Stud> &StudentObject);
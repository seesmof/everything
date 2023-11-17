#pragma once
#include <bits/stdc++.h>
#include "sup.cpp"
#include "../../lib.h"
using namespace std;

// define the Stop struct, which represents a stop on the route
class Stop;

// delta class declaration
class Stud;

// for converting double time to correct format
string convertTime(double timeInHours);

// for manipulating input stream
istream &insetup(istream &input);

// for manipulating input stream with file
istream &insetup(istream &input, const string &FILE);

// for manipulating output stream
ostream &outsetup(ostream &output);

// for manipulating output stream with file
ostream &outsetup(ostream &output, string file_name);

// for showing all stops in a route
void showRoute(Route &routeContainer);

// for showing all stops in a route
void showRoute(Route &routeContainer, const string &FILE_NAME);

// for adding stops to route container
void addStop(Route &routeContainer);

// for adding stops to route container from a file
void addStop(Route &routeContainer, const string &FILE_NAME);

// for deleting stops from container
void deleteStop(Route &routeContainer);

// for showing the main menu of the application
void outputMenu(Route &routeContainer);
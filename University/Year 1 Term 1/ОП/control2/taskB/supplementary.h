#pragma once
#include <bits/stdc++.h>
#include "supplementary.cpp"
using namespace std;

// create struct for holding emails data
struct Letter;
string getEmailAddress();
string getFileName();
string generateRandomString(int length);
vector<string> getUniqueElements(vector<string> &inputVector);
void fillVector(vector<Letter> &a, const string &FILE_NAME);
ostream &BOLD(ostream &);
ostream &UNBOLD(ostream &);
ostream &RED(ostream &);
ostream &UNRED(ostream &);
ostream &GREEN(ostream &);
ostream &UNGREEN(ostream &);
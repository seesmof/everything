#pragma once
#include <bits/stdc++.h>
#include "menu.cpp"
using namespace std;

// for outputting main menu to user
void outputMenu(vector<Letter> &lettersVector, string inEmailAddress);

// For outputting emails from the inbox
void outputLetters(vector<Letter> &lettersVector, string inEmailAddress);

// for searching for a letter by different parameters
void searchLetters(vector<Letter> &lettersVector);

// for searching letters by keyword
void searchLetters(vector<Letter> &lettersVector, string keyword);

// for offering user to make some actions on the letter
void letterManipulation(vector<Letter> &lettersVector, vector<int> &inboxLettersVector);

// for outputting search results
void searchResults(int inboxLettersCounter, vector<int> &inboxLettersVector, vector<Letter> &lettersVector);
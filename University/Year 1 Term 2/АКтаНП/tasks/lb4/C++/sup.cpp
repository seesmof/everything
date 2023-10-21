#include "sup.h"
#include "D:\repos\university\lib.h"

void showNums(ll numOne, ll numTwo)
{
    cout << GRAY << "The two numbers are: " << UNGRAY;
    cout << numOne << " and " << numTwo << endl;
}

void addNums(ll operandOne, ll operandTwo)
{
    cout << GRAY << "The sum of the two numbers is: " << UNGRAY;
    cout << operandOne + operandTwo << endl;
}

void subNums(ll operandOne, ll operandTwo)
{
    cout << GRAY << "The difference of the two numbers is: " << UNGRAY;
    cout << operandOne - operandTwo << endl;
}

void mulNums(ll operandOne, ll operandTwo)
{
    cout << GRAY << "The product of the two numbers is: " << UNGRAY;
    cout << operandOne * operandTwo << endl;
}

void divNums(ll operandOne, ll operandTwo)
{
    cout << GRAY << "The quotient of the two numbers is: " << UNGRAY;
    cout << operandOne / operandTwo << endl;
}

void outputMenu()
{
    cout << GRAY << "Before we begin, let's enter the two opearnds\n"
         << UNGRAY;
    cout << "Enter number one: ";
    ll operandOne = getNum();
    cout << "Enter number two: ";
    ll operandTwo = getNum();
    cout << endl;
    vector<string> menuItems = {
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Show numbers",
        "Exit"};
    ll userDecision = showMenu(menuItems);

    if (userDecision == 1)
    {
        addNums(operandOne, operandTwo);
    }
    else if (userDecision == 2)
    {
        subNums(operandOne, operandTwo);
    }
    else if (userDecision == 3)
    {
        mulNums(operandOne, operandTwo);
    }
    else if (userDecision == 4)
    {
        divNums(operandOne, operandTwo);
    }
    else if (userDecision == 5)
    {
        showNums(operandOne, operandTwo);
    }
}
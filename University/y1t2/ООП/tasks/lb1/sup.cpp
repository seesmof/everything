#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// delta class declaration
class Delta
{
private:
    // declare private members
    ll objectDescriptor;

public:
    // create default constructor function
    Delta() : objectDescriptor(getNextDefaultDescriptor()) {}

    // next identifier creator
    static ll getNextDefaultDescriptor()
    {
        // use static variable for tracking identifier
        static int descriptorHolder = 0;
        // return it to user
        return descriptorHolder++;
    }

    ll getObjectDescriptor() const;

    // create default destructor function
    ~Delta()
    {
    }
};

// getter for object identifier
ll Delta::getObjectDescriptor() const
{
    return objectDescriptor;
}

// object creation function
void createObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
    // ask user to enter number of delta objects to create
    ll objectsAmount;
    cout << "\nEnter an amount of objects to create: ";
    cin >> objectsAmount;

    // if entered text is not an integer
    if (cin.fail())
    {
        // output error
        cout << RED << "\nERROR: Enter an integer...\n\n"
             << UNRED;
        // clear buffer
        cin.clear();
        cin.ignore();
        // stop function execution
        return;
    }
    // if entered amount is less than one
    else if (objectsAmount < 1)
    {
        // output error and stop function
        cout << RED << "\nERROR: Invalid amount of objects...\n\n"
             << UNRED;
        // stop function execution
        return;
    }

    // create specified amount of objects using a for loop
    for (ll i = 0; i < objectsAmount; i++)
        deltaObjectsVector.push_back(make_unique<Delta>());

    // end function execution
    return;
}

// printing objects function
void printObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
    // get vector size
    ll vectorSize = deltaObjectsVector.size();

    // output all objects with their identifiers using a for loop
    cout << BOLD << "\nYour objects (" << vectorSize << "): \n"
         << UNBOLD;
    for (ll i = 0; i < vectorSize; i++)
        cout << i + 1 << ". Descriptor: " << deltaObjectsVector[i]->getObjectDescriptor() << endl;

    // end function execution
    return;
}

// object deletion function
void deleteObjects(vector<unique_ptr<Delta>> &deltaObjectsVector)
{
    // check if vector is empty
    if (deltaObjectsVector.size() == 0)
        // if so, output error message
        cout << GRAY << "\nNo objects to delete\n"
             << UNGRAY;
    // if not
    else
    {
        // print all objects to user
        printObjects(deltaObjectsVector);

        // prompt user to enter an object number to delete
        ll numToDelete = 0;
        cout << "\nEnter a number of object to delete: ";
        cin >> numToDelete;

        // check if entered text is not an integer
        if (cin.fail())
        {
            // output error
            cout << RED << "\nERROR: Enter an integer...\n\n"
                 << UNRED;
            // clear buffer
            cin.clear();
            cin.ignore();
            // stop function execution
            return;
        }

        // modify object number to fit in with indeces
        numToDelete--;

        // if the object number is out of range
        if (numToDelete > deltaObjectsVector.size() - 1 || numToDelete < 0)
            // output error message
            cout << RED << "\nERROR: Invalid object number\n"
                 << UNRED;
        // if not
        else
        {
            // output success message
            cout << GREEN << endl
                 << deltaObjectsVector[numToDelete]->getObjectDescriptor() << " successfully deleted\n"
                 << UNGREEN;

            // erase object from vector
            deltaObjectsVector.erase(deltaObjectsVector.begin() + numToDelete);
        }
    }

    // end function execution
    return;
}
// include necessary libraries
#include <iostream>
#include <string>
using namespace std;

// create a structure to hold the semi truck's information
struct freightTruck
{
    // declare variables for storing manufacturer and model name
    string manufacturerName;
    string modelName;
    // declare variables for storing carrying capacity
    int carryingCapacity;
    // declare variables for storing manufacturing and registration years
    int manufacturedYear;
    int registrationYear;
};

// declare a function prototype
void trucksInput(int n, freightTruck *truck);

// declare main function
int main(int argc, char **argv)
{
    // output program intro
    cout << "****************************** Task A *************************************" << endl
         << endl;

    // declare local variables
    int n;
    freightTruck truck[n];

    // ask user to enter the amount of trucks he wants
    cout << "Enter the amount of trucks you want to enter: ";
    cin >> n;
    cout << endl;

    // call a function for entering information for each of the trucks
    trucksInput(n, truck);

    // create function to output the trucks that suit the parameters
    cout << "Trucks that were registered more than a year ago and have carrying capacity of more than 3 tons: " << endl;
    for (int i = 0; i < n; i++)
    {
        // if truck's registration year is less than 2021 and it has a carrying capacity of more than 3 tons
        if (truck[i].registrationYear < 2021 && truck[i].carryingCapacity > 3)
        {
            // output its information to user
            cout << i + 1 << ". " << truck[i].manufacturerName << " " << truck[i].modelName << " has carrying capacity of " << truck[i].carryingCapacity << " tons, was manufactured in " << truck[i].manufacturedYear << " and registered in " << truck[i].registrationYear << "." << endl;
        }
    }

    // output project outro
    cout << endl
         << "***************************************************************************" << endl;

    // end main function
    return 0;
}

// create function that will ask user to input information for each of the vehicles
void trucksInput(int n, freightTruck *truck)
{
    // create for loop for the amount of vehicles a user entered before
    for (int i = 0; i < n; i++)
    {
        int subCount = 1;
        // ask user to enter manufacturerName
        cout << i + 1 << "." << subCount << " Enter manufacter name: ";
        cin >> truck[i].manufacturerName;
        subCount++;
        // if the name starts with a lowercase letter
        if (islower(truck[i].manufacturerName[0]))
        {
            // convert it to an uppercase one
            truck[i].manufacturerName[0] = toupper(truck[i].manufacturerName[0]);
        }
        // ask user to enter modelName
        cout << i + 1 << "." << subCount << " Enter model name: ";
        cin >> truck[i].modelName;
        subCount++;
        // ask user to enter carryingCapacity
        cout << i + 1 << "." << subCount << " Enter carrying capacity (tons): ";
        cin >> truck[i].carryingCapacity;
        subCount++;
        // ask user to enter manufacturedYear
        cout << i + 1 << "." << subCount << " Enter manufactured year: ";
        cin >> truck[i].manufacturedYear;
        subCount++;
        // ask user to enter registrationYear
        cout << i + 1 << "." << subCount << " Enter registration year: ";
        cin >> truck[i].registrationYear;
        cout << endl;
    }
    // end function
    return;
}
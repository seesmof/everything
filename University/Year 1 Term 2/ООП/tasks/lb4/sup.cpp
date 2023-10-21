#include <bits/stdc++.h>
#include "sup.h"
#include "../../lib.h"
using namespace std;

// Для завдання з лабораторної роботи #2 реалізувати методи консольного та файлового введення/виведення, створити маніпулятори insetup та outsetup для форматування відповідно потоків введення/виведення.

// define the Stop struct, which represents a stop on the route
class Stop
{
public:
    string stopName;             // name of the stop
    double distanceFromPrevious; // distance from previous stop
    Stop *previousStop;          // pointer to previous stop in route
    Stop *nextStop;              // pointer to next stop in route
};

// define the Route class, which represents a route composed of stops
class Route
{
private:
    Stop *firstStop;      // pointer to first stop in route
    Stop *lastStop;       // pointer to last stop in route
    static ll stopsCount; // total number of stops in route
public:
    // constructor initializes empty route with head and tail set to nullptr
    Route() : firstStop(nullptr), lastStop(nullptr) {}

    // copy constructor for the Route class
    Route(const Route &otherRoute)
    {
        // create a new empty Route object
        Route newRoute;

        // traverse the original Route object from first to last Stop
        Stop *currentStop = otherRoute.firstStop;
        while (currentStop != nullptr)
        {
            // create a new Stop object with the same properties and add it to the new Route object
            Stop *newStop = new Stop;
            newStop->stopName = currentStop->stopName;
            newStop->distanceFromPrevious = currentStop->distanceFromPrevious;
            newStop->previousStop = newRoute.lastStop;
            newStop->nextStop = nullptr;
            if (newRoute.lastStop != nullptr)
            {
                newRoute.lastStop->nextStop = newStop;
            }
            else
            {
                newRoute.firstStop = newStop;
            }
            newRoute.lastStop = newStop;

            // move onto the next Stop in the original Route object
            currentStop = currentStop->nextStop;
        }
    }

    // declare desctructor that deletes all stops from the route
    ~Route()
    {
        // set temp stop to first one
        Stop *currentStop = firstStop;
        // till the end of the list
        while (currentStop != nullptr)
        {
            // declare next stop and assign it the next stop value
            Stop *nextStop = currentStop->nextStop;
            // delete current stop
            delete currentStop;
            // move onto the next one
            currentStop = nextStop;
        }
    }

    // first stop getter
    Stop *getFirstStop() const
    {
        return firstStop;
    }

    // last stop getter
    Stop *getLastStop() const
    {
        return lastStop;
    }

    // for getting the amount of stops in the route
    ll getStopsCount() const
    {
        // return the stops count
        return stopsCount;
    }

    // adds a new stop with the given name and distance from previous stop to the end of the route
    void add_stop(string inputStopName, double inputDistance)
    {
        // declare new stop
        Stop *stopHolder = new Stop();
        // assign data values to it
        stopHolder->stopName = inputStopName;
        stopHolder->distanceFromPrevious = inputDistance;

        // check if the list is empty by checking if head element points to NULL
        if (firstStop == nullptr)
        {
            // if so set our stop as a first by assigning it to both first and last
            firstStop = stopHolder;
            lastStop = stopHolder;
        }
        // if its not empty
        else
        {
            // our previous stop is current last
            stopHolder->previousStop = lastStop;
            // current last stop's next stop is our stop
            lastStop->nextStop = stopHolder;
            // and our stop becomes last, because we add it to the end
            lastStop = stopHolder;
        }
        stopsCount++;
    }

    // for deleting a stop based on its name
    void delete_stop(string inputStopName)
    {
        // declare temp stop
        Stop *stopHolder = firstStop;
        // iterate over all stops
        while (stopHolder != nullptr)
        {
            // check if we found the one with a correct name
            if (stopHolder->stopName == inputStopName)
            {
                // check if its the first stop
                if (stopHolder == firstStop)
                    // if so assign first stop to our current next stop
                    firstStop = stopHolder->nextStop;
                // check if we have a stop ahead
                if (stopHolder->nextStop != nullptr)
                    // if so assign next stop's previous stop value to current previous stop
                    stopHolder->nextStop->previousStop = stopHolder->previousStop;
                // check if we have a stop behind us
                if (stopHolder->previousStop != nullptr)
                    // if so assign previous stop's next stop value to current next stop
                    stopHolder->previousStop->nextStop = stopHolder->nextStop;
                // delete the stop
                delete stopHolder;
                // stop function execution
                return;
            }
            // if we haven't found the stop, continue to the next one
            stopHolder = stopHolder->nextStop;
        }
    }

    // for getting the length of a route
    double len_route()
    {
        // for holding the resulting length
        double totalLength = 0.0;
        Stop *currentStopHolder = firstStop;
        // iterate over all the stops
        while (currentStopHolder != nullptr)
        {
            // add distance of each stop to total counter
            totalLength += currentStopHolder->distanceFromPrevious;
            // and continue
            currentStopHolder = currentStopHolder->nextStop;
        }
        // return the resulting length
        return totalLength;
    }

    // for getting the time it takes to traverse the route
    double time_route()
    {
        // get route time by dividing the length by an average speed of 30km/h
        double routeTime = len_route() / 50.0;
        // return it
        return routeTime;
    }
};

// initialize the stops counter at 0
ll Route::stopsCount = 0;

// for converting double time to correct format
string convertTime(double timeInHours)
{
    // get total minutes count by converting to int and multiplying by 60
    int totalMinutes = static_cast<int>(timeInHours * 60);
    // get hours cound by dividing minutes by 60
    int hours = totalMinutes / 60;
    // get minutes count by getting modulo of total minutes by 60
    int minutes = totalMinutes % 60;
    // return string in correct format, utilize ternary operator
    return to_string(hours) + ":" + (minutes < 10 ? "0" : "") + to_string(minutes);
}

// for manipulating input stream
istream &insetup(istream &input)
{
    // declare manipulators for console input
    input >> noskipws;       // don't skip whitespaces
    input.ignore(100, '\n'); // ignore up to 100 characters or until newline is found
    return input;
}

// for manipulating input stream with file
istream &insetup(istream &input, const string &FILE)
{
    // declare manipulators for file input
    input >> noskipws;       // don't skip whitespaces
    input.ignore(100, '\n'); // ignore up to 100 characters or until newline is found

    // open file and check if it is open
    ifstream inFile(FILE);
    if (!inFile.is_open())
    {
        bad("Could not open file");
        exit(1);
    }
    // read data from file into buffer
    input.rdbuf(inFile.rdbuf());

    // close file and return
    inFile.close();
    return input;
}

// for manipulating output stream
ostream &outsetup(ostream &output)
{
    // Useful manipulators for console output
    output.precision(2);     // Set precision to 2 decimal places
    output.setf(ios::fixed); // Set fixed floating-point notation
    return output;
}

// for manipulating output stream with file
ostream &outsetup(ostream &output, string file_name)
{
    // Useful manipulators for file output
    output.precision(2);     // Set precision to 2 decimal places
    output.setf(ios::fixed); // Set fixed floating-point notation

    // Open file and check if it is open
    ofstream file(file_name);
    if (!file.is_open())
    {
        bad("Could not open file");
        exit(1);
    }

    // Write to file
    output.rdbuf(file.rdbuf());
    file.close();
    return output;
}

// for showing all stops in a route
void showRoute(Route &routeContainer)
{
    // get container size
    ll routeSize = routeContainer.getStopsCount();
    // check if the container is empty
    if (routeSize == 0)
    {
        // if so output message
        cout << GRAY << "No stops found yet...\n"
             << UNGRAY;
        // end function execution
        return;
    }
    // output all objects with their identifiers using a for loop
    cout << BOLD << "Stops (" << routeSize << "):\n\n"
         << UNBOLD;
    ll counter = 1;
    // iterate over all stops
    Stop *stopHolder = routeContainer.getFirstStop();
    while (stopHolder != NULL)
    {
        outsetup(cout) << "(" << counter << ") " << stopHolder->stopName << "• " << stopHolder->distanceFromPrevious << " KM\n\n";
        // continue
        stopHolder = stopHolder->nextStop;
        counter++;
    }
    // additionally show the length of the route and the time it takes to complete
    outsetup(cout) << "Total distance is " << routeContainer.len_route() << " KM\n";
    outsetup(cout) << "Time it takes to complete the route is " << convertTime(routeContainer.time_route()) << endl;

    // end function execution
    return;
}

// for showing all stops in a route
void showRoute(Route &routeContainer, const string &FILE_NAME)
{
    // get container size
    ll routeSize = routeContainer.getStopsCount();
    // check if the container is empty
    if (routeSize == 0)
    {
        // if so output message
        cout << GRAY << "No stops to add...\n"
             << UNGRAY;
        // end function execution
        return;
    }

    // declare file variable
    fstream oFile(FILE_NAME.c_str(), ios::out);
    // and check if it cannot be opened
    if (!oFile.is_open())
    {
        // if so output the error and stop function execution
        bad("Couldn't open file for writing");
        return;
    }

    // output the upper side to the file
    outsetup(oFile) << "========================================\n";
    outsetup(oFile) << setw(30) << "Welcome on board!\n";
    outsetup(oFile) << "========================================\n";

    // output all objects with their identifiers using a for loop
    outsetup(oFile) << "\nStops (" << routeSize << "):\n\n";
    ll counter = 1;
    // iterate over all stops
    Stop *stopHolder = routeContainer.getFirstStop();
    while (stopHolder != NULL)
    {
        // output stops data to a file
        outsetup(oFile) << "(" << counter << ") " << stopHolder->stopName << "• " << stopHolder->distanceFromPrevious << " KM\n\n";
        // continue
        stopHolder = stopHolder->nextStop;
        counter++;
    }

    // add the distance and the time it takes to complete the route to the end of the file
    outsetup(oFile) << "========================================\n";
    outsetup(oFile) << "\nTotal distance is " << routeContainer.len_route() << " KM\n";
    outsetup(oFile) << "Time it takes to complete the route is " << convertTime(routeContainer.time_route()) << endl;

    // close file, output success message and end function execution
    cout << endl;
    oFile.close();
    good("Data successfully added to the file");
    return;
}

// for adding stops to route container
void addStop(Route &routeContainer)
{
    // ask user to enter number of stop objects to create
    cout << "Enter an amount of stops to add: ";
    ll objectsAmount = getNum();
    // if entered amount is less than one
    if (objectsAmount < 1)
    {
        // output error and stop function
        cout << RED << "\nERROR: Invalid amount of objects...\n\n"
             << UNRED;
        // stop function execution
        return;
    }

    // create specified amount of objects using a for loop
    cout << endl;
    for (ll counter = 1; counter <= objectsAmount; counter++)
    {
        // ask user to enter stop name
        cin.ignore();
        string stopName;
        cout << "(" << counter << ") Stop Name: ";
        getline(cin, stopName);
        // validate stop name and continue
        stopName = validateName(stopName);

        // ask user to enter stop distance
        cout << "    Distance from Previous Stop (KM): ";
        // validate it as well
        double distanceFromPreviousStop;
        insetup(cin) >> distanceFromPreviousStop;

        // add stop using the method and continue
        routeContainer.add_stop(stopName, distanceFromPreviousStop);
        cout << endl;
    }
    // end function execution
    return;
}

// for adding stops to route container from a file
void addStop(Route &routeContainer, const string &FILE_NAME)
{
    // declare file instance
    ifstream oFile(FILE_NAME.c_str());
    // check if file cannot be opened
    if (!oFile.is_open())
    {
        // if so output the error and stop function execution
        bad("Couldn't open file for writing");
        return;
    }

    // declare variables for proecessing the lines of file
    vector<string> linesFromFile;
    string lineHolder;
    ll linesCounter = 1;

    // get all file lines
    while (getline(oFile, lineHolder))
    {
        // check if a line is empty which will indicate the new item
        if (lineHolder.empty())
            // if it is increment the counter
            linesCounter++;
        // if its not
        else
            // add line to vector
            linesFromFile.pb(lineHolder);
    }

    // create specified amount of objects using a for loop
    for (ll counter = 0, subCounter = 0; counter < linesCounter; counter++, subCounter += 2)
    {
        // process stop name
        string stopName;
        stopName = linesFromFile[subCounter];
        // validate stop name and continue
        stopName = validateName(stopName);

        // process distance
        string distanceHolder = linesFromFile[subCounter + 1];
        // convert it to double
        double distanceFromPreviousStop = stod(distanceHolder);

        // add stop using the method and continue
        routeContainer.add_stop(stopName, distanceFromPreviousStop);
    }

    // end function execution
    good("Stops successfully added");
    return;
}

// for deleting stops from container
void deleteStop(Route &routeContainer)
{
    // check if container is empty
    if (routeContainer.getStopsCount() == 0)
        // if so, output error message
        cout << GRAY << "\nNo stops to delete...\n"
             << UNGRAY;
    // if not
    else
    {
        // print all objects to user
        cin.ignore();
        showRoute(routeContainer);
        // prompt user to enter stop name to delete
        cout << "\nEnter a stop name to delete: ";
        string inputStopName;
        getline(cin, inputStopName);
        // validate it
        inputStopName = validateName(inputStopName);
        // output success message
        cout << GREEN << endl
             << inputStopName << " successfully deleted\n"
             << UNGREEN;
        // erase object from container
        routeContainer.delete_stop(inputStopName);
    }
    // end function execution
    return;
}

// for showing the main menu of the application
void outputMenu(Route &routeContainer)
{
    // output the menu
    cout << BOLD << "Welcome! Choose some option from below\n"
         << UNBOLD;
    cout << "1. Output route\n";
    cout << "2. Add stops\n";
    cout << "3. Remove stops\n";
    cout << "4. Show route length\n";
    cout << "5. Show route time\n";
    cout << "6. Exit\n";
    // ask user to enter their choice
    cout << "Enter: ";
    // and validate it
    ll userDecision = getNum();
    cout << endl;

    // if user chose to just show route
    if (userDecision == 1)
    {
        // ask user where to output the route
        cout << BOLD << "Where would you like to output the route?\n"
             << UNBOLD;
        cout << "1. Console\n";
        cout << "2. File\n";
        // validate input
        cout << "Enter: ";
        userDecision = getNum();
        cout << endl;

        // if user chose to output to console
        if (userDecision == 1)
        {
            // show it using the function
            showRoute(routeContainer);
        }
        // if user chose to output to a file
        else
        {
            // declare file name holder with path
            string outputFileName = "D:/repos/university/t2y1/oop_lab4/";
            // add the file name itself to the path
            outputFileName += getFileName();
            cout << endl;
            // output the route to a file
            showRoute(routeContainer, outputFileName);
        }
    }
    // if user chose to add stops to route
    else if (userDecision == 2)
    {
        // show the route
        showRoute(routeContainer);
        // ask user how they would like to add those stops
        cout << endl;
        cout << BOLD << "How would you like to add stops?\n"
             << UNBOLD;
        cout << "1. From console\n";
        cout << "2. From file\n";
        // validate input
        cout << "Enter: ";
        userDecision = getNum();
        cout << endl;

        // if user chose to add stops from console
        if (userDecision == 1)
        {
            // call the function
            addStop(routeContainer);
        }
        // if user chose to add stops from a file
        else
        {
            // declare file path variable
            string inputFileName = "D:/repos/university/t2y1/oop_lab4/";
            // and add filename itself to it
            inputFileName += getFileName();
            cout << endl;
            // let user add stops using the function
            addStop(routeContainer, inputFileName);
        }
    }
    // if user chose to delete a stop
    else if (userDecision == 3)
        // delete it using the function
        deleteStop(routeContainer);
    // if user chose to show the route length
    else if (userDecision == 4)
    {
        // show the route
        showRoute(routeContainer);
        // get route length using the method
        double resultLenght = routeContainer.len_route();
        // output the route length to user
        cout << "Route length is " << resultLenght << " KM\n";
    }
    // if user chose to show the route length
    else if (userDecision == 5)
    {
        // show the route
        showRoute(routeContainer);
        // get route length via the method
        double resultTime = routeContainer.time_route();
        // calculate the time in correct time format
        string formattedTime = convertTime(resultTime);
        // output the result
        cout << "It takes around " << formattedTime << " to complete the route\n";
    }
    // end function execution
    return;
}
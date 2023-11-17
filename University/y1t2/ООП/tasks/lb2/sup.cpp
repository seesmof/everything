#include <bits/stdc++.h>
#include "sup.h"
#include "../../../lib.h"
using namespace std;

// Створити динамічний клас Route на основі двозв’язного списку, де кожний елемент типа Stop (зупинка). Клас повинен містити наступні операції:
// add_stop() – додавання зупинки;
// len_route() – розрахунок довжини маршруту;
// time_route() – розрахувати час руху.

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

    double time_route()
    {
        double routeTime = len_route() / 50.0;
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
        cout << "(" << counter << ") " << stopHolder->stopName << "• " << stopHolder->distanceFromPrevious << " KM\n\n";
        // continue
        stopHolder = stopHolder->nextStop;
        counter++;
    }
    cout << "Total distance is " << routeContainer.len_route() << " KM\n";
    cout << "Time it takes to complete the route is " << convertTime(routeContainer.time_route()) << endl;
    // end function execution
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
        double distanceFromPreviousStop = getNum();

        // add stop using the method and continue
        routeContainer.add_stop(stopName, distanceFromPreviousStop);
        cout << endl;
    }
    // end function execution
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
    cout << "1. Show route\n";
    cout << "2. Add stop\n";
    cout << "3. Remove stop\n";
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
        // show it using the function
        showRoute(routeContainer);
    // if user chose to add stops to route
    else if (userDecision == 2)
    {
        // show the route
        showRoute(routeContainer);
        // and let user add stops using the function
        cout << endl;
        addStop(routeContainer);
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
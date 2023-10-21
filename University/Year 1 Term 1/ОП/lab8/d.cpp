// include necessary libraries
#include <bits/stdc++.h>
using namespace std;

// declare structure with necessary product data
struct productData
{
    string name;  // for storing product name
    double price; // for storing product price per unit
    int stock;    // for storing product quantity of products in stock
};

// function prototypes //
string fileNameInput();
string randString(int);
int countProducts(const string &);
void fillArr(const string &, productData *);
void makeOrder(const string &, productData *);
/////////////////////////

// declare main function
int main()
{
    // declare local variables //
    srand(time(NULL));
    char doContinue;
    /////////////////////////////

    // project intro
    cout << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl
         << "Welcome! This program will let you make orders from file" << endl
         << endl
         << "/////////////////////////////////////////////////////////////" << endl
         << endl;
    do
    {
        //////////////////////////////////////////////////////////////////////////////////

        // ask input file name from user
        string inputFileName = fileNameInput();
        cout << endl;

        // declare variable for storing number of products in a file
        int numOfProducts = countProducts(inputFileName);
        // declare array with number of elements from previous variable
        productData product[numOfProducts];

        // call function for filling in the array with products
        fillArr(inputFileName, product);
        // generate output file name
        int numOfLetters = rand() % 10 + 2;
        string outputFileName = randString(numOfLetters);

        // call function for making an order
        makeOrder(outputFileName, product);

        //////////////////////////////////////////////////////////////////////////////////
        cout << endl
             << "/////////////////////////////////////////////////////////////" << endl
             << endl
             << "Would you like to continue program execution? (Y | N): ";
        cin >> doContinue;
        if (doContinue == 'N' || doContinue == 'n')
        {
            cout << endl
                 << "Thanks for using this program." << endl
                 << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            break;
        }
        else
        {
            cout << endl
                 << "/////////////////////////////////////////////////////////////" << endl
                 << endl;
            continue;
        }
    } while (doContinue = 'Y' || doContinue == 'y');

    // end main function
    return 0;
}

// declare function that will process user's offer
void makeOrder(const string &out, productData *arr)
{
    // declare local variables
    vector<int> orderNames;  // for storing order names
    vector<int> orderAmount; // for storing order amounts
    int prodCount = 0;       // for storing amount of products in cart
    char anyElse;            // for storing user confirmation
    double orderTotal = 0.0; // for storing total order sum

    // create do while loop
    do
    {
        int prodChoice; // for storing user input
        // ask user to select product from the list
        cout << "Which one would you like to order? ";
        cin >> prodChoice;
        // modify product number for future operations
        prodChoice -= 1;
        // add product name to vector
        orderNames.push_back(prodChoice);

        int quantity; // for storing user input
        do
        {
            // ask user to input quantity
            cout << "Which quantity would you like to order? ";
            cin >> quantity;
            cin.ignore();

            // if quantity is more than is in stock
            if (quantity > arr[prodChoice].stock)
            {
                // output error message
                cout << endl
                     << "ERROR: Stock quantity of " << arr[prodChoice].name << " is " << arr[prodChoice].stock << endl;
                cout << "Please enter something within this range." << endl;
                // skip to next iteration
                continue;
            }
            // if quantity is good
            else
            {
                // add it to amounts vector
                orderAmount.push_back(quantity);
                cout << endl;
                // end loop
                break;
            }
            // until quantity entered is more than 0 and is within the stock range
        } while (quantity > 0 && quantity <= arr[prodChoice].stock);

        // ask if user wants to order anything else
        cout << "Would you like to order anything else? (Y | N) ";
        cin >> anyElse;
        // increase product amount in cart
        prodCount += 1;

        // if answer is no
        if (anyElse == 'N' || anyElse == 'n')
            break; // break out of loop
        // else
        else
        {
            cout << endl;
            continue; // jump to next iteration
        }
        // continue as long as user wants to order anything else
    } while (anyElse == 'Y' || anyElse == 'y');

    // temporary counter
    int counter = 1;
    // output order details to user
    cout << endl
         << "Your order is " << endl;
    for (int i = 0; i < prodCount; i++)
    {
        // temporary variables
        int nameBuf = orderNames[i];                      // for storing order name as string
        double sum = orderAmount[i] * arr[nameBuf].price; // for storing sum of current position
        // add current sum to total
        orderTotal += sum;
        // output
        cout << counter << ". x" << orderAmount[i] << " " << arr[nameBuf].name << " with a total sum of $" << sum << endl;
        // increase counter
        counter++;
    }
    // output total sum to user
    cout << "Your order is $" << orderTotal << " total." << endl;

    char confirmation; // for user confirmation
    // ask user if they confirm their order
    cout << endl
         << "Do you want to confirm your order? (Y | N) ";
    cin >> confirmation;

    // if they do
    if (confirmation == 'y' || confirmation == 'Y')
    {
        // output success message
        cout << endl;
        cout << "Order was successfully confirmed. Thank you for your trust!" << endl;

        // declare output file variable
        fstream oFile(out.c_str(), ios::out);

        // output receipt to output file
        oFile << "===============================================" << endl;
        oFile << "         Thank you for your order!" << endl;
        oFile << "===============================================" << endl
              << endl;
        oFile << "Order Details" << endl
              << endl;

        // output each position with amount and price
        counter = 1;
        for (int i = 0; i < prodCount; i++)
        {
            int nameBuf = orderNames[i];
            double sum = orderAmount[i] * arr[nameBuf].price;
            oFile << orderAmount[i] << "x " << arr[nameBuf].name << ": $" << sum << endl;
            counter++;
        }
        // output total sum
        oFile << endl
              << "===============================================" << endl;
        oFile << "Total Order Sum\t\t\t\t\t\t$" << orderTotal << endl;
        oFile << "===============================================" << endl;

        return; // end function
    }
    // if they don't confirm order
    else
    {
        // output message
        cout << endl;
        cout << "We are sorry to hear that. Order successfully cancelled." << endl;
        return; // end function
    }
}

// declare function that will count number of products in input file
int countProducts(const string &filename)
{
    fstream iFile(filename.c_str(), ios::in); // for holding file
    int res = 1;                              // for storing result
    string buf;                               // for storing current line

    // for each line
    while (getline(iFile, buf))
    {
        // if line is empty
        if (buf.empty())
            // increment counter
            res++;
    }
    // return number of products
    return res;
}

// declare function that will fill in the array with data from the file
void fillArr(const string &name, productData *arr)
{
    // declare local variables
    fstream iFile(name.c_str(), ios::in); // input file
    vector<string> products;              // for storing all lines
    string buf;                           // for storing current line
    int res = 1;                          // for storing number of products

    // for each line
    while (getline(iFile, buf))
    {
        // if line is empty
        if (buf.empty())
            // increment counter
            res++;
        else
            // add line to string array
            products.push_back(buf);
    }

    // declare temporary counter
    int counter = 1;
    // output all the products from file to user
    cout << "Here is every product in stock right now: " << endl;
    for (int i = 0, j = 0; i < res; i++, j += 3)
    {
        arr[i].name = products[j];
        cout << counter << ". Product name: " << arr[i].name << endl;
        arr[i].price = stod(products[j + 1]);
        cout << counter << ". Price per one: $" << arr[i].price << endl;
        arr[i].stock = stoi(products[j + 2]);
        cout << counter << ". Current stock: " << arr[i].stock << endl;
        cout << endl;
        counter++;
    }

    return; // end function
}

// create a function that will take file name from user
string fileNameInput()
{
    // declare local variables
    bool isExtensionFound = false;
    string input;

    // ask user to input file name
    cout << "Enter the name of the file: ";
    cin >> input;
    cin.ignore();

    // create for loop to look for extension
    for (int i = 0; i < input.length(); i++)
    {
        // dot is an indication of extension
        if (input[i] == '.')
        {
            // if found then change bool isExtensionFound to true
            isExtensionFound = true;
            break; // break out of loop
        }
    }

    // if the result is not found then
    if (!isExtensionFound)
    {
        // create a new string for holding the file extension
        string fileExtension;

        // ask user to enter a file extension
        cout << "Please specify a file extension: ";
        cin >> fileExtension;
        cin.ignore();

        // create a for loop
        for (int i = 0; i < fileExtension.length(); i++)
        {
            // look for a dot in input
            if (fileExtension[i] == '.')
            {
                // if found then add it to the result string
                input += fileExtension;
                break; // break out of loop
            }
            else
            {
                // if not found then add add a dot + input to the result string
                input += "." + fileExtension;
                break; // break out of loop
            }
        }
    }

    // return the result string
    return input;
}

// create a function that will generate random string
string randString(int ch)
{
    // declare max array length
    const int maxArrSize = 25;
    // declare possible characters
    char possibleCharactersArr[maxArrSize] = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
                                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                              'o', 'p', 'q', 'r', 's', 't', 'u',
                                              'v', 'w', 'x', 'y'};
    // declare result string
    string result = "";
    // create for loop
    for (int i = 0; i < ch; i++)
        // add random character from an earlier declared set to the string
        result += possibleCharactersArr[rand() % maxArrSize];

    // add file extension to result
    result += ".txt";
    // return result
    return result;
}
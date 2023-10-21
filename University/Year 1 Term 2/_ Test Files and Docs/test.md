```c++
class Exception
{
public:
    virtual void what() const throw()
    {
        bad("An exception has occurred");
    }
};

class IOException : public Exception
{
public:
    void what() const throw() override
    {
        bad("I/O stream error");
    }
};

class ArithmeticException : public Exception
{
public:
    void what() const throw() override
    {
        bad("Arithmetic error: division by zero");
    }
};

class MemoryException : public Exception
{
public:
    void what() const throw() override
    {
        bad("Memory allocation error");
    }
};

int main()
{
    try
    {
        // Example of handling I/O stream error
        ifstream file("nonexistent_file.txt");
        if (!file.is_open())
        {
            throw IOException();
        }
        // Example of handling arithmetic error
        divide(10, 0);
        // Example of handling memory allocation error
        int *arr = new int[1000000000000];
        delete[] arr;
    }
    catch (Exception &e)
    {
        cerr << "Exception caught: " << e.what() << endl;
    }
    return 0;
}
```


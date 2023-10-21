#include <iostream>
using namespace std;

class Piece
{
protected:
    int sequenceNumber;

public:
    Piece(int sequenceNumber) : sequenceNumber(sequenceNumber) {}
};

class Checker : public Piece
{
private:
    double x, y;

public:
    Checker(int sequenceNumber, double x, double y) : Piece(sequenceNumber), x(x), y(y) {}

    Checker operator-(Checker &c)
    {
        if ((x - c.x == 1 && y - c.y == 1) || (x - c.x == -1 && y - c.y == -1))
        {
            c.x = 0.0;
            c.y = 0.0;
        }
        else
        {
            x = 0.0;
            y = 0.0;
        }
        return c;
    }

    Checker operator++()
    {
        y++;
        return *this;
    }

    Checker operator++(int)
    {
        Checker temp(*this);
        operator++();
        return temp;
    }

    bool operator<(const Checker &c)
    {
        return y < c.y;
    }

    bool operator>(const Checker &c)
    {
        return y > c.y;
    }

    friend ostream &operator<<(ostream &os, Checker &c)
    {
        os << "Checker at position (" << c.x << ", " << c.y << ")";
        return os;
    }

    friend istream &operator>>(istream &is, Checker &c)
    {
        cout << "Enter x coordinate: ";
        is >> c.x;
        cout << "Enter y coordinate: ";
        is >> c.y;
        return is;
    }
};

class Queen : public Piece
{
public:
    Queen(int sequenceNumber) : Piece(sequenceNumber) {}

    void move()
    {
        cout << "Queen moved" << endl;
    }

    void strike()
    {
        cout << "Queen struck" << endl;
    }
};

int main()
{
    Checker c1(1, 1.0, 1.0), c2(2, 2.0, 2.0);
    cout << c1 << endl;
    cout << c2 << endl;

    c1 = c1 - c2;
    cout << c1 << endl;
    cout << c2 << endl;

    c1++;
    cout << c1 << endl;

    cout << (c1 < c2) << endl;
    cout << (c1 > c2) << endl;

    cin >> c1;
    cout << c1 << endl;

    Queen q(3);
    q.move();
    q.strike();

    return 0;
}

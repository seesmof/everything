#include <iostream>
#include <vector>
#include <string>

using namespace std;

const string RED_COLOR_CODE = "\033[31m";
const string BLACK_COLOR_CODE = "\033[30m";
const string RESET_COLOR_CODE = "\033[0m";

class Piece
{
public:
    int sequence_number;
    Piece(int sequence_number) : sequence_number(sequence_number) {}
};

class Checker : public Piece
{
public:
    Checker(int sequence_number) : Piece(sequence_number) {}
    bool operator<(const Checker &other) const
    {
        return sequence_number < other.sequence_number;
    }
    bool operator>(const Checker &other) const
    {
        return sequence_number > other.sequence_number;
    }
    Checker operator--(int)
    {
        sequence_number--;
        return *this;
    }
    Checker &operator--()
    {
        --sequence_number;
        return *this;
    }
    Checker operator-(const Checker &other) const
    {
        Checker result = *this;
        if (result > other)
        {
            result.sequence_number = 0;
        }
        return result;
    }
    friend ostream &operator<<(ostream &os, const Checker &checker);
};

class Queen : public Piece
{
public:
    Queen(int sequence_number) : Piece(sequence_number) {}
    void move()
    {
        cout << "Move method for Queen" << endl;
    }
    void strike()
    {
        cout << "Strike method for Queen" << endl;
    }
};

ostream &operator<<(ostream &os, const Checker &checker)
{
    os << "Checker " << checker.sequence_number;
    return os;
}

int main()
{
    // Create objects of derived types
    Checker checker1(1);
    Checker checker2(2);
    Queen queen1(1);
    Queen queen2(2);

    // Initialize board
    const int BOARD_SIZE = 8;
    vector<vector<char>> board(BOARD_SIZE, vector<char>(BOARD_SIZE, '.'));
    board[0][1] = 'X';
    board[0][3] = 'X';
    board[0][5] = 'X';
    board[0][7] = 'X';
    board[1][0] = 'X';
    board[1][2] = 'X';
    board[1][4] = 'X';
    board[1][6] = 'X';
    board[2][1] = 'X';
    board[2][3] = 'X';
    board[2][5] = 'X';
    board[2][7] = 'X';
    board[5][0] = 'O';
    board[5][2] = 'O';
    board[5][4] = 'O';
    board[5][6] = 'O';
    board[6][1] = 'O';
    board[6][3] = 'O';
    board[6][5] = 'O';
    board[6][7] = 'O';
    board[7][0] = 'O';
    board[7][2] = 'O';
    board[7][4] = 'O';
    board[7][6] = 'O';

    // Play game
    bool is_red_turn = true;
    while (true)
    {
        // Print board
        cout << BLACK_COLOR_CODE << "  ";
        for (int col = 0; col < BOARD_SIZE; col++)
        {
            cout << col << " ";
        }
        cout << endl;
        for (int row = 0; row < BOARD_SIZE; row++)
        {
            cout << BLACK_COLOR_CODE << row << " ";
            for (int col = 0; col < BOARD_SIZE; col++)
            {
                if (board[row][col] == 'X')
                {
                    cout << RED_COLOR_CODE << 'X' << " ";
                }
                else if (board[row][col] == 'O')
                {
                    cout << BLACK_COLOR_CODE << 'O' << " ";
                }
                else
                {
                    cout << ". ";
                }
            }
            cout << endl;
        }
        cout << RESET_COLOR_CODE;
        // Print turn message
        if (is_red_turn)
        {
            cout << RED_COLOR_CODE << "\nRed's turn" << RESET_COLOR_CODE << endl;
        }
        else
        {
            cout << BLACK_COLOR_CODE << "\nBlack's turn" << RESET_COLOR_CODE << endl;
        }

        // Get move from user
        int from_row, from_col, to_row, to_col;
        cout << "Enter move: ";
        cin >> from_row >> from_col >> to_row >> to_col;

        // Move piece
        char piece = board[from_row][from_col];
        board[from_row][from_col] = '.';
        board[to_row][to_col] = piece;

        // Check for capture
        int capture_row = (from_row + to_row) / 2;
        int capture_col = (from_col + to_col) / 2;
        if (abs(from_row - to_row) == 2)
        {
            if (board[capture_row][capture_col] == 'X' || board[capture_row][capture_col] == 'O')
            {
                cout << "Capture!" << endl;
            }
            board[capture_row][capture_col] = '.';
        }

        // Check for promotion to queen
        if (to_row == 0 && board[to_row][to_col] == 'X')
        {
            board[to_row][to_col] = 'Q';
        }
        else if (to_row == BOARD_SIZE - 1 && board[to_row][to_col] == 'O')
        {
            board[to_row][to_col] = 'q';
        }

        // Switch turns
        is_red_turn = !is_red_turn;
    }
    return 0;
}

class GeometricFigure
{
protected:
    int centerX;
    int centerY;
    int angle;
    int scale;
public:
    GeometricFigure() : centerX(0), centerY(0), angle(0), scale(0) {}
    GeometricFigure(int centerX, int centerY, int angle, int scale) : centerX(centerX), centerY(centerY), angle(angle), scale(scale) {}
    virtual void show() = 0;
    virtual void hide() = 0;
    virtual void rotate(int angle) = 0;
    virtual void move(int x, int y) = 0;
    virtual ~GeometricFigure() {}
};

class Rectangle : public GeometricFigure
{
private:
    string color;
    string symbol;
public:
    Rectangle(int centerX, int centerY, int angle, int scale, string color) : GeometricFigure(centerX, centerY, angle, scale), color(color), symbol(NUint) {}
    void show() override
    {
        if (color == "orange")
        {
            if (angle != 90 || angle != 180 || angle != 270 || angle != 360 || angle != 0)
                symbol = "🟧";
            else
                symbol = "🔶";
        }
        else
        {
            if (angle != 90 || angle != 180 || angle != 270 || angle != 360 || angle != 0)
                symbol = "🟦";
            else
                symbol = "🔷";
        }
        for (int i = 0; i < scale; i++)
        {
            for (int k = 0; k < centerX; k++)
                cout << " ";
            for (int k = 0; k < centerY; k++)
                cout << "\n";

            for (int j = 0; j < scale; j++)
                cout << symbol;
            cout << endl;
        }
    }
    void hide() override
    { symbol = " "; }
    void rotate(int angle) override
    { angle += angle; }
    void move(int x, int y) override
    { centerX += x; centerY += y; }
};
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    string str;
    int second = 0;
    cin >> str;
    for (int i = 0; i < str.length(); i++)
    {
        if (str.at(i) >= 'A' && str.at(i) <= 'C')
            second += 3;
        else if (str.at(i) >= 'D' && str.at(i) <= 'F')
            second += 4;
        else if (str.at(i) >= 'G' && str.at(i) <= 'I')
            second += 5;
        else if (str.at(i) >= 'J' && str.at(i) <= 'L')
            second += 6;
        else if (str.at(i) >= 'M' && str.at(i) <= 'O')
            second += 7;
        else if (str.at(i) >= 'P' && str.at(i) <= 'S')
            second += 8;
        else if (str.at(i) >= 'T' && str.at(i) <= 'V')
            second += 9;
        else if (str.at(i) >= 'W' && str.at(i) <= 'Z')
            second += 10;
    }
    cout << second;
}
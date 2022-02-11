#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a, b[4] = {};
    cin >> a;
    for (int i = 1; i <= 3; i++)
    {
        scanf("%1d", &b[i]);
    }

    int n = (b[1] * 100) + (b[2] * 10) + b[3];

    cout << a * b[3] << endl;
    cout << a * b[2] << endl;
    cout << a * b[1] << endl;
    cout << a * n << endl;
}
#include <iostream>
using namespace std;

int main()
{
    int n, x, a;
    cin >> n >> x;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        for (int i = 0; i < n; i++)
        {
            if (a < x)
            {
                cout << a << ' ';
                break;
            }
        }
    }
}
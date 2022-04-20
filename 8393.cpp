#include <iostream>
using namespace std;

int main()
{
    int n, tmp = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        tmp += i;
    }

    cout << tmp;
}
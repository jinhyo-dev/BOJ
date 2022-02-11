#include <iostream>
using namespace std;

int main()
{
    int a[2];
    int tmp = 0, cnt = 0, n = 0, var, num;
    scanf("%d", &num);

    if (num >= 10)
    {
        a[0] = num / 10;
        a[1] = num % 10;
    }
    else
    {
        a[0] = 0;
        a[1] = num;
    }

    n = (a[0] * 10) + a[1];

    while (1)
    {
        tmp = a[0] + a[1];

        if (tmp >= 10)
            tmp - 10;

        a[0] = a[1];
        a[1] = tmp;

        if (a[1] >= 10)
            a[1] -= 10;

        var = (a[0] * 10) + a[1];

        cnt++;
        if (n == var)
            break;
    }
    cout << cnt;
}
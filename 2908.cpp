#include <iostream>
using namespace std;

int main()
{
    int a[3] = {}, b[3] = {};
    int firstNum = 0, secondNum = 0;
    scanf("%1d %1d %1d", &a[0], &a[1], &a[2]);
    scanf("%1d %1d %1d", &b[0], &b[1], &b[2]);

    firstNum = a[2] * 100 + a[1] * 10 + a[0];
    secondNum = b[2] * 100 + b[1] * 10 + b[0];

    if (firstNum > secondNum)
        cout << firstNum;
    else if (firstNum < secondNum)
        cout << secondNum;
}
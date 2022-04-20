// n을 입력받아 n번째로 큰 수를 찾기
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[100000] = {};
    int max = 0, index;

    for (int i = 0; i < 9; i++)
    {
        cin >> a[i];
        if (a[i] > max)
        {
            max = a[i];
            index = i;
        }
    }
    cout << max << ' ' << index + 1;
}
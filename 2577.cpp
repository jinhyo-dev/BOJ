//세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까
#include <iostream>
using namespace std;
int main()
{
    int a, b, c, total = 0;
    int cnt[10] = {};
    cin >> a >> b >> c;
    total = a * b * c;

    while (total != 0)
    {
        cnt[total % 10]++;
        total /= 10;
    }

    for (int i : cnt)
        cout << i << endl;
}
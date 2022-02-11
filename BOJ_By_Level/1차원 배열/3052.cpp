//수 10개를 입력받은 뒤, 이를 42로 나눈 나머지
#include <iostream>
using namespace std;

int main()
{
    int a[42] = {};
    int n, sum = 0;

    for (int i = 0; i < 10; i++)
    {
        cin >> n;

        if (!a[n % 42]++)
            sum++;
    }
    cout << sum;
}

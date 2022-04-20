//기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[1000000] = {};
    int n, max = 0;
    double result;
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, a + n);
    max = a[n - 1];

    for (int i = n - 1; i > -1; i--)
        result += a[i];

    result = (result / max * 100) / n;

    cout << fixed;
    cout.precision(6);
    cout << result << endl;

    // printf("%.6lf", result);
}
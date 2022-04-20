// #include <iostream>
// #include <algorithm>
// using namespace std;
// int main()
// {
//     int a[100000001] = {};
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++)
//         cin >> a[i];

//     sort(a, a + n);
//     cout << a[0] << a[n - 1];
// }

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, maxVal = 0, minVal = 100000000, value;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> value;
        maxVal = max(maxVal, value);
        minVal = min(minVal, value);
    }

    cout << minVal << ' ' << maxVal;
}

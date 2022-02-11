#include <iostream>
using namespace std;

int main()
{
  int a[100][100] = {};
  int n, cnt, i, j, m;
  cin >> n;

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
      cin >> a[j][i];
  }

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
      cout << a[j][i] << ' ';

    cout << endl;
  }
}
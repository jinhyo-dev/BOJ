#include <iostream>
using namespace std;
int main()
{
  int a[1000][1000] = {};
  int n, cnt, i, j, m;
  cin >> n;

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
      a[j][i] = ++cnt;
  }

  for (i = 1; i <= n; i++)
  {
    if (i % 2 != 0)
    {
      for (j = n; j > 0; j--)
        cout << a[j][i] << ' ';
    }
    else if (i % 2 == 0)
    {

      for (j = 1; j <= n; j++)
        cout << a[j][i] << ' ';
    }
    cout << endl;
  }
}
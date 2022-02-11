#include <iostream>
using namespace std;
int main()
{
  int a[101][101];
  int i, j, n, m, cnt = 1;
  cin >> n >> m;

  for (i = m; i >= 1; i--)
  {
    for (j = n; j >= 1; j--)
      a[j][i] = cnt++;
  }

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= m; j++)
      cout << a[i][j] << ' ';
    cout << endl;
  }
}
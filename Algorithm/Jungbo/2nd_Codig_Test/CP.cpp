#include <iostream>
using namespace std;
int main()
{
  int a[101][101];
  int i, j, n, cnt = 1;
  cin >> n;

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
      a[j][i] = cnt++;
  }

  for (i = 1; i <= n; i++)
  {
    for (j = 1; j <= n; j++)
      cout << a[i][j] << ' ';
    cout << endl;
  }
}
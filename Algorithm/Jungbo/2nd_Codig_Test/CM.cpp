#include <iostream>
using namespace std;

int list[10000001] = {};

int main()
{
  int n, m, idx;
  cin >> n;

  for (int i = 0; i < n; i++)
  {
    cin >> idx;
    list[idx] = 1;
  }

  cin >> m;

  for (int i = 0; i < m; i++)
  {
    cin >> idx;
    cout << list[idx] << endl;
  }
}
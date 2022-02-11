#include <iostream>
using namespace std;
int main()
{
  int arr[7] = {}, n, t;
  cin >> n;
  for (int i = 1; i <= n; i++)
  {
    cin >> t;
    arr[t] += 1;
  }
  for (int i = 1; i <= 6; i++)
    cout << arr[i] << ' ';
  cout << endl;
}

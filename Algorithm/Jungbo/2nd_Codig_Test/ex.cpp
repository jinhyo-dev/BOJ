#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int num)
{
  if (num < 2)
    return false;
  int a = (int)sqrt(num);
  for (int i = 2; i <= a; i++)
    if (num % i == 0)
      return false;
  return true;
}

int main()
{
  int arr[10000] = {}, n, tmp = 0, cnt = 0;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  for (int i = 0; i < n; i++)
  {
    if (is_prime(arr[i]))
      cnt++;
    else 
      continue;
  }
  cout << cnt << endl;
}
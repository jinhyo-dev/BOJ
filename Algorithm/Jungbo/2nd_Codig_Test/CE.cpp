#include <iostream>
using namespace std;
int main()
{
  int arr[1000000] = {}, n;
  cin >> n;
  for (int i = 0; i < n; i++) 
    cin >> arr[i];
  for (int i = 0; i < n; i++)
    cout << arr[i] << ' ';
}
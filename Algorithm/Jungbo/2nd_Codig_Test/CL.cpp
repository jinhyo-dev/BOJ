#include <iostream>
using namespace std;
int main()
{
  int arr[10] = {}, max = -100000, maxPoint = 0;
  for (int i = 0; i < 9; i++)
    cin >> arr[i];

  for (int i = 0; i < 9; i++)
  {
    if (arr[i] > max)
    {
      max = arr[i];
      maxPoint = i+1;
    }
  }

  cout << max << endl
       << maxPoint << endl;
}
#include <iostream>
using namespace std;
int f(int k)
{
	int i, sum = 0;
	for (i = 1; i <= k; i++)
		sum += i;
	return sum;
}
int main()
{
	int n;
	cin >> n;
	cout << f(n) << endl;
}
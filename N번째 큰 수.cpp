#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int num[2250010] = {};
	int N;
	cin >> N;
	int p = pow(N, 2);
	
	for(int i = 0; i < p; i++)
		cin >> num[i];
		
	sort(num, num+p);	

	cout << num[p-N] << endl;
}
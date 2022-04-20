#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int t, n;
    char A[1000];
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        cin >> A;
        for (int j = 0; j < strlen(A); j++)
        {
            for (int k = 0; k < n; k++)
                cout << A[j];
        }
        cout << endl;
    }
}
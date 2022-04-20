// OX퀴즈
#include <iostream>
using namespace std;
int main()
{
    int t, sum = 0, cnt = 0;
    string str;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        sum = 0, cnt = 0;
        cin >> str;
        for (int j = 0; j < str.length(); j++)
        {
            if (str.at(j) == 'O')
                cnt++;
            else
                cnt = 0;
            sum += cnt;
        }
        cout << sum << endl;
    }
}
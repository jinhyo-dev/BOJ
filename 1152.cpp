#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int cnt = 0;
    string str;
    getline(cin, str);
    if (str.empty())
        cout << "0";

    cnt = 1;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == ' ')
            cnt++;
    }

    if (str[0] == ' ')
        cnt--;

    if (str[str.length() - 1] == ' ')
        cnt--;

    cout << cnt;
}
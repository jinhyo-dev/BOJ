#include <iostream>
#include <string>
using namespace std;
int main()
{
    string str;
    string alp = "abcdefghijklmnopqrstuvwxyz";
    cin >> str;
    for (int i = 0; i < alp.length(); i++)
        cout << (int)str.find(alp[i]) << ' ';
    cout << endl;
}
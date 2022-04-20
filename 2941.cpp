#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<string> croatian = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int index;
    string str;
    cin >> str;

    for (int i = 0; i < croatian.size(); i++)
    {
        while (1)
        {
            index = str.find(croatian[i]);
            if (index == string::npos)
                break;
            str.replace(index, croatian[i].length(), "#");
        }
    }
    cout << str.length();
}
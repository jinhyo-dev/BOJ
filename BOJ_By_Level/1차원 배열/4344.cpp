#include <iostream>
using namespace std;

int main()
{
    int t, n, avg = 0;
    double percentage = 0, cnt = 0;
    int score[1000000];
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        int sum = 0;
        for (int j = 0; j < n; j++)
        {
            cin >> score[j];
            sum += score[j];
        }

        avg = sum / n;
        cnt = 0;

        for (int k = 0; k < n; k++)
        {
            if (score[k] > avg)
                cnt++;
        }

        percentage = (cnt / n) * 100;

        cout << fixed;
        cout.precision(3);
        cout << percentage << "%" << endl;
    }
}
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> g1;

    for (int i = 1; i <= 10; i++)
        g1.push_back(i * 100);

    // g1.push_back('c');

    for (auto &x : g1)
    {
        x = 10;
        cout << x << endl;
    }
    cout << "Original vector";
    for (auto x : g1)
    {
        cout << x << endl;
    }
    return 0;
}

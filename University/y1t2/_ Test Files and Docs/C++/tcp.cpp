#include <bits/stdc++.h>
using namespace std;

const int MXN = 1e5 + 5, INF = 1e9 + 5;

#define all(x) (x).begin(), (x).end()
#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define pb push_back
#define mp make_pair
#define ull unsigned long long
#define endl "\n"
#define ios                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);

template <class T>
void print_array(T arr[], int size_arr)
{
    for (int i = 0; i < size_arr; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

template <class T>
void print_vector(vector<T> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}

void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T)
{
    cerr << ' ' << H;
    dbg_out(T...);
}
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

void solve()
{
    ll i = 345363;
    dbg(i);
}

int main()
{
    ios;
    int TC = 1;
    // cin >> TC;
    while (TC--)
        solve();
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);  

    int year; cin >> year;
    while (true) {
        string ny = to_string(++year);
        set<char> se(all(ny));
        if (sz(se) == 4) {
            cout << ny;
            break;
        }
    }
    return 0;
}
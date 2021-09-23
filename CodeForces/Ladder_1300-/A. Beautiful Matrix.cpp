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
    int m = 5, n = 5;
    int x = 0, y = 0;
    rep(i, 0, 5) {
        rep(j, 0, 5) {
            int val;
            cin >> val;
            if (val == 1) {
                x = i, y = j;
            }
        }
    }
    cout << abs(x-2)+abs(y-2);
    return 0;
}
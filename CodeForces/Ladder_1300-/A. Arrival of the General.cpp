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

    int n; cin >> n;
    vi aa(n); int max_idx = 0, min_idx = 0;
    rep(i, 0, n) {
        cin >> aa[i];
        if (aa[i] > aa[max_idx]) {max_idx = i;};
        if (aa[i] <= aa[min_idx]) {min_idx = i;};
    };

    if (min_idx  > max_idx) {
        cout << max_idx+n-1-min_idx;
    } else {cout << max_idx+n-1-min_idx-1;}

    return 0;
}
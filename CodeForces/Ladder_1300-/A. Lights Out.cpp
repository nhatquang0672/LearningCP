#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vi di{-1,0,1,0}, dj{0,1,0,-1};

bool ok(int x, int y) {
    return 0 <= x && x < 3 && 0 <= y && y < 3;
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);  

    int m=3, n=3;
    vector<vi> lights(m, vi(n, 0));
    rep(i, 0, 3) {
        rep(j, 0, 3) { 
            int x; cin >> x;
            lights[i][j] += x;
            rep (t, 0, 4) {
                if (ok(i+di[t],j+dj[t])) {lights[i+di[t]][j+dj[t]] += x;}
            }
        }
    }
    rep(i, 0, 3) {
        rep(j, 0, 3) {
            lights[i][j] = lights[i][j] % 2 == 0 ? 1 : 0;
            cout<<lights[i][j];
        }
        cout << endl;
    }
    return 0;
}
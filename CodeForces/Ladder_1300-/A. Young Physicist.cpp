#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n, x, y, z, xx = 0, yy = 0, zz = 0;

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);    

    cin >> n;
    while (n--) {
        cin >> x >> y >> z;
        xx += x; 
        yy += y;
        zz += z;
    }
    if (xx == 0 && yy == 0 &&  zz == 0) {
        cout <<"YES";
    } else {
        cout << "NO";
    }

    return 0;
}

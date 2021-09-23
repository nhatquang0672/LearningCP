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

    string s; cin >> s;
    vi lower{}, upper{};

    rep(i,0,sz(s)) {
        if ((int)s[i] < 97) {
            upper.push_back(i);
        } else {
            lower.push_back(i);
        }
    }
    if (sz(upper)>sz(lower)) {
        trav(a, lower) {
            s[a] = toupper(s[a]);
        }
    } else {
        trav(a, upper) {
            s[a] = tolower(s[a]);
        }
    }

    cout << s;

    return 0;
}
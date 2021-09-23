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
    
    string s, ans; cin >> s; 
    int m = sz(s), i = 0, len = 1;
    
    map<string, string> msi = {{".", "0"}, {"-.", "1"}, {"--", "2"}};
    while (i<m) {
        len = s[i] == '.' ? 1 : 2;
        ans += msi[s.substr(i, len)];
        i += len;
    }
    cout << ans;
    return 0;
}
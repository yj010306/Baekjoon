#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int s_len[51] = {0,};

int pplus(int a){
    int sum = 0;
    for(int i=1; i<a; i++){
        sum += s_len[i];
    }
    return sum;
}

int main() {
    vector<string> v;
    vector<string> v_ans;
    int n;
    int cnt = 1;
    string s;

    cin >> n;
    
    for(int i=0; i<n ;i++){
        cin >>s;
        s_len[s.length()]++;
        v.insert(v.begin()+ pplus(s.length()),s);
    }

    for(int i=1; i<51; i++){
        sort(v.begin()+pplus(i),v.begin()+pplus(i+1));
    }

    v_ans.push_back(v[0]);
    if(n>1) {
        for (int i = 1; i < n; i++) {
            if (v[i - 1] != v[i]) {
                v_ans.push_back(v[i]);
                cnt++;
            }
        }
    }

    for(int i=0; i<cnt; i++){
        cout << v_ans[i] << endl;
    }
  
    return 0;
}

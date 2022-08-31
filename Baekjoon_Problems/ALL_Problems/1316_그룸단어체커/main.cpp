#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

vector<char> word_tmp;

bool check(char a){
    for(int i=0; i<word_tmp.size(); i++){
        if(word_tmp[i] == a) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    char word_arr[105] = { 0, };
    int test_cnt=0;
    int ans =0;
    string s;

    cin >> n;

    for(int i=0; i<n; i++){
        cin >> s;
        s.copy(word_arr,s.length()+1);

        for(int j=0; j<s.length(); j++){
            if(word_arr[j] != word_arr[j+1] && check(word_arr[j])== true){
                word_tmp.push_back(word_arr[j]);
            }
            else if(word_arr[j] != word_arr[j+1] && check(word_arr[j])== false){
                break;
            }
            test_cnt++;
        }
        if(test_cnt == s.length()) {
            ans++;
        }
        test_cnt=0;
        word_tmp.clear();
        memset(word_arr, 0, 105);


    }

    cout << ans << endl;
    return 0;
}

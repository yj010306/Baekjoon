#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main() {
    int n, ans;
    int check=0;
    int cnt=0;
    string s;

    cin >> n;
    for(int i=666; ; i++){
        if(cnt == n){
            ans = i-1;
            break;
        }

        s = to_string(i);       //  'int' to 'string'
        char *arr = new char[s.length()];       //  배열 동적할당;
        strcpy(arr,s.c_str());      //  'string' to 'char'

        for(int j=2; j<s.length(); j++){
            if(arr[j] == '6' && arr[j-1] == '6' && arr[j-2] == '6') check = 1;
        }
        if(check == 1) cnt++;

        check = 0;

    }

    cout << ans << endl;

    return 0;
}

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

char word_arr[100000] = {0,};       // 입력받은 문자열을 char형으로 바꾼 값을 저장하는 배열
char chg_word_arr[100000] = {0,};   // 문자열을 거꾸로 읽었을때의 값을 저장하는 배열

string chg_word(string a){      // 문자열을 전달받아 해당 문자열을 거꾸로 읽었을 때의 값을 문자열로 반환함
    int cnt = 0;
    int word_len = a.length();
    strcpy(word_arr,a.c_str());
    for(int i=word_len-1; i>=0; i--){
        chg_word_arr[cnt]=word_arr[i];
        cnt++;
    }
    string changedWord(chg_word_arr);
    return changedWord;
}

int main() {
    string s;
    for(;;){
        cin >> s;
        if(s == "0") break;
        if(s == chg_word(s)) cout << "yes" << endl;
        else cout << "no" << endl;
        memset(word_arr,0,sizeof (word_arr));       // 배열 초기화
        memset(chg_word_arr,0,sizeof (word_arr));   // 배열 초기화
    }

    return 0;
}

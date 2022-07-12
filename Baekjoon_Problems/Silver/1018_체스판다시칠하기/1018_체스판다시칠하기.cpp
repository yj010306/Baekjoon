#include <iostream>
#include <algorithm>

using namespace std;

char arr[50][50];       // 입력받을 2차원 배열 선언
int cnt=0;      // 비교 배열과 다른 값의 개수를 세는 변수 ( 함수 compare_w, compare_b 에서 사용 )
char w_start_arr[8][9] = {"WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"};      // 'W'로 시작하는 배열의 비교 배열
char b_start_arr[8][9] = { "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"};     // 'B'로 시작하는 배열의 비교 배열

int compare_w(int a, int b) {       // 'W'로 시작하는 배열을 비교하는 함수
    cnt = 0;
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            if(arr[i+a][j+b] != w_start_arr[i][j]) cnt++;
        }
    }
    return cnt;
}
int compare_b(int a, int b) {       // 'B'로 시작하는 배열을 비교하는 함수
    cnt = 0;
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            if(arr[i+a][j+b] != b_start_arr[i][j]) cnt++;
        }
    }
    return cnt;
}

int main() {
    int Min = 100;
    int m,n;
    cin >> n >> m;

    for(int i=0; i<n; i++) {
            scanf("%s", arr[i]);
    }

    for(int i=0; i<=n-8; i++){
        for(int j=0; j<=m-8; j++){
                Min = min(Min, compare_w(i,j));     // 둘 다 확인 ( )
                Min = min(Min, compare_b(i,j));     // 둘 다 확인 ( )
        }
    }

    cout << Min << endl;

    return 0;
}

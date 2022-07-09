#include <iostream>
#include <cmath>

using namespace std;

int compare(int a, int b) {     // 두 수를 비교해서 더 작은 수를 반환하는 함수.
    return min(a,b);
}

int main() {
    int x,y,w,h;
    int Min = 1000;     // 처음으로 비교하는 숫자는 무조건 최솟값이 되어야 하기 때문에 Min의 초기값을 1000으로 설정

    cin >> x >> y >> w >> h;      // 입력

    Min = compare(Min,x);       
    Min = compare(Min,y);
    Min = compare(Min,w-x);      // 코드가 위에서 차례로 실행됨
    Min = compare(Min,h-y);      // 결국 x, y, w-x, h-y를 전부 비교하는 셈.( 비교해야 하는 숫자가 많아지면 어떻게 해야할까...? )

    cout << Min << endl;

    return 0;
}

#include <iostream>
#include <cmath>

using namespace std;

int compare(int a, int b) {     // �� ���� ���ؼ� �� ���� ���� ��ȯ�ϴ� �Լ�.
    return min(a,b);
}

int main() {
    int x,y,w,h;
    int Min = 1000;     // ó������ ���ϴ� ���ڴ� ������ �ּڰ��� �Ǿ�� �ϱ� ������ Min�� �ʱⰪ�� 1000���� ����

    cin >> x >> y >> w >> h;

    Min = compare(Min,x);
    Min = compare(Min,y);
    Min = compare(Min,w-x);
    Min = compare(Min,h-y);

    cout << Min << endl;

    return 0;
}

---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 52장 ~ 53장"
category : algorithm
date : 2020-06-21 17:00
---

오늘도 따라하며 배우는 알고리즘!! Keep Going!

## 52장. Ugly Numbers

어떤 수를 소인수분해 했을 때 그 소인수가 2 또는 3 또는 5로만 이루어진 수를 Ugly Number라고 부른다. Ugly Number를 차례대로 적어보면
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ... 이다. 숫자 1은 Ugly Number의 첫 번째 수로 한다.

자연수 N이 주어지면 Ugly Number를 차례로 적을 때 N번째 Ugly Number를 구하는 프로그램을 작성하세요.

> 입력

첫 줄에 자연수 N(3<=N<=1500)이 주어진다.

> 출력

첫 줄에 N번째 Ugly Number를 출력하세요.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int arr[1501];

bool isUglyNum(int x);

int main(){
    int N;
    int cnt = 0;
    
    cin >> N;
    
    int i = 1;
    while(1){
        if(isUglyNum(i)){
            cnt++;
        }
        
        if(cnt == N){
            cout << i << endl;
            break;
        }
        i++;
    }
    
    return 0;
}

bool isUglyNum(int x){
    if(x == 1)
        return true;
    
    int i = 2;
    int tmp = x;
    while(1){
        if(tmp%i == 0){
            tmp = tmp/i;
        }else
            i++;
        if(tmp==1)
            break;
        if(i > 5)
            return false;
    }
    return true;
}
```

잘 돌아간다. 근데 숫자를 크게 하면 time out error날 듯. (1초 안에 안나온다.)
처음에는 dynamic programming을 사용하면 될 것 같다는 느낌이 들긴 했는데, 어떻게 DP를 사용해야할지 감이 안온다. 선생님 강의를 확인해 보아야 할 듯!
 

### 선생님 코드

1500 입력 하면 8억 5천까지의 수를 다 소인수 분해해야함 ㅋㅋㅋㅋㅋ 오마이갓~

**투포인트 알고리즘**을 이용하면 된다. 

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int a[1501];
int main(){
    freopen("input.txt", "rt", stdin);
    int n, i, p2, p3, p5, min = 2147000000;

    scanf("%d", &n);
    a[1] = 1;
    p2=p3=p5=1;

    for(i = 2; i <= n; i++){
        if(a[p2]*2 < a[p3]*3) mint = a[p2] * 2;
        else min = a[p3]*3;
        if(a[p5]*5 < min) min = a[p5]*5;

        if(a[p2]*2 == min) p2++;
        if(a[p3]*3 == min) p3++;
        if(a[p5]*5 == min) p5++;
        a[i] = min; 
    }
    printf("%d", a[n]);
    return 0;
}
```

p2, p3, p5라는 포인터를 주었다. 각 배수의 값대로 슝슝 하면 훨씬 빠르게 돌 수 있음!!


## 53장. K진수 출력

10진수 N이 입력되면 K진수 변환하여 출력하는 프로그램을 작성하세요. 스택 자료구조를 사용하시길 바랍니다.

> 입력

첫 번째 줄에 10진수 N(10<=N<=1,000)과 K(2, 5, 8, 16)가 주어진다.

> 출력

K진수를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, K;
    vector <int> result;
    
    cin >> N >> K;
    
    int tmp = N;
    while(1){
        if(tmp/K != 0){
            result.push_back(tmp%K);
            tmp = tmp/K;
        }else{
            result.push_back(tmp);
            break;
        }
    }
    
    if(K == 16){
        for(int i=result.size()-1; i>=0; i--){
            if(result[i] >= 10){
                char s = result[i] - 10 + 'A';
                printf("%c", s);
            }else{
                cout << result[i];
            }
        }
        cout << endl;
    }else{
        for(int i=result.size()-1; i >= 0; i--){
            cout << result[i];
        }
        cout << endl;
    }
    
    
    return 0;
}
```

16진수 바꾸는 부분만 살짝 손봄. 근데 `#include <stdio.h>` 안써줘도 잘 돌아가네 ?!
이거는 크게 어렵지 않을 것 같아서 강의는 따로 듣지 않음!

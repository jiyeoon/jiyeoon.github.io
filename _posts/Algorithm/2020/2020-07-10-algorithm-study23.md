---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 76장"
date : 2020-07-10 17:00
category : algorithm
---

## 76장. 이항계수 (메모이제이션)

이항계수 N개의 원소를 가지는 집합에서 R개의 원소를 뽑아 부분집합을 만드는 경우의 수를 의미한다. 공식은 nCr로 표현된다.

N과 R이 주어지면 이항계수를 구하는 프로그램을 작성하세요.

> 입력

첫 번째 줄에 자연수 N(1<=N<=20)과 R(0<=R<=20)이 주어진다. 단, N>=R

> 출력

첫 번째 줄에 이항계수 값을 출력한다.


### 나의 코드

```c++
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int getFac(int n);
int getC(int n, int r);

int main(){
    int N, R;
    cin >> N >> R;
    
    cout << getC(N, R) << endl;
    
    return 0;
}

int getFac(int n){
    int result = 1;
    for(int i=1; i<=n; i++){
        result *= i;
    }
    return result;
}

int getC(int n, int r){
    int result = 1;
    
    for(int i=n; i>=n-r+1; i--){
        result = result * i;
    }
    
    result = result / getFac(r);
    
    return result;
}
```


---


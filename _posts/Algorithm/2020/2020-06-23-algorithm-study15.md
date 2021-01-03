---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 56장 ~ 57장"
category : algorithm
date : 2020-06-23 20:00
---

오늘도 계속 하는 알고리즘!!! No Pain No Gain!!!!!

# 56장. 재귀함수 분석

자연수 N이 주어지면 아래와 같이 출력하는 프로그램을 작성하세요

> 입력

첫 번째 줄에 자연수 N(1<=N<=20)이 주어진다.

(예시)
```
3
```

> 출력

첫 번째 줄에 재귀함수를 이용해 출력한다.

```
1 2 3
```

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print_num(int x);

int main(){
    int N;
    
    cin >> N;
    
    print_num(N);
    
    return 0;
}

void print_num(int x){
    if(x == 1){
        cout << "1" << " ";
        return;
    }else{
        print_num(x-1);
        cout << x << " ";
    }
}
```

별거 아닌데 처음에 조금 헤맸다. (ㅠㅠ)

---

# 57장. 재귀함수 이진수 출력

10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
단, 재귀함수를 이용해서 출력해야 합니다.

> 입력

첫 번째 줄에 10진수 (1<=N<=1,000)이 주어집니다.

> 출력

첫 번째 줄에 이진수를 출력하세요.

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


string binary(int x);

int main(){
    int N;
    
    cin >> N;
    
    cout << binary(N) << endl;
    
    return 0;
}

string binary(int x){
    int tmp;
    if(x/2==0){
        tmp = x%2;
        return to_string(tmp);
    }else{
        tmp = x%2;
        return binary(x/2) + to_string(tmp);
    }
}
```

쉽게 함!! string으로 받아서 쉽게 했다. 정수로 했다면 조금 더 오래 걸리지 않았을까..?
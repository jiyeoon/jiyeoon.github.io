---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 73장~"
category : algorithm
date : 2020-07-08 21:00
---

오늘도 한다 알고리즘!!!

## 73장. 최대힙(priority_queue : 우선순위 큐)

최대힙은 완전이진트리로 구현된 자료구조입니다. 그 구성은 부모 노드 값이 왼쪽 자식과 오른쪽 자식 노드의 값보다 크게 트리를 구성하는 것입니다. 그렇개 하면 트리의 루트(root) 노드는 입력된 값들 중 가장 큰 값이 저장되어 있습니다. 예를들어 5 3 2 1 4 6 7 순으로 입력되면 최대힙 트리는 아래와 같이 구성됩니다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FcXm20R%2FbtqFrT3aCJY%2FuKrLYn7Qgnu0f8l97gul90%2Fimg.png)

최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.

1) 자연수가 입력되면 최대힙에 입력한다.
2) 숫자 0이 입력되면 최대 힙에서 최댓값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램을 종료한다.

> 입력

첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.

> 출력

2) 연산을 한 결과를 보여준다.

### 나의 코드

나는.. 못풀었다. 선생님 코드를 바로 보면

### 선생님 코드

여기서 Key Point는 **priority_queue는 이미 stl에 정의되어 있다는 점!!**
그냥 있는 것을 가져다가 쓰면 된다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    //freopen("input.txt", "rt", stdin);
    int a;
    priority_queue<int> pQ;
    
    while(true){
        scanf("%d", &a);
        if(a==-1){
            break;
        }
        if(a==0){
            if(pQ.empty())
                printf("-1\n");
            else{
                printf("%d\n", pQ.top());
                pQ.pop();
            }
        }else{
            pQ.push(a);
        }
    }
    return 0;
}
```

잊지말자 `priority_queue <int> pQ;`...


---

## 74장. 최소힙 (priority_queue : 우선순위 큐)

최소힙은 완전 이진트리로 구현된 자료구조입니다. 그 구성은 부모 노드 값이 왼쪽자식과 오른쪽 자식 노드의 값보다 작게 트리를 구성하는 것입니다. 그렇게 하면 트리의 루트(root) 노드는 입력된 값들 중 가장 작은 값이 저장되어 있습니다. 예를 들어 5 3 2 1 4 6 7 순으로 입력되면 최소 힙 트리는 아래와 같이 구성됩니다. 

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FkIWiN%2FbtqFvIkVz0f%2FKgdfsk1WqL2QM8dpSe1MZ0%2Fimg.png)

최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.

1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램을 종료한다.

> 입력

첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자가 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.

> 출력

2) 연산을 한 결과를 보여준다.


### 나의 코드

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    //freopen("input.txt", "rt", stdin);
    int a;
    priority_queue<int, vector<int>, greater<int>> pQ;
    
    while(true){
        scanf("%d", &a);
        if(a==-1){
            break;
        }
        if(a==0){
            if(pQ.empty())
                printf("-1\n");
            else{
                printf("%d\n", pQ.top());
                pQ.pop();
            }
        }else{
            pQ.push(a);
        }
    }
    return 0;
}
```

priority_queue를 선언할 때 `priority_queue<int, vector<int>, greater<int>> pQ;`라고 선언 하면 된다!! (왕신기)

---

### 선생님 코드

와 선생님은 완전 신기하게 푸셨다...
음수 처리 해버리면 됨!!!

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    //freopen("input.txt", "rt", stdin);
    int a;
    priority_queue<int> pQ;
    
    while(true){
        scanf("%d", &a);
        if(a==-1){
            break;
        }
        if(a==0){
            if(pQ.empty())
                printf("-1\n");
            else{
                printf("%d\n", -pQ.top());
                pQ.pop();
            }
        }else{
            pQ.push(-a);
        }
    }
    return 0;
}
```

그냥 마이너스만 넣어버리셨다. 역시.. 선생님은 천재야

---

## 75장. 최대 수업 스케줄 (priority_queue 응용 문제)

현수는 유명한 강연자이다. N개의 기업에서 강연 요청을 해왔다. 각 기업은 D일 안에 와서 강연을 해주면 M만큼의 강연료를 주기로 했다.
각 기업이 요청한 D와 M를 바탕으로 가장 많은 돈을 벌 수 있도록 강연 스케줄을 짜야한다.

단, 강연의 특성상 현수는 하루에 하나의 기업에서만 강연을 할 수 있다.

> 입력

첫 번째 줄에 자연수 N(1<=N<=10,000)이 주어지고, 다음 N개의 줄에 M(1<=M<=10,000)과 D(1<=D<=10,000)이 차례로 주어진다.

> 출력

첫 번째 줄에 최대로 벌 수 있는 수입을 출력한다.

### 나의 코드

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    //freopen("input.txt", "rt", stdin);
    int N, M, D;
    priority_queue<pair<int, int>> pQ;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> M >> D;
        pair<int, int> p;
        p.first = M; p.second = D;
        pQ.push(p);
    }
    
    int result = 0;
    int day = N;
    
    while(day > 0 && !pQ.empty()){
        pair<int, int> p;
        p = pQ.top();
        pQ.pop();
        if(day - p.second >= 0){
            result += p.first;
            day -= p.second;
        }else{
            continue;
        }
    }
    
    
    cout << result << endl;
    return 0;
}

/*
 input
 6
 50 2
 20 1
 40 2
 60 3
 30 3
 30 1 
 */
```

나는 이렇게 했는데.. 틀린거다!!
first랑 second를 비교하고 가장 최선의 값을 선택해주어야하는데 나는 틀림.. 선생님 코드를 보도록 하자.


### 선생님 코드

```c++
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

struct Data{
    int money;
    int when;
    Data (int a, int b){
        money = a;
        when = b;
    }
    bool operator < (Data &b){
        return when > b.when;
    }
};

int main(){
    int n, i, j, a, b, res=0, max = -2147000000;
    vector<Data> T;
    priority_queue<int> pQ;
    
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        scanf("%d %d", &a, &b);
        T.push_back(Data(a, b));
        if(b>max)
            max = b;
    }
    sort(T.begin(), T.end());
    j = 0;
    for(i=max; i>=1; i--){ //i는 날짜. 날짜는 뒤에서부터 확인한다.
        for(; j<n; j++){
            if(T[j].when < i) break; // 날짜가 작으면 그냥 스루해버린다~
            pQ.push(T[j].money);
        }
        if(!pQ.empty()){
            res += pQ.top();
            pQ.pop();
        }
    }
    printf("%d\n", res);
    return 0;
}
```

이렇게 된다!!! 사실 아직 저 for문 부분을 이해를 하질 못하겠다. (,,)
`bool operator < ` 선언해준 것으로 저렇게 sort가 되는 것도 넘 신기하다.
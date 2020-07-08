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

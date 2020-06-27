---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 62장 ~ 63장"
category : algorithm
date : 2020-06-27 22:00
---

## 62장. 병합정렬

N개의 숫자가 입력되면 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요
정렬하는 방법은 병합정렬입니다.

> 입력 

첫 번째 줄에는 자연수 N(1<=N<=100)이 주어집니다
두 번째 줄에는 N개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 정수형 범위 안에 있습니다.

> 출력 설명

오름차순으로 정렬된 수열을 출력합니다.


*여기선.. 병합정렬을 몰라서 fail. 병합정렬에 대해서 알아보도록 하자*

### 병합정렬이란? (Merge Sort)

합병정렬이라고도 한다. 오름차순으로 정렬하는 알고리즘이다. 

**분할정복** 알고리즘의 하나로, 하나의 리스트를 두개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 정렬된 리스트가 되게 하는 방법이다.

> 분할정복(divide and conquer) 방법

- 문제를 2개의 작은 문제로 분리하고 각각을 해결한 다음 결과를 모아서 원래의 문제를 해결하는 전략
- 분할 정복 방법은 대개 순환 호출을 이용하여 구현한다.

![img](https://gmlwjd9405.github.io/images/algorithm-merge-sort/merge-sort-concepts.png)

합병 정렬은 아래와 같은 단계로 이루어진다. 

1. 분할(Divide) : 입력 배열을 같은 크기의 2개의 부분 배열로 분할한다.
2. 정복(Conquer) : 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 정복 방법을 적용한다.
3. 결합(Combine) : 정렬된 부분 배열들을 하나의 배열에 합병한다.

여기서 두개의 리스트를 합병(merge) 하는 과정은 두개의 리스트를 처음부터 하나씩 비교하여 두 개의 리스트 값 중에서 작은 값을 새로운 리스트로 옮기는 것이다.

### 내가 푼 문제 코드

는 없다..
개념을 알아도 구현을 못했다 ㅋ 선생님 코드를 보도록 하자.


### 선생님 코드

```c++
#include <stdio.h>
int data[10], tmp[10];

void divide(int lt, int rt){
    int mid;
    int p1, p2, p3;
    if(lt<rt){
        mid = (lt+rt)/2;
        divide(lt, mid);
        divide(mid+1, rt);

        p1 = lt; p2 = mid+1; p3 = lt;

        while(p1<=mid && p2 <= rt){
            if(data[p1] < data[p2])
                tmp[p3++] = data[p1++];
            else
                tmp[p3++] = data[p2++];
        }
        while(p1 <= mid) tmp[p3++] = data[p1++];
        while(p2 <= rt) tmp[p3++] = data[p2++];

        for(int i=lt; i<=rt; i++){
            data[i] = tmp[i];
        }
    }
}

int main(){
    int n, i;
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        scanf("%d", &data[i]);
    }
    divide(n, 1);
    for(i=1; i<=n; i++){
        printf("%d ", data[i]);
    }
    return 0;
}
```
역시~ 선생님은 멋있다!! 저 `divide(int lt, int rt)` 함수가 간지!!

---

## 63장. 인접 행렬(가중치 방향 그래프)

아래 그림과 같은 그래프 정보를 인접행렬로 표현해보세요

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FlmJXX%2FbtqFbjs4BZ9%2F3AClFFsAr5WllG0nFxffZk%2Fimg.png)

> 입력

첫째줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보와 거리비용이 주어진다.

> 출력

인접 행렬을 출력하세요


```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int N, M;
    int to, from, weight;
    int adj[21][21];
    cin >> N >> M;
    
    for(int i=0; i<M; i++){
        cin >> to >> from >> weight;
        adj[to][from] = weight;
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<= N; j++){
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}

/* input
 6 9
 1 2 7
 1 3 4
 2 1 2
 2 3 5
 2 5 5
 3 4 5
 4 2 2
 4 5 5
 6 4 5
 */
```

잘 출력된다!
예전에 인접행렬은 전역변수로 뺐던 것 같은데, 이번에는 그냥 그대로 했네.. ㅇㅅㅇ; 지역변수면 좋지 뭐~
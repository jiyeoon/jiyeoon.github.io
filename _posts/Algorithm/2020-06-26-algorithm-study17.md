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

### 병합정렬이란?






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
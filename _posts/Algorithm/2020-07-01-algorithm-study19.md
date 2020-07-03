---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 68장~69장"
category : algorithm
date : 2020-07-01 20:00
---


## 68장. 최소비용 (DFS : 가중치 방향그래프 인접리스트)

가중치 방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 최소비용을 출력하는 프로그램을 작성하세요.


> 입력

첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결 정보가 주어진다.

> 출력

총 가지수를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct node{
    int v;
    int weight;
}node;

vector<node> map[30];
int ch[30];

int minimum = 2147000000;
int sum = 0;

int N;

void DFS(int start){
    ch[start] = 1;
    if(start == N){
        if(minimum > sum){
            minimum = sum;
            //cout << "min : " << sum << endl;
        }
    }else{
        for(int i=0; i<map[start].size(); i++){
            if(ch[map[start][i].v] == 0){
                sum += map[start][i].weight;
                DFS(map[start][i].v);
                sum -= map[start][i].weight;
            }
        }
    }
    ch[start] = 0;
}

int main(){
    int M;
    int from, to, w;
    
    cin >> N >> M;
    for(int i=0; i<M; i++){
        cin >> from >> to >> w;
        node n;
        n.v = to;
        n.weight = w;
        map[from].push_back(n);
    }
    
    DFS(1);
    
    cout << minimum << endl;
    
}

/**
 5 8
 1 2 12
 1 3 6
 1 4 10
 2 3 2
 2 5 2
 3 4 3
 4 2 2
 4 5 5
 
 */
```

인접리스트를 활용했다!
선생님 코드도 뭐 크게 다르진 않았던 것 같은데.. 선생님은 `pair<int, int> p`라는 것을 사용함. (**pair는 stl에 있다.**)
나는 그냥 구조체를 만들어서 사용했다.


---

## 69장. 이진트리 넓이우선탐색 (BFS)

아래 그림과 같은 이진트리를 넓이 우선 탐색해보세요. 간선 정보 6개를 입력받아 처리해보세요.

### 선생님 코드

나는 구현을 제대로 못해서.. 선생님 코드를 확인해보자.
선생님은 큐를 직접 구현하셨는데, 사실 직접 구현할 필요까지는 없다. (stl에 있는 queue를 사용하면 된다)

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int Q[100], front=-1; back=-1; ch[10];

vector<int> map[10];

int main(){
    int i, a, b, x;
    for(i=1; i<=6; i++){
        scanf("%d %d", &a, &b);
        map[a].push_back(b);
        map[b].push_back(a);
    }
    Q[++back] = 1;
    ch[1] = 1;
    while(front<back){
        x = Q[++front];
        printf("%d ", x);
        for(i=0; i<map[x].size(); i++){
            if(ch[map[x][i]] == 0){
                ch[map[x][i]] = 1;
                Q[++back] = map[x][i];
            }
        }
    }
    return 0;
}
```

그냥 stl에 있는 queue를 쓰자! (뭔말인지 모르겠다!)



> 암튼 결론은..

아무튼 결론부터 말하자면!!

1. DFS : 최소비용 구할 때 => stack(=vector)를 사용. 재귀함수
2. BFS : 최단거리 구할 때 => Queue 사용. while문.


---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 70장 ~ "
category : algorithm
date : 2020-07-03 16:00
---

## 70장. 그래프 최단거리 (BFS)

다음 그래프에서 1번 정점에서 각 정점으로 가는 최소 이동 간선수를 출력하세요.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FblSKAu%2FbtqFnFogzEa%2FCPgKOO7XOQSWqM4aB6zLG0%2Fimg.png)


> 입력

첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결 정보가 주어진다.

> 출력

1번 정점에서 각 정점으로 가는 최소 간선수를 2번 정점부터 차례대로 출력하세요.

```c++
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
int N;
vector<int> map[21];
//int ch[21];

queue<int> jobs;

void BFS(int destination);

int main(){
    int M;
    int from, to;
    
    cin >> N >> M;
    for(int i=0; i<M; i++){
        cin >> from >> to;
        map[from].push_back(to);
    }
    
    for(int i=2; i<=N; i++){
        BFS(i);
    }
    
    return 0;
}

void BFS(int destination){
    int ch[N];
    int start = 1;
    ch[1] = 1;
    jobs.push(1);
    int cnt = 0;
    int cost = 0;
    while(jobs.size() != 0){
        cost++;
        start = jobs.front();
        for(int i=0; i<map[start].size(); i++){
            if(ch[map[start][i]] == 0){
                jobs.push(map[start][i]);
            }
        }
    }
}
```
하다가 못풀었다.
얘는 근데 DFS 써야 하는 문제 아님??!?!

---

## 71장. 송아지 찾기 (BFS : 상대트리검색)

현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려있다. 현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.

현수는 스카이콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성하세요.

> 입력

첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표점은 1부터 10,000까지이다.

> 출력

점프의 최소횟수를 구한다.

### 나의 코드


### 선생님 코드

```c++
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int ch[10001], d[3] = {1, -1, 5};

int main(){
    int s, e, x, pos, i;
    queue<int> Q;

    scanf("%d %d", &s, &e);

    ch[s] = 1;
    Q.push(s);
    while(!Q.empty()){
        x = Q.front();
        Q.pop();
        for(i=0; i<3; i++){
            pos = x + d[i];
            if(pos <= 0 || pos >10000) continue;
            if(pos == e){
                printf("%d\n", ch[x]);
                exit(0);
            }
            if(ch[pos] == 0){
                ch[pos] = ch[x] + 1; 
                Q.push(pos);
            }
        }
    }
}
```

와~~~ 선생님은 완전 천재적!!

여기서 포인트는 **Ch 배열이 거리 배열도 된다는 것!**

`ch[pos] = ch[x]+1`이라는 간단한 함수로 바로 만들어버릴 수 있다. 위의 문제도 마찬가지!
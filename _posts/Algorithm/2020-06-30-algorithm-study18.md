---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 66장 ~ 67장"
date : 2020-06-30 20:00
category : algorithm
---



## 66장. 경로 탐색 (DFS : 인접리스트 방법)

*64장 문제와 같은 문제! 이 문제는 인접 리스트를 활용해서 풀어보자.*

방향 그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지수를 출력하는 프로그램을 작성하세요.

> 입력

첫 째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보가 주어진다.

> 출력

총 가지수를 출력한다.


나는.. 인접리스트를 몰라서 바로 선생님 코드를 보도록 하자.

### 선생님 코드

```c++
#include <stdio.h>
#include <vector>

using namespace std;

int ch[30], cnt=0, n;

vector<int> map[30]; // 이게 인접리스트!!!

void DFS(int v){
    if(v==n){
        cnt++;
    }else{
        for(i=0; i<map[v].size();i++){
            if(ch[map[v][i]] == 0){
                ch[map[v][i]] = 1;
                DFS(map[v][i]);
                ch[map[v][i]] = 0;
            }
        }
    }
}

int main(){
    int m, i, a, b;
    scanf("%d %d", &n, &m);
    
    for(i=1; i<=m; i++){
        scanf("%d %d", &a, &b);
        map[a].push_back(b);
    }
    ch[1] = 1;
    DFS(1);
    printf("%d\n", cnt);
}
```

**인접리스트는 벡터를 이용해서 푼다!!**

인접행렬보다 훨씬 메모리도 적게 차지하고 탐색하는 시간도 빠르다. 
(예, 노드 1000개 간선 9개면 인접행렬은 그래도 1000x1000으로 하는데 인접리스트는 그렇지 않다.)



---

## 67장. 최소 비용(DFS : 인접행렬)

가중치 방향 그래프가 주어지면 1번 정점에서 N번 정점으로 가는 최소비용을 출력하는 프로그램을 작성하세요.

> 입력

첫 번째 줄에는 정점의 수 N(1<=N<=20)과 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보가 주어진다.

> 출력

총 가지수를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int adj[21][21];
int ch[21];

int minimum = 2147000000;
int sum = 0;

int N;

void DFS(int start);

int main(){
    int M;
    
    cin >> N >> M;
    
    for(int i=0; i<M; i++){
        int from, to, weight;
        cin >> from >> to >> weight;
        adj[from][to] = weight;
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }
    
    DFS(1);
    
    cout << minimum << endl;
    
    return 0;
}

void DFS(int start){
    ch[start] = 1;
    if(start == N){
        if(minimum > sum){
            cout << "sum : " << sum << endl;
            minimum = sum;
        }
    }else{
        for(int i=1; i<=N; i++){
            if(adj[start][i] != 0 && ch[i] == 0){
                sum += adj[start][i];
                DFS(i);
                sum -= adj[start][i];
            }
        }
    }
    ch[start] = 0;
}

/* input
 
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

오케이 풀었다!!!
포인트는 **check 배열!!!**


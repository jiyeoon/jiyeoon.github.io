---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 66장 ~ 67장"
date : 2020-06-30 20:00
category : algorithm
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
    
    return 0;
}

void DFS(int start){
    if(start == N){
        if(minimum > sum){
            minimum = sum;
        }
        sum = 0;
    }else{
        for(int i=1; i<=N; i++){
            if(adj[start][i] != 0){
                sum += adj[start][i];
                DFS(i);
                sum -= adj[start][i];
            }
        }
    }
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
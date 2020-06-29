---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 64장 ~ 65장"
category : algorithm
date : 2020-06-29 14:00
---

## 64장. 경로탐색 (DFS)

방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요. 아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지수는 ~~


> 입력

첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결 정보가 주어진다.

> 출력

총 가지수를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int adj[21][21];
int flag[21];
int N, M;
int cnt=0;

void DFS(int start);

int main() {
  cin >> N >> M;

  for(int i=0; i<M; i++){
    int from, to;
    cin >> from >> to;
    adj[from][to] = 1;
  }

  DFS(1);

  cout << cnt << endl;
}

void DFS(int start){
  flag[start] = 1;
  if(start == N){
    cnt++;
  }else{
    for(int i=1; i<=N; i++){
      if(flag[i] == 0 && adj[start][i] == 1){
        //cout << i << " ";
        DFS(i);
      }
    }
  }
  flag[start] = 0;
}

/* input
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
*/
```

DFS를 저렇게 푸는 것이 맞을지는 모르겠지만 암튼 풀었던 문제! 잘 작동하는 것 같다.

여기서 포인트는 **flag 변수**를 두어 이미 방문한 노드면 다시 방문하지 않도록 하는 것! 

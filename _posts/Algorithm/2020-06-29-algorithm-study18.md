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


### 선생님 코드

```c++
#include <stdio.h>

int map[30][30], ch[30], cnt=0;
int n;

void DFS(int v){
  if(v==n){
    cnt++;
  }else{
    for(int i=1; i<=n; i++){
      if(map[v][i] == 1 && ch[i] == 0){
        ch[i]=1;
        DFS(i);
        ch[i]=0;
      }
    }
  }
}

int main(){
  int m, i, a, b;
  scanf("%d %d", &n, &m);

  for(int i=0; i<m; i++){
    scanf("%d %d", &a, &b);
    map[a][b] = 1;
  }
  
  ch[1] = 1;
  DFS(1);
  printf("%d", cnt);
}
```

---

## 65장. 미로탐색(DFS)

7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요. 출발점은 격자의 (1, 1) 좌표이고 탈출 도착점은 (7, 7) 좌표이다. 격자판의 1은 벽이고, 0은 통로이다. 격자판의 움직임은 상하좌우로만 움직인다.

출발점에서 도착점까지 갈 수 있는 방법의 수는 여러개 나올 수 있습니다.

> 입력

첫 번째 줄부터 7*7 격자의 정보가 주어집니다.

> 출력

첫 번째 줄에 경로의 가지수를 출력한다.


```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int adj[9][9];
int cnt = 0;
int flag[8][8];

void DFS(int x, int y);

int main(){

  //input
  for(int i=1; i<=7; i++){
    for(int j=1; j<=7; j++){
      cin >> adj[i][j];
    }
  }

  DFS(1, 1);

  cout << cnt << endl;
}

void DFS(int x, int y){
  flag[x][y] = 1;
  if(x==7 && y==7){
    cnt++;
  }else{
    if(flag[x+1][y]==0 && adj[x+1][y] == 0){
      DFS(x+1, y);
    }
    if(flag[x][y+1]==0 && adj[x][y+1] == 0){
      DFS(x, y+1);
    }
    if(flag[x-1][y] == 0 && adj[x-1][y]==0){
      DFS(x-1, y);
    }
    if(flag[x][y-1] == 0 && adj[x][y-1] == 0){
      DFS(x, y-1);
    }
  }
  flag[x][y] = 0;
}

/*
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
*/
```

못풀었다!!!
선생님 코드를 확인해보자.

### 선생님 코드

```c++
#include <stdio.h>
int map[10][10], ch[10][10];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int cnt=0;

void DFS(int x, int y){
  int i, xx, yy;
  if(x==7 && y==7){
    cnt++;
  }else{
    for(i=0; i<4; i++){
      xx = x + dx[i];
      yy = y + dy[i];
      if(xx<1 || xx>7 || yy<1 || yy>7)
        continue;
      if(map[xx][yy] == 0 && ch[xx][yy] ==0){
        ch[xx][yy] = 1;
        DFS(xx, yy);
        ch[xx][yy] = 0;
      }
    }
  }
}

int main(){
  int i, j;
  for(int i=1; i<=7; i++){
    for(int j=1; j<=7; j++){
      scnaf("%d", &map[i][j]);
    }
  }
  ch[1][1] = 1;
  DFS(1, 1);
  printf("%d\n", cnt);
}
```

여기서 포인트는..!!!
**DFS(x, y)** 이렇게 쓴다는 것!!! 
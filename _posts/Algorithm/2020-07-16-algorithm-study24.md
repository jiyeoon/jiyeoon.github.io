---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 77장 "
category : algorithm
date : 2020-07-16 17:00
---

## 77장. 친구인가? (Union & Find 자료구조)

오늘은 새 학기 새로운 반에서 처음 시작하는 날이다. 현수네 반 학생은 N명이다. 현수는 각 학생들의 친구관계를 알고 싶다.

모든 학생은 1부터 N까지 번호가 부여되어 있고, 현수에게는 각각 두명의 학생은 친구관계가 번호로 표현된 숫자쌍이 주어진다. 만약 (1, 2), (2, 3), (3, 4)의 숫자쌍이 주어지면 1번 학생과 2번 학생이 친구이고, 2번 학생과 3번 학생이 친구, 3번 학생과 4번 학생이 친구이다. 그리고 1번 학생과 4번 학생은 2번과 3번을 통해서 친구관계가 된다.

학생의 친구관계를 나타내는 숫자쌍이 주어지면 특정 두 명이 친구인지를 판별하는 프로그램을 작성하세요. 두 학생이 친구이면 "YES", 아니면 "NO"를 출력합니다.

> 입력

첫 번째 줄에 반 학생수인 자연수 N(1<=N<=1,000)과 숫자쌍의 개수인 M(1<=M<=3,000)이 주어지고, 다음 M개의 줄에 걸쳐 숫자쌍이 주어진다.

마지막 줄에는 두 학생이 친구인지 확인하는 숫자쌍이 주어진다.

> 출력

첫 번째 줄에 "YES" 또는 "NO"를 출력한다.

> 입력 예제

```
9 7
1 2
2 3
3 4
4 5
6 7
7 8
8 9
3 8
```

> 출력 예제

```
NO
```

### 내가 푼 코드

```c++
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int adj[1001][1001];
int ch[1001];

int result = 0;

int from, to;
int N;
void isFriend(int start);

int main(){
    int M;
    int a, b;
    
    cin >> N >> M;
    
    for(int i=0; i<M; i++){
        cin >> a >> b;
        adj[a][b] = 1;
        adj[a][b] = 1;
    }
    
    cin >> from >> to;
    
    isFriend(from);
    
    if(result == 1){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    
    return 0;
    
}

void isFriend(int start){
    ch[start] = 1;
    if(start == to){
        result = 1;
    }else{
        for(int i=1; i<=N; i++){
            if(adj[start][i] == 1 && ch[i] == 0){
                isFriend(i);
            }
        }
    }
    ch[start] = 0;
}
```

저번에는 답이 안나왔었는데 이번에는 어떻게 저렇게 풀었다~! 결과값을 전역변수로 빼버리고 샤샤샥 풀어버리니 약간은 쉬움. 

근데 Union & Find라는 것이 뭔지 몰라서 강의를 들어야겠다.


## 78장. 원더랜드 (Kruskal MST 알고리즘 : Union & Find 활용)

원더랜드에 문제가 생겼다. 원더랜드의 각 도로를 유지보수하는 재정이 바닥난 것이다.

원더랜드는 모든 도시를 서로 연결하면서 최소의 유지비용이 들도록 도로를 선택하고 나머지 도로는 폐쇄하려고 한다. 어떤 도로는 도로를 유지보수하면 재정에 도움이 되는 도로도 존재한다. 재정에 도움이 되는 도로는 비용을 음수료 표현했다.

아래의 그림은 그 한 예를 설명하는 그림이다.

위의 지도는 각 도시가 1부터 9로 표현되었고, 지도의 오른쪽은 최소비용 196으로 모든 도시를 연결하는 방법을 찾아낸 것이다.

> 입력

첫째 줄에 도시의 개수 V(1<=V<=100)와 도로의 개수 E(1<=E<=1,000)가 주어진다. 다음 E개의 줄에는 각 도로에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 도시와 B번 도시가 유지비용이 C인 도로로 연결되어 있다는 의미다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

> 출력

모든 도시를 연결하면서 드는 최소 비용을 출력한다.

> 입력 예제

```
9 12
1 2 12
1 9 25
2 3 10
2 8 17
2 9 8
3 4 18
3 7 55
4 5 44
5 6 60
5 7 38
7 8 35
8 9 15
```

> 출력 예제

```
196
```

### 내가 푼 코드 

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int adj[101][101];
int ch[101];

int N;

int minimum = 2147000000;
int result = 0;

void getresult(int start);
bool isFullyChecked();

int main(){
    int E;
    int from, to, price;
    
    cin >> N >> E;
    
    for(int i=0; i<E; i++){
        cin >> from >> to >> price;
        adj[from][to] = price;
    }
    
    getresult(1);
    
    cout << minimum << endl;
    
}

void getresult(int start){
    ch[start] = 1;
    if(isFullyChecked()){
        cout << result << endl;
        if(result < minimum){
            minimum = result;
        }
    }else{
        for(int i=1; i<=N; i++){
            if(adj[start][i] != 0 && ch[i] == 0){
                result = result + adj[start][i];
                getresult(i);
                result = result - adj[start][i];
            }
        }
    }
    ch[start] = 0;
}

bool isFullyChecked(){
    for(int i=1; i <= N; i++){
        if(ch[i] == 0)
            return false;
    }
    return true;
}
```

답이 안나옴 ㅋ 다시 봐야겠다.

답이 안나온다..
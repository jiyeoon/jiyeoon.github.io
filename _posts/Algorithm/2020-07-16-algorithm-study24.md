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



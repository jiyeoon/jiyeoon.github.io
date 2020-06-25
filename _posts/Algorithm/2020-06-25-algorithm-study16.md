---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 58장 ~ 59장"
date : 2020-06-25 20:00
category : algorithm
---

## 58장. 이진트리 깊이우선탐색(DFS)

아래 그림과 같은 이진트리를 전위순회와 후위순회를 연습해보세요. 

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdCim19%2FbtqE8x5Zy2t%2F3mvmGuF1aAS4oNTzkSgnI1%2Fimg.png)

```c++
typedef struct node{
    node* left;
    node* right;
    int curr;
}
//전위순회
void dfs(node* n){
    dfs(n->left);
    cout << n->curr << " ";
    dfs(n->right);
}

//중위순회
void dfs(node* n){
    cout << n->curr << " ";
    dfs(n->left);
    dfs(n->right);
}

//후위순회
void dfs(node* n){
    dfs(n->left);
    dfs(n->right);
    cout << n->curr << " ";
}
```

뭔가... 예전에 자주 했었는데 까먹었다.
얘도 구글 면접에서 나왔던 건데.. (숙연)... 
사람이 발전이 없네 ㅇㅅㅠ

### 선생님 코드

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

void D(int v){
    if(v>7) return;
    else{
        D(v*2);
        printf("%d ", v);
        D(v*2+1);
    }
}

int main(){
    D(1);
    return 0;
}
```

선생님은 굉장히 특이한 방법으로 푸셨다. 재미있던 것은 왼쪽 노드는 현재\*2, 오른쪽 노드는 현재\*2+1로 계산하여 푸신 것. 

**Key Point**
1. `left = curr*2`, `right = curr*2 + 1`


---


## 59장. 부분집합(DFS)

자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요.

> 입력

첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

> 출력

첫 번째 줄부터 각각의 부분집합을 출력합니다. 부분 집합을 출력하는 순서는 출력 예제에서 출력한 순서와 같게 합니다. 단, 공집합은 출력하지 않습니다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F2tlTO%2FbtqE9c1pmH2%2FE8tktgk5BZ3zqgcW5mu4d1%2Fimg.png)

이거는... 진심으로 진짜 아예 감이 잡히지 않는다.
*진심으로* 모르겠다. 그래서 그냥 바로 선생님 강좌를 보았다.

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int n, ch[11];

void DFS(int L){
    int i;
    if(L == n+1){
        for(i =1 ; i<=n; i++){
            if(ch[i] == 1)
                printf("%d ", i);
        }
        puts("");
    }else{
        ch[L] = 1;
        DFS(L+1);
        ch[L] = 0;
        DFS(L+1);
    }
}

int main(){
    scanf("%d", &n);
    DFS(1);
    
    return 0;
}
```

왕신기.. 진짜진짜 신기하게 푸셨다. 

**Key Point**

1. **Ch배열** : 이 배열은 출력 하니 마니를 하고 있다. 만약 왼->왼->왼 의 순서로 방문하고 있으면 ch배열은 [1, 1, 1]이 된다. 그러면 1인 인덱스를 출력하는 것이다. 
2. **Level** : 저기서 L은 레벨을 의미한다. 3이 입력이 되면 레벨은 3이고, 4가 입력이 되면 레벨은 4까지를 둘러(?)본다.

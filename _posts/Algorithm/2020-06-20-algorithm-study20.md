---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 49장 ~ 51장"
date : 2020-06-20 14:00
category : algorithm
---

오늘도~~!!!! Keep Going!
두려워하는 것을 매일 차근차근 한다면 두려움 보다는 설레임이 더 커진다!


## 49장. 블록의 최댓값

현수에게 정면에서 본 단면과 오른쪽 측면에서 본 단면을 주고 최대 블록 개수를 사용하여 정면과 오른쪽 측면에서 본 모습으로 블록을 쌓으라고 했다. 현수가 블록을 쌓는데 사용해야 할 최대 개수를 출력하는 프로그램을 작성하세요.

> 입력

첫 줄에 블록의 크기 N(3<=N<=10)이 주어진다. 블록의 크기는 정사각형 N*N이다.
두 번째 줄에 N개의 정면에서의 높이 정보가 왼쪽 정보부터 주어진다.
세 번째 줄에 N개의 오른쪽 측면 높이 정보가 앞쪽부터 주어진다.
블록의 높이는 10 미만이다.

> 출력

첫 줄에 블록의 최대 개수를 출력한다.


```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int min(int a, int b);

int main(){
    int a[10][10], b[10][10];
    int result[10][10];
    int N, input;
    int cnt=0;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        for(int j=0; j<N; j++){
            a[j][i] = input;
        }
    }
    
    for(int i=0; i<N; i++){
        cin >> input;
        for(int j = N-1; j >= 0; j--){
            b[i][j] = input;
        }
    }
    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            result[i][j] = min(a[i][j], b[i][j]);
            cnt += result[i][j];
        }
    }
    
    cout << cnt << endl;
}

int min(int a, int b){
    if(a >= b){
        return b;
    }else{
        return a;
    }
}
```

이거는 처음에는 당황스럽지만 막상 풀면 그렇게 어렵지 않은 문제!
배열을 두개로 받고, 그 하나하나의 원소 값들 중 최솟값을 선택해서 result 이차원 배열에 넣어주면 되는 문제였다.

---

## 50장. 영지(territory) 선택

세종대왕은 현수에게 현수가 다스릴 수 있는 영지를 하사하기로 했다. 전체 땅은 사각형으로 표시된다. 그 사각형의 땅 중에서 세종대왕이 현수가 다스릴 수 있는 땅의 크기(세로의 길이와 가로의 길이)를 정해주면 전체 땅 중에서 그 크기의 땅의 위치를 현수가 정하면 되는 것이다.

전체 땅은 사각형의 모양의 격자로 되어있으며, 그 사각형 땅 안에는 많은 오렌지 나무가 심겨져 있다. 현수는 오렌지를 무척 좋아하여 오렌지 나무가 가장 많이 포함되는 지역을 선택하고 싶어한다. 현수가 얻을 수 있는 영지의 오렌지 나무 최대 개수를 출력하는 프로그램을 작성하세요.

> 입력 설명

첫 줄에 H(세로길이)와 W(가로 길이)가 입력된다. (5<=H, W<=50) 그 다음 H줄에 걸쳐 각 사각형 지역에 오렌지의 나무 개수 정보가 주어진다.
그 다음 영지의 크기인 세로 길이와 가로 길이가 차례대로 입력된다.

> 출력 설명

첫 줄에 현수가 얻을 수 있는 오렌지 나무의 최대 개수를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 2147000000
#define MIN -2147000000

using namespace std;


int main(){
    int H, W;
    int h, w;
    int max = -2147000000;
    
    cin >> H >> W;
    
    int territory[H][W];
    
    for(int i=0; i < H; i++){
        for(int j=0; j<W; j++){
            cin >> territory[i][j];
        }
    }
    
    cin >> h >> w;
    
    for(int i=0; i < H - h + 1; i++){
        for(int j=0; j<W-w+1; j++){
            int tmp = 0;
            for(int k=0; k<h; k++){
                for(int l=0; l<w; l++){
                    tmp += territory[i+k][j+l];
                }
            }
            if(tmp > max){
                max = tmp;
            }
        }
    }
    
    cout << max << endl;
    
    return 0;
}

/* input
 6 7
 3 5 1 3 1 3 2
 1 2 1 3 1 1 2
 1 3 1 5 1 3 4
 5 1 1 3 1 3 2
 3 1 1 3 1 1 2
 1 3 1 3 1 2 2
 2 3
 */

```

4중 포문을 쓰는게.. 마음에 걸리지만 이렇게 안하고 어떻게 풀 수 있는지는 모르겠기에 그냥 구해보았다.
선생님은 어떻게 푸셨으려나?


### 선생님 코드

여기서는...
**다이나믹 프로그래밍** 을 이용해야 한다!!!!!!!!! 

4중 포문은 작은 배열들에서는 잘 동작하지만, 크기가 커지면 제대로 동작하지 않는다. **dynamic 배열**을 하나 더 만들어서 생각을 해줘야 한다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FtqIv2%2FbtqE0bipmBa%2FyiSNobpTuoOWpi8xbgsD61%2Fimg.png)

이렇게 다이나믹 배열을 또 따로 생각을 해주어야 한다. 필수!!

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int a[701][701], dy[701][701];

int main(){
    freopen("input.txt", "rt", stdin);
    int h, w, n, m, i, j, tmp, max=-2147000000;
    scanf("%d %d", &h, &w);
    for(i=1; i<=h; i++){ //point! 1부터 시작 -> 0에는 자동으로 아무것도 들어가지 않음.
        for(j=1; j<=w; j++){
            scanf("%d", &a[i][j]);
            dy[i][j] = dy[i-1][j] + dy[i][j-1] - dy[i-1][j-1] + a[i][j];
        }
    }

    scanf("%d %d", &n, &m);

    for(i=n; i<=h; i++){  //가장 마지막 인덱스가 중요한 거니까! n, m부터 시작해서 크게 해나감.
        for(j=m; j<=w; j++){
            tmp = dy[i][j] - dy[i-n][j] - dy[i][j-m] + dy[i-n][j-m];
            if(tmp>max) max = tmp;
        }
    }
    
    printf("%d\n", max);

    return 0;
}
```

오늘도 또 하나 배웠다! 다이나믹 프로그래밍!!
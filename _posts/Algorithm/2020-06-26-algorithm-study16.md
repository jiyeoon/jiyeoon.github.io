---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 60장 ~ 61장"
date : 2020-06-26 20:00
category : algorithm
---

## 60장. 합이 같은 부분집합 (DFS : 아마존 인터뷰)

N개의 원소로 구성된 자연수 집합이 주어지면 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES"를 출력하고, 그렇지 않으면 "NO"를 출력하는 프로그램을 작성하세요.

예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10}으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.

> 입력

첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
두 번째 줄에 집합의 원소 N개가 주어진다. 각 우너소는 중복되지 않는다.

> 출력

첫 번째 줄에 "YES" 또는 "NO"를 출력한다.

```c++
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int n, ch[11];
vector<int> input;
vector<int> s;

void DFS(int L){
    int i;
    if(L == n+1){
        int sum = 0;
        for(i =1 ; i<=n; i++){
            if(ch[i] == 1){
                cout << input[i-1] << " ";
                sum += input[i-1];
            }
        }
        cout << endl << "sum : " << sum << endl;
        s.push_back(sum);
    }else{
        ch[L] = 1;
        DFS(L+1);
        ch[L] = 0;
        DFS(L+1);
    }
}

int main(){
    cin >> n;
    
    for(int i=0; i<n; i++){
        int tmp;
        cin >> tmp;
        input.push_back(tmp);
    }
    
    DFS(1);
    
    int t = s.size();
    cout << t << endl;
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()));
    int k = s.size();
    cout << k << endl;
    
    if(t != k){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    
    return 0;
}
```

어찌 저찌 풀었지만...
과연 이게 가장 효율적인 방법인가... 그거에 대한 확신은 없다.. 쩝.. 
선생님 코드를 확인해보아야겠다!

### 선생님 코드

```c++
#include <stdio.h>

int n, a[11], total = 0;
bool flag = false;

void DFS(int L, int sum){
    if(flag == true) return;
    if(L == n+1){
        if(sum == (total-sum)){
            flag = true;
        }
    }else{
        DFS(L+1, sum+a[i]);
        DFS(L+1, sum);
    }
}

int main(){
    int i;
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        scanf("%d", &a[i]);
        total += a[i];
    }
    DFS(1, 0);
    if(flag == true) printf("YES\n");
    else printf("NO\n");

    return 0;
}
```
포인트는 DFS 함수에 level 뿐만 아니라 sum을 같이 넣은 것! 

---

## 61장. 특정 수 만들기 (DFS : MS 인터뷰)

N개의 원소로 구성된 자연수 집합이 주어지면, 집합의 원소와 '+', '-' 연산을 사용하여 특정 수인 M을 만드는 경우가 몇 가지 있는지 출력하는 프로그램을 작성하세요. 각 원소는 연산에 한번만 사용합니다.

예를 들어, {2, 4, 6, 8}이 입력되고 M=12 이면

2 + 4 + 6 = 12
4 + 8 = 12
6 + 8 - 2 = 12
2 - 4 + 6 + 8 = 12

로 총 4가지의 경우가 있다. 만들어지는 경우가 존재하지 않으면 -1를 출력한다.

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[11];

int ch[12];
int polarity[12];

int N, M;

int cnt=0;

vector<int> tmp;

void polarity_DFS(int level);
void ch_DFS(int level);

void ch_DFS(int level){
    if(level == N+1){
        //vector <int> tmp;
        for(int i=1; i<=N; i++){
            if(ch[i] == 1)
                tmp.push_back(arr[i]);
        }
        polarity_DFS(1);
        tmp.clear();
    }else{
        ch[level] = 1;
        ch_DFS(level+1);
        ch[level] = 0;
        ch_DFS(level+1);
    }
}

void polarity_DFS(int level){
    if(level == tmp.size()+1){
        int sum=0;
        cout << "# : ";
        for(int i=1; i<=tmp.size(); i++){
            if(polarity[i] == 1){
                sum += tmp[i-1];
                //cout << " + " << tmp[i-1] << " ";
            }
            else{
                sum -= tmp[i-1];
                //cout << " - " << tmp[i-1] << " ";
            }
        }
        //cout << " = " << sum << endl;
        if(sum == M)
            cnt++;
        
    }else{
        polarity[level] = 1; // +
        polarity_DFS(level+1);
        polarity[level] = 0;
        polarity_DFS(level+1);
        
    }
}

int main(){
    cin >> N >> M;
    
    for(int i=1; i<=N; i++){
        cin >> arr[i];
    }
    
    ch_DFS(1);
    
    if(cnt == 0){
        cout << "-1" << endl;
    }else{
        cout << cnt << endl;
    }
    
}
```

*모르겠다.. 어렵다.. 선생님 강의 도움..을 해야겟다 헉억*


풀었다!! 여기서는 DFS를 두번 사용해서 풀어야했다. 
먼저 ch 배열로 있는지 없는지를 선택한 후 극성을 넣어주어야 했던 문제였다. 그 후에는 극성을 선택해주는 polarity를 선택해주는 경우를 또 DFS를 통해 구해줘야 했다.

근데 이게 맞는 건지는 모르겠다. 선생님 강의를 봐야겠다.
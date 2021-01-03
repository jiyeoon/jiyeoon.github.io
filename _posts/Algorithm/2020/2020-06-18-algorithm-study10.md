---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 46장"
category : algorithm
date : 2020-06-18 20:00
---

다른거 하느라 바쁘더라도 문제 하나라도 풀자!!! (는 진짜 하나 품 ㅋㅋㅋㅋㅋ)

## 46장. 멀티태스킹 (카카오 먹방 문제 변형)

현수의 컴퓨터는 멀티태스킹이 가능하다. 처리해야 할 작업이 N개 들어오면 현수의 컴퓨터는 작업을 1부터 N까지의 번호를 부여하고 처리를 다음과 같이 한다.

1) 컴퓨터는 1번 작업부터 순서대로 1초씩 작업을 한다. 즉, 각 작업을 1초만 작업하고 다음 작업을 하는 식이다.

2) 마지막 번호의 작업을 1초 했으면 다시 1번 작업으로 가서 다시 1초씩 후속 처리를 한다. 

3) 처리가 끝난 작업은 작업 스케줄에서 사라지고 새로운 작업은 들어오지 않는다.

그런데 현수의 컴퓨터가 일을 시작한지 K초 후에 정전이 되어 컴퓨터가 일시적으로 멈추었다. 전기가 들어오고 나서 현수의 컴퓨터가 몇 번 작업부터 다시 시작해야 하는지 알아내는 프로그램을 작성하세요.

> 입력 설명

첫 번째 줄에 작업의 개수 N(1<= N <= 2,000)이 주어지고 그 다음 N 줄에 걸쳐 각 작업을 처리하는데 걸리는 시간이 초단위로 주어진다. 한 작업을 처리하는 데 필요한 시간은 1000를 넘지 않는다.

마지막 줄에 정전이 발생한 시간 K(1<=K<=2,000,0000)가 주어진다.

> 출력 설명

첫 번째 줄에 몇 번 작업부터 다시 시작해야 하는지 작업 번호를 출력한다.

만약 더이상 처리할 작업이 없다면 -1를 출력한다.


```c++
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef struct job{
    int index;
    int remain;
}job;

int main(){
    int numOfTask;
    int blackout;
    int input;
    
    vector<job> job_scheduler;
    
    cin >> numOfTask;
    
    for(int i=0; i<numOfTask; i++){
        cin >> input;
        job j;
        j.index = input; j.remain = input;
        job_scheduler.push_back(j);
    }
    
    cin >> blackout;
    
    int i = 0;
    while(1){
        int tmp = i;
        if(tmp > job_scheduler.size()){
            tmp = tmp - (int)job_scheduler.size();
        }
        
        if(i==blackout-1){
            if(job_scheduler.size() == 0){
                cout << -1 << endl;
            }else{
                cout << job_scheduler[tmp].index << endl;
            }
            break;
        }
        
        job_scheduler[tmp].remain--;
                
        if(job_scheduler[tmp].remain == 0){
            job_scheduler.erase(job_scheduler.begin() + tmp);
        }else{
            i++;
        }
        /*
        cout << "[ ";
        for(int j=0; j<job_scheduler.size(); j++){
            cout << "index : " <<  job_scheduler[j].index << ", remain :  " << job_scheduler[j].remain << " ";
        }
        cout << " ]" << endl;
        */
    }
    
    return 0;
}
```

풀긴 했는데 아마 이게 답은 아닐거다.
선생님 코드를 보자!!

### 선생님 코드

```c++
#include <stdio.h>
using namespace std;

int a[2001];

int main(){
    int n, k, i, p=0, cnt=0, tot=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++){
        scanf("%d", &a[i]);
        tot += a[i];
    }
    scanf("%d", &k);
    if(k>=tot){
        printf("-1\n");
        return 0;
    }

    while(1){
        p++;
        if(p>n) p=1;
        if(a[p] == 0) continue;
        a[p]--;
        cnt++;
        if(cnt==k) break;
    }

    while(1){
        p++;
        if(p>n) p=1;
        if(a[p]!= 0) break;
    }

    printf("%d\n", a[p]);

    return 0;
}
```

오케이 오케이 갓잇~!!!! 어떤 맥락인지 이해했다. 

선생님 코드에서 특징점은

1. 배열을 전역변수로 선언
2. `int pos;`라고 position 변수를 둠. 간단하게 `if(pos>n) p=1`로 생각함.
3. 나는 배열의 remain이 끝나면 erase하는 것을 생각했는데, 여기서는 0이면 그냥 continue하는 것으로 생각함. 


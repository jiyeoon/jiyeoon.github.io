---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 21장 ~ 25장"
date : 2020-06-12 20:00
category : algorithm
---

오늘도 꾸준하게 하는 알고리즘~! 
아직까지는 문제 구현력? 해결력 키우기 단계이다. 이번주는 문제 해결력 키우고 다음주부터는 알고리즘 들어가기!!

## 21. 카드게임

0부터 9까지의 숫자가 표시된 카드를 가지고 두 사람 A와 B가 게임을 한다. A와 B에게는 각각 0에서 9까지의 숫자가 하나씩 표시된 10장의 카드 뭉치가 주어진다. 두 사람은 카드를 임의의 순서로 섞은 후 숫자가 보이지 않게 일렬로 늘어놓고 게임을 시작한다. 단, 게임 도중 카드의 순서를 바꿀 수는 없다.

A와 B 각각이 늘어놓은 카드를 뒤집어서 표시된 숫자를 확인하는 것을 한 라운드라고 한다. 게임은 첫 번째 놓인 카드부터 시작하여 순서대로 10번의 라운드로 진행된다. 각 라운드에서는 공개된 숫자가 더 큰 사람이 승자가 된다. 승자에게는 승점 3점이 주어지고 패자에게는 승점이 주어지지 않는다. 만약 공개된 두 숫자가 같아서 비기게 되면, A, B 모두에게 승점 1점이 주어진다.

10번의 라운드가 모두 진행된 후 총 승점이 큰 사람이 게임의 승자가 된다. 

> 입력

첫 번째 줄에는 A가 늘어놓은 카드의 숫자들이 빈칸을 사이에 두고 순서대로 주어진다. 두번째 줄에는 B가 늘어놓은 카드의 숫자들이 빈칸을 사이에 두고 순서대로 주어진다.

> 출력

첫 번째 줄에는 게임이 끝난 후, A와 B가 받은 총 승점을 순서대로 빈칸을 사이에 두고 출력한다. 두번째 줄에는 이긴 사람을 출력한다. 비겼을 경우에는 D를 출력한다.

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int input;
    int score_a = 0, score_b = 0;
    
    vector <int> a;
    vector <int> b;
    
    for(int i=0; i<10; i++){
        cin >> input;
        a.push_back(input);
    }
    
    for(int i=0; i<10; i++){
        cin >> input;
        b.push_back(input);
    }
    
    for(int i=0; i<10; i++){
        if(a[i] == b[i]){
            score_a++;
            score_b++;
        }else if(a[i] > b[i])
            score_a += 3;
        else
            score_b += 3;
    }
    
    cout << score_a << " " << score_b << endl;
    
    cout << (score_a > score_b ? "A" : "B");
    
    return 0;
}
```


## 22. 온도의 최대값

매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠동안의 온도 합이 가장 큰 값을 알아보고자 한다.
예를들어, 다음과 같이 10일간의 온도가 주어졌을 때, 3, -2, -4, -9, 0, 3, 7, 13, 8, -3 모든 이틀간의 온도 합은 아래와 같다.

(사진 생략..)

매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도 합이 가장 큰 값을 계산하는 프로그램을 작성하세요

> 입력
첫번째 줄에는 두개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다.
첫 번째 정수 N은 온도를 측정한 전체 날짜의 수다. K는 합을 구하기 위한 연속적인 날짜의 수다.

둘째줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int N, K, input, sum;
    vector <int> arr;
    
    int max = -2147000000;
    
    cin >> N >> K;
    
    for(int i=0; i<N; i++){
        cin >> input;
        arr.push_back(input);
    }
    
    for(int i=0; i < N - K + 1; i++){
        sum = 0;
        for(int j=0; j < K; j++){
            sum += arr[i+j];
        }
        //cout << sum << " / ";
        if(max < sum)
            max = sum;
    }
    
    cout << max << endl;
    
    return 0;
}
```


## 23. 연속 부분 증가 수열

N개의 숫자가 나열된 수열이 주어진다. 이 수열 중 연속적으로 증가하는 부분 수열을 최대 길이를 구하여 출력하는 프로그램을 작성하세요
만약 N=9이고  57 3 3 12 12 13 10 11 이면 "3 3 12 12 13" 부분이 최대 길이 증가 수열이므로 그 길이인 5를 출력한다. 값이 같을 때는 증가하는 걸로 생각한다.

> 입력
첫 줄에 자연수의 개수 N이 주어진다.
두 번째 줄에 N개의 숫자열이 주어진다. 각 숫자는 100,000 이하의 자연수다

> 출력
최대 부분 증가 수열의 길이를 출력하세요


```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int N, input;
    int count=0, max = -2147000000;
    
    vector<int> arr;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        arr.push_back(input);
    }
    
    int flag = 0;
    for(int i=1; i<arr.size();i++){
        if(arr[i] >= arr[i-1]){
            if(flag == 1){
                count++;
            }else{
                flag = 1;
                count++;
            }
        }else{
            flag = 0;
            count = 0;
        }
        
        if(max < count)
            max = count;
    }
    
    if(max != 0)
        max++;
    cout << max << endl;
}
```



## 24. Jolly Jumpers

N개의 정수로 이루어진 수열에 대해 서로 인접해있는 두 수의 차가 1에서 N-1까지의 값을 모두 가지면 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다. 예를들어 1 4 2 3 앞 뒤에 있는 숫자 차의 절대 값이 각각 3, 2, 1 이므로 이 수열은 유쾌한 점퍼가 된다.

> 입력
첫 번째 줄에 자연수 N이 주어진다
그 다음 줄에 N개의 정수가 주어진다. 

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int N, input, num;
    vector <int> arr, diff;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        arr.push_back(input);
        diff.push_back(0);
    }
    
    for(int i=1; i<N; i++){
        num = arr[i] - arr[i-1];
        if(num<0) num = -num;
        diff[num]++;
    }
    
    for(int i=1; i<N-1; i++){
        if(diff[i] == 0){
            cout << "NO" << endl;
            exit(0);
        }
    }
    cout << "YES" << endl;
    return 0;
}
```

## 25. 석차 구하기

N명의 학생의 수학점수가 입력되면 각 학생의 석차를 입력된 순서대로 출력하는 프로그램을 작성하세요.

> 입력
첫 줄에 N이 입력되고 두번째 줄에 수학점수를 의미하는 N개의 정수가 입력됨. 같은 점수가 입력될 경우 높은 석차로 동일 처리.

> 출력
첫 줄에 입력된 순서대로 석차 출력

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef struct st {
    int score;
    int rank;
    int index;
}st;

bool cmp_score(const st& x, const st& y){
    return x.score > y.score;
}

bool cmp_index(const st& x, const st& y){
    return x.index < y.index;
}

int main(){
    vector<st> student;
    st st_input;
    int N, input;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> input;
        st_input.index = i;
        st_input.score = input;
        st_input.rank = 0;
        student.push_back(st_input);
    }
    
    sort(student.begin(), student.end(), cmp_score);
    
    for(int i=0; i<student.size(); i++){
        if(i==0){
            student[i].rank = 1;
            continue;
        }
        if(student[i].score >= student[i-1].score){
            student[i].rank = student[i-1].rank;
        }else{
            student[i].rank = i+1;
        }
    }
    
    sort(student.begin(), student.end(), cmp_index);
    
    for(int i=0; i<student.size(); i++){
        cout << student[i].rank << " ";
    }
    
    return 0;
}

```

눈누.. 여기서 키포인트!

## sort(v.begin(), v.end(), cmp)

`#include <vector>` 헤더가 필요한 sort 함수.
여기서 원하는대로 정렬을 하고싶으면 cmp라는 bool 함수를 정의해주어야 한다.
bool 함수는 그냥 심플하게..~

예시
```c++
bool cmp(const s& x, const s& y){
    return x.dd < y.dd;
}
```

그래서 나는 cmp 함수를 두개 작성해주었다. index별로 정렬할거랑 score대로 정렬할 것!!
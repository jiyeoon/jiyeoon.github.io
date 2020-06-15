---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 31장 ~ 35장"
category : algorithm
date : 2020-06-15 20:00
---

오늘도 따라하며 배우는 인프런강좌!!! 존버는 승리한다~~ 엽져니는 승리한다~!!!

오늘 과제는 약간 이런 느낌 ㅋㅋㅋ
![img1](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99619C485A7DB9D810)




## 31장. 탄화수소 질량

탄소(C)와 수소(H)로만 이루어진 화합물을 탄화수소라고 한다.
탄소 한개의 질량은 12g, 수소 하나의 질량은 1g이다. 탄화수소식이 주어지면 해당 화합물의 질량을 구하는 프로그램을 작성하시오. 

> 입력

첫 줄에 탄화수소식이 주어진다. 식이 형태는 CaHb의 형태이며 (1 <= a, b <= 100)이다.
단, a나 b가 1이면 숫자가 식에 입력되지 않는다.

> 출력

첫 줄에 탄화수소의 질량을 출력한다.


```c++
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    string input;
    int numOfC=0, numOfH=0;
    //두글자가 나올 수도 있는거니까..
    string num = "";
    
    cin >> input;
    
    int i = 1;
    
    if(input[i] == 'H'){
        numOfC = 1;
        
        if(input[i+1] == '\0'){
            numOfH = 1;
        }else{
            num = "";
            for(int j=i+1; input[j] != '\0'; j++){
                num += input[j];
            }
            numOfH = stoi(num);
        }
        
    }else{
        int j = i;
        num = "";
        for(j = i; input[j] != 'H'; j++){
            num += input[j];
        }
        numOfC = stoi(num);
        
        i = j;
        
        //cout << input[j] << endl;
        
        if(input[i+1] == '\0'){
            numOfH = 1;
        }else{
            num = "";
            for(int k = i+1; input[k] != '\0'; k++){
                num += input[k];
            }
            numOfH = stoi(num);
        }
        
    }
    
    cout << 12 * numOfC + numOfH << endl;
    
    return 0;
}

```

ㅋㅋㅋㅋㅋㅋㅋㅋ
개떡같이 짜긴 했지만 답은 잘 나옴.. ㅎ


### 선생님 코드

선생님도 뭐.. 로직은 나랑 비슷하신 것 같다.
근데 야금야금 푼게 조금씩 다른 듯?


```c++
#include <stdio.h>
int main(){
    freopen("input.txt", "rt", stdin);
    char a[10];
    int c = 0, h = 0, i, pos; //pos : H의 인덱스

    scanf("%s", &a);

    if(a[1] == 'H'){ //c의 개수가 1
        c = 1;
        pos = 1;
    }else{ //c의 개수가 1이 아님
        for(i = 1; a[i] != 'H'; i++){
            c = c * 10 + (a[i] - '0');
        }
        pos = i;
    }

    if(a[pos+1] == '\0'){ //h의 개수가 1
        h = 1;
    }else{
        for(i = pos+1; a[i] != '\0'; i++){
            h = h * 10 + (a[i] - '0');
        }
    }

    printf("%d\n", c*12 + h);

    return 0;
}
```


---

## 32장. 선택정렬

사실.. 여기서부터는 할게 없다. 선택정렬, 삽입정렬, 버블정렬이 뭔지 모르기 때문.. 


### 선택정렬이란?

![img2](https://lh3.googleusercontent.com/proxy/TWn7LApX_uNwIWNlOi4FgqfZCzAZVoWJKvLVgRHOTcJXSeaD-mjFoy4EmjcVIELwuBibaRcapsZRMnv6aTRgFxK1YKTLQTB8bBbnfXOVy3FIvEiIt9hcvzXwi4OP8dAG_s5dkaBLGZx9L1gE8vpb1VMfq7moXighFTJag7-NlS9rthMLg7WMeM9V0ZXf83mTuqfbGIYf5tMN0AsDIZ6fB5l3XiKaWmbPm1NFjdqnKXxcM0RbT7waxuklT4u08MJCcweg8mlZm6Rp6whcJj4bKmapoSh811xydWx8xMXXR_vS8NgEWhgs)

이게 선택정렬이다. 앞에서부터 한칸한칸씩 하면서 제일 작은 값과 swap 하는거.. 
인덱스 i 뒷편부터.. 슝.. 


### 선생님 코드

```c++
for(int i=0; i < n-1; i++){
    idx = i;
    for(int j = i+1; j < n; j++){
        if(a[j] < a [idx]) //여기가 포인트..
            idx = j;
    }
    //아래는 swap 부분
    tmp = a[i];
    a[i] = a[idx];
    a[idx] = tmp;
}
```


---

## 33장. 3등의 성적은?

주어진 점수들이 있을 때 3등인 사람의 점수는?

아!! 여기서 중복을 제거해주어야한다!! `unique(arr.begin(), arr.end())` 해주어야 한다!!

> 입력

첫 줄에 사람수
둘째 줄에 그 사람들의 점수

> 출력

3등의 점수 출력

(얘도 그냥 sort 함수 써버리고 끝내기..)

```c++
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, input;
    vector <int> arr;

    cin >> N;

    for(int i=0; i<N; i++){
        cin >> input;
        arr.push_back(input);
    }

    sort(arr.begin(), arr.end());
    unique(arr. begin(), arr.end());

    cout << arr[3] << endl; 

    return 0;
}

```

중복 제거 해주는걸 깜빡했다..!! 중복도 제거해주어야 함.

선생님은 이거를 그.. 위에 있는 선택 정렬을 사용해서 푸셨다.

```c++
for(int i=0; i < n-1; i++){
    idx = i;
    for(int j = i + 1; j < n; j++){
        if(a[j] > a[idx]) idx = j;
    }
    tmp = a[i];
    a[i] = a[idx];
    a[idx] = tmp;
}
int cnt = 0;
for(int i = 1; i < n; i++){
    if(a[i-1] != a[i]) cnt++; //중복이면 카운트하지 않겠다는 의미!!
    if(cnt==2){
        cout << a[i] << endl;
        break;
    }
}

```


---

## 34장. 버블 정렬

버블정렬이 뭔지 몰라여~

### 버블 정렬이란?

![img3](https://lh3.googleusercontent.com/proxy/QMwZx2b-VnqNwhkIFUrIGLAELO0_q4CHvPiVwICMgg0h_PPEYgARYzxaQQlpj8Yw0_0OkBX7uYfYtd_hqDIECiDhjJHcJRDl_Vid-xROUUjf9F_5D_jJlMb1CrqzHx5a3oF-_VyDmnA0hou3MQ01yz6uiIC4IoIN_SlXQv92Wd23EhqO)

인접한 두 수끼리 계속 정렬하는 것을 말한다.
시간복잡도가 제일 좋지 않음. 

### 선생님 코드

```c++
for(i = 0; i < n-1; i++){
    for(j = 0; j < n-i-1; j++){
        if(a[j] > a[j+1]){
            tmp = a[j];
            a[j] = a[j+1];
            a[j+1] = tmp;
        }
    }
}
```
뭔가 간단..한데..
굳이 이 버블 정렬로 풀어야하는.. 그런 마음.. 

---

## 35장. Special Sort (구글 인터뷰)

N개의 정수가 입력되면 당신은 입력된 값을 정렬해야 한다.
음의 정수는 앞쪽에 양의 정수는 뒷쪽에 있어야 한다. 또한 양의 정수와 음의 정수 순서에는 변함이 없어야 한다.

> 입력

첫 번째 줄에는 N이 주어지고, 그 다음줄 부터 음수를 포함한 정수가 주어진다. 숫자 0은 입력되지 않는다.

> 출력

정렬된 결과를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, input;
    vector<int> pos;
    vector<int> neg;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> input;
        if(input > 0)
            pos.push_back(input);
        else if(input < 0)
            neg.push_back(input);
        else
            continue;
    }
    //아 머야 훨씬 간단하잖아
    
    for(int i = 0; i < neg.size(); i++){
        cout << neg[i] << " ";
    }
    for(int i = 0; i < pos.size(); i++){
        cout << pos[i] << " ";
    }
    
    return 0;
}
```

음의 정수 배열 양의 정수 배열 2개를 쓰면 되는 간단한 문제!


### 선생님 코드

이거는 버블소트가 가장 적절한 문제임! 버블 소팅하는 것이 중요하다.
이웃한 두 수 끼리는 바꾸지 않는다. 근데 앞에가 양수고 뒤에가 음수일때만 바꿈!

```c++
for(int i=0; i<n-1; i++){
    for(int j=0; j < n - i - 1; j++){
        if(a[j] > 0 && a[j+1] < 0){
            tmp = a[j];
            a[j] = a[j+1];
            a[j+1] = tmp;
        }
    }
}
```
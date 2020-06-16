---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 36장 ~ 40장"
date : 2020-06-16 19:30
category : algorithm
---


오늘도 나는 알고리즘 공부를 한다네~ 할 수 있다 이지연!!
센스는 갈고 닦는 것, 재능은 꽃 피우는 것!

## 36장. 삽입 정렬

삽입 정렬이 뭔지 몰라 까먹음 ㅠㅠ 

뭔가.. 약간 pos라는 개념을 쓴게 삽입정렬같다.  

```c++
for(i = 1; i < n; i++){
    tmp = a[i];
    for(j = i-1; j >= 0; j--){
        if(a[j] > tmp)
            a[j+1] = a[j];
        else
            break;
    }
    a[j+1] = tmp;
}
```


## 37장. Least Recently Used (카카오 캐시 문제 변형)

캐시메모리 사용 규칙이 LRU 알고리즘을 따른다. LRU알고리즘은 Least Recently Used 의 약자로 직역하자면 가장 최근에 사용되지 않은 것 정도의 의미다. 캐시에서 작업을 제거할 때 가장 오랫동안 사용되지 않은 것을 제거하겠다는 의미다. 

만약 캐시의 사이즈가 5이고 작업이 2 3 1 6 7 순서로 저장되어 있다면 

1) Cache Miss : 해야할 작업이 캐시에 없는 상태로 위 상태에서 만약 새로운 작업인 5번 작업을 CPU가 사용한다면 Cache miss가 되고 모든 작업이 뒤로 밀리고 5번 작업은 캐시의 맨 앞에 위치한다. 5 2 3 1 6

2) Cache Hit : 해야할 작업이 캐시에 있는 상태로 위 상태에서 만약 3번 작업을 CPU가 사용한다면 Cache Hit가 되고, 3번이 맨 앞으로 그리고 나머지는 한칸씩 뒤로 밀리게 된다.

캐시의 크기가 주어지고 캐시가 비어있는 상태에서 N개의 작업을 CPU가 차례로 처리한다면 N개의 작업을 처리한 후 캐시 메모리의 상태를 가장 최근 사용된 작업부터 차례대로 출력하는 프로그램을 작성하시오.

> 입력

첫 번째 줄에 캐시의 크기 S(3 <= S <= 10)와 작업의 개수 N(5<= N <= 1000)이 입력된다.
두 번째 줄에 N개의 작업번호가 처리순으로 주어진다. 작업번호는 1~100이다.

> 출력

마자막 작업 후 캐시 메모리의 상태를 가장 최근 사용된 작업부터 차례로 출력한다.

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cache_hit(vector<int> cache, int x);

int main(){
    int size, N;
    int input, pos;
    
    cin >> size >> N;
    
    vector<int> cache(size, 0);
    
    for(int i=0; i<N; i++){
        cin >> input;
        if(cache_hit(cache, input)){ //cache hit
            for(pos = 0; pos < cache.size(); pos++){
                if(cache[pos] == input)
                    break;
            }
            cache.erase(cache.begin()+pos);
            cache.insert(cache.begin(), input);
        }else{ // cache miss
            cache.insert(cache.begin(), input);
            if(cache.size() >= size)
                cache.pop_back();
        }
    }

    for(int i=0; i<cache.size(); i++){
        cout << cache[i] << " ";
    }
    cout << endl;
    
    return 0;
}


bool cache_hit(vector<int> cache, int x){
    for(int i=0; i<cache.size(); i++){
        if(cache[i] == x){
            return true;
        }
    }
    return false;
}
```

깔끔베리.. 답은 매우 잘 나온다. 
문제는 엄청 길고 어려운 것 같은데 막상 풀면 크게 어렵지는 않은 문제다.
근데 벡터의 함수에 의존을 많이 함. 훔,, 

### 선생님 코드

여기서 캐시 미스.. 히트 하는 pos = -1로 초기화 해서.. 좋았다..



---

## 38장. Inversion Sequence

1부터 n까지의 수를 한번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞에 놓여있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 inversion sequence라고 한다. 
따라서 4 8 6 2 5 1 3 7 의 inversion sequence는 5 3 4 0 2 1 1 0 이 된다.
n과 1부터 n까지의 수를 사용하여 이루어진 수열의 inversion sequence가 주어졌을 때, 원래의 수열을 출력하는 프로그램을 작성하시오. 

> 입력

첫 번째 줄에 자연수 N이 주어지고, 두 번째 줄에는 inversion sequence가 숫자 사이에 한 칸의 공백을 두고 주어진다.

> 출력

오름차순으로 정렬된 수열을 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    int N;
    int input;
    vector<int> inversion_seq;
    vector<int> result;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> input;
        inversion_seq.push_back(input);
    }
    
    for(int i = N-1; i >= 0; i--){ 
        result.insert(result.begin() + inversion_seq[i], i+1);
    }
    
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    
    return 0;
}
```

얘도 마찬가지로 원리를 알면 정말 금방 풀 수 있는 문제였다.



## 39장. 두 배열 합치기

오름차순으로 정렬된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

> 입력 설명

첫 번째 줄에 첫 번째 배열의 크기 N이 주어짐
두 번째 줄에 N개의 배열 원소가 오름차순으로 주어짐
세 번째 줄에 두 번째 배열의 크기 M이 주어짐
네 번째 줄에 M개의 배열 원소가 오름차순으로 주어진다.

> 출력

오름차순으로 정렬된 배열을 출력한다.



이거는.. sort 함수를 쓰면 한컷에 끝내버릴 수 있다.. 쩝..

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    int N, M;
    int input;
    vector<int> arr1;
    vector<int> arr2;
    
    vector<int> result;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        arr1.push_back(input);
    }
    
    cin >> M;
    
    for(int i=0; i<M; i++){
        cin >> input;
        arr2.push_back(input);
    }
    
    int i=0, j=0;
    
    while(1){
        if(i==N){
            while(j != M){
                result.push_back(arr2[j]);
                j++;
            }
            break;
        }
        if(j == M){
            while(i != N){
                result.push_back(arr1[i]);
                i++;
            }
            break;
        }
        
        if(arr1[i] < arr2[j]){
            result.push_back(arr1[i]);
            i++;
        }else if (arr1[i] == arr2[j]){
            result.push_back(arr1[i]);
            result.push_back(arr1[i]);
            i++; j++;
        }else{
            result.push_back(arr2[j]);
            j++;
        }

    }
    
    for(int i=0; i<result.size(); i++){
        cout << result[i] << " ";
    }
    
    return 0;
}
```

굳이 조금 다르게 풀어봄.. ㅎ


---

## 40장. 교집합 (투포인트 알고리즘)

두 집합 A, B가 주어지면 두 집합의 교집합을 출력하는 프로그램을 작성하시오.

> 입력

첫 번째 줄에 집합 A의 크기 N이 주어진다.
두 번째 줄에 N개의 원소가 주어진다. 원소가 중복되어 주어지지 않는다.
세 번째 줄에 집합 B의 크기 M이 주어진다.
네 번째 줄에 M개의 원소가 주어진다. 원소가 중복되어 주어지지 않는다.

> 출력

두 집합의 교집합을 오름차순 정렬하여 출력한다.

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M;
    int input;
    
    vector<int> arr1, arr2;
    vector<int> result;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        arr1.push_back(input);
    }
    
    cin >> M;
    
    for(int i=0; i<M; i++){
        cin >> input;
        arr2.push_back(input);
    }
    
    for(int i=0; i < arr1.size(); i++){
        for(int j=0; j<arr2.size(); j++){
            if(arr1[i] == arr2[j]){
                result.push_back(arr1[i]);
                break;
            }
        }
    }
    
    sort(result.begin(), result.end());
    
    for(int i=0; i<result.size(); i++){
        cout << result[i] << " ";
    }
    
    return 0;
}
```

잘 된다. 이게 가장 좋은 방법인지 아닌지는 모르겠지만 말이다..


알고리즘은 다 좋은데 공부하면 너무 단게 먹고싶다. ㅋㅋㅋㅋㅋㅋ 머리를 많이 써서 그런가보다

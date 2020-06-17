---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 41장 ~ 45장"
category : algorithm
date : 2020-06-17 16:00
---

오늘도~ 나는~ 존버를 한다네~~

## 41장. 연속된 자연수의 합

입력으로 양의 정수 N이 입력되면 2개 이상의 연속된 자연수의 합으로 정수 N을 표현하는 방법의 가짓수를 출력하는 프로그램을 작성하세요.

만약 N=15이면
7+8 = 15
4 + 5 + 6 = 15
1 + 2 + 3 + 4 + 5 = 15
와 같이 총 3가지의 경우가 존재한다.

> 입력

첫 번째 줄에 양의 정수 N(7<=N < 1000)이 주어진다.

> 출력

첫 줄부터 각각의 경우의 수를 출력한다.
맨 마지막 줄에 총 개수를 출력한다.

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int getSum(int x, int n);

int main() {
  int N;
  int sum;
  int count = 0;
  cin >> N;

  for(int i=2; i<N; i++){
    sum = 0;
    for(int j=1; j <= N; j++){
      sum = getSum(j, i);
      if(sum == N){
        cout << "";//얼마나.. 더한건지를.. 알려줘..
        for(int l=0; l < i; l++){
          cout << j + l << " + ";
        }
        cout <<  "= " << N << endl;
        count++;
        break;
      }
    }
  }

  cout << count << endl;
}

int getSum(int x, int n){ //x가 시작. n은 몇번 하는지.
  int result = 0;
  for(int i = 0; i < n; i++){
    result += x + i;
  }
  return result;
}
```

나... 삼중포문 씀... (ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ)
이래도 되는건가....



---

## 42장. 이분 검색

아나 이래서.. 클라우드를 쓰나보다 코드 작성한거 없어짐~~ 이런~

임의의 N개의 숫자가 입력으로 주어진다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하시오.

> 입력

첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어진다.
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어진다.

> 출력

첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.


```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, M;
    vector<int> arr;
    
    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    
    int mid;
    int left = 0, right = N;
    
    sort(arr.begin(), arr.end());
    
    while(1){
        mid = (left + right) / 2;
        if(arr[mid] == M){
            cout << mid + 1 << endl;
            break;
        }else if (arr[mid] < M){
            left = mid+1;
        }else{
            right = mid-1;
        }
    }
    
    return 0;
}
```

이거는 기억이 남!! 정렬하는 것이 포인트~



---

## 43. 뮤직비디오(이분검색 응용)

DVD의 크기를 최소로 하게 만드는 방법은?

> 입력

첫째 줄에 자연수 N, M이 주어진다. 다음 줄에는 부른 순서대로 부른 곡의 길이가 분 단위로 주어진다. 부른 곡의 길이는 10000분을 넘지 않는다.

> 출력

첫 번째 줄부터 DVD의 최소 용량 크기를 출력하시오.


```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getSize(vector<int> arr, int index1, int index2);

int main(){
    int N, M;
    vector<int> arr;
    
    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    
    int index[M+1];
    
    for(int i=0; i< M; i++){
        index[i] = (N/M) * i;
        cout << index[i] << " ";
    }
    index[M] = N-1;
    cout << index[M] << endl;
    
    //오케이!! 초기값 설정 끝!!!
    
    int flag[M]; //반복이면 ~ 반복 아니면 1
    
    
    int prev[M+1];
    
    for(int i=0; index[i] != '\0'; i++){
        prev[i] = index[i];
    }
    
    while(1){
        for(int i=0; i<M; i++){
            if(getSize(arr, index[i], index[i+1]) > getSize(arr, index[i+1], index[i+2])){ //앞에가 더 크면
                if(flag[i] == 0){ //처음이다!!
                    flag[i] = 1;
                }else{ //연속해서 그러고 있는거면
                    continue;
                }
            }else if(getSize(arr, index[i], index[i+1]) == getSize(arr, index[i+1], index[i+2])){
                
            }else{
                
            }
        }
        
        
        
    }
    
    return 0;
}

int getSize(vector<int> arr, int index1, int index2){
    if(index2 == 0 || index2 > arr.size() || index1 < 0)
        return 0;
    
    int result = 0;
    for(int i = index1; i < index2; i++){
        result += arr[i];
    }
    
    return result;
}
```

모르겠숨.. 먼가 이분검색을 대충 이렇게 이용하면 되겠다~ 싶은건 있는데 그걸 코드로 구현을 못하겠네.

### 선생님 코드

```c++
#include <stdio.h>
#include <algorithm>

using namespace std;

int a[1001], n;

int Count(int s);

int main(){
    int m, i, lt=1, rt=0, mid, res;
    
    scanf("%d %d", &n, &m);
    
    for(i=1; i<=n; i++){
        scanf("%d", &a[i]);
        rt = rt + a[i];
    }
    
    while(lt <= rt){
        mid = (lt+rt)/2;
        if(Count(mid) <= m){
            res = mid;
            rt = mid - 1;
        }
        else{
            lt = mid + 1;
        }
    }
    printf("%d\n", res);
}

int Count(int s){
    int i, cnt=1, sum=0;
    for(int i=0; i<=n; i++){
        if(sum + a[i] > s){
            cnt++;
            sum = a[i];
        }
        else{
            sum += a[i];
        }
    }
    return cnt;
}
```

훨씬 가시적이고 쉽게 쓰셨다!!

키 포인트를 적자면

1. 전역변수 - 배열과 갯수를 전역변수로 선언함. 그래서 함수 쓸 때도 따로 받을 필요 없게끔 함.
2. `while(lt <= rt)` 이거를 해주면 따로 break를 쓸 필요가 없다.
3. 생각의 전환 - 입력받은 배열에서 값을 찾으려고 했었는데, 그게 아니라 입력받은 값들의 합에서 중간값을 찾아 나가면 되는 거였다.

---

## 44장. 마구간 정하기 (이분검색 응용)

N개의 마구간이 1차원 수직선상에 있다. 각 마구간은 x1, x2, x3, ...., xN의 좌표를 가지며 마구간간에 좌표가 중복되는 일은 없다.

현수는 C마리의 말을 가지고 있는데 이 말들은 서로 가까이 있는 것을 좋아하지 않는다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶다. C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

> 입력

첫 줄에 자연수 N(3 <= N <= 200,000)과 C(2 <= C<= N)이 공백을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0 <= xi <= 1,000,000,000)가 한 줄에 하나씩 주어진다.

> 출력 

첫 줄에 가장 가까운 두 말의 최대 거리를 출력하시오


## 45. 공주 구하기



```c++
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

void print_arr(vector<int> arr);

int main(){
    int N, M;
    vector<int> arr;
    
    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        arr.push_back(i+1);
    }
    
    while(arr.size() != 0){
        if(M > arr.size()){
            int tmp = M;
            while(1){
                tmp = tmp - arr.size();
                if(tmp < arr.size())
                    break;
            }
            cout << arr[tmp-1] << endl;
            arr.erase(arr.begin() + tmp - 1);
            
            vector<int> new_arr(arr.size(), 0);
            //todo : arr update
            for(int i=0; i<arr.size(); i++){
                if(tmp + i > arr.size()){
                    new_arr[i] = arr[tmp -1 + i - arr.size()];
                }else{
                    new_arr[i] = arr[tmp -1 + i];
                }
            }
            arr = new_arr;
            //print_arr(arr);
            
        }else{
            int tmp = M;
            
            cout << arr[tmp-1] << endl;
            arr.erase(arr.begin() + M - 1);
            
            vector<int> new_arr(arr.size(), 0);
            //todo : arr update
            for(int i=0; i<arr.size(); i++){
                if(tmp + i > arr.size()){
                    new_arr[i] = arr[tmp -1 + i - arr.size()];
                }else{
                    new_arr[i] = arr[tmp-1 + i];
                }
            }
            arr = new_arr;
            //print_arr(arr);

        }
    }
    
    cout << endl <<  arr[0] << endl;
    
    return 0;
}

void print_arr(vector<int> arr){
    for(int i=0; i<arr.size(); i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}
```

껌이군~ 하고 풀었다가 꽤 오래걸렸다 캬캬... 선생님 강의 들어야겠다.
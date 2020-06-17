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

나... 삼중포문 씀...
이래도 되는건가....



---

## 42장. 이분검색

임의의 N개의 숫자가 입력으로 주어진다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.

> 입력

첫 줄에 한 줄에 자연수 N(3 <= N <= 1,000,000)과 M이 주어진다.
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어진다.

> 출력

첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int N, M, input;
  int mid;

  vector<int> arr;

  cin >> N >> M;

  for(int i = 0; i < N; i++){
    cin >> input;
    arr.push_back(input);
  }

  int left = 0, right = N-1;

  sort(arr.begin(), arr.end());

  while(1){
    mid = (left + right)/2;
    if(arr[mid] == M){
      cout << mid +1 << endl;
      break;
    }else if(arr[mid] < M){
      left = mid+1;
    }else{
      right = mid-1;
    }
  }

  return 0;
}
```

binary search 자연스럽게 습-득..
후후..


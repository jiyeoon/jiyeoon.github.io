---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 26장 ~ 30장"
date : 2020-06-13 17:00
category : algorithm
---

## 26. 마라톤

장거리 달리기 대회가 진행되어 모든 선수가 반환점을 넘었다. 각 선수의 입장에서 자기보다 앞에 달리고 있는 선수들 중 평소 실력이 자기보다 좋은 선수를 남은 거리동안 앞지르는 것은 불가능하다. 평소 실력이 자기보다 좋지 않은 선수가 앞에 달리고 있으면 남은 거리동안 앞지르는 것이 가능하다. 이러한 가정 하에서 각 선수는 자신이 앞으로 얻을 수 있는 최선의 등수를 알 수 있다.

> 입력

첫째 줄에는 선수의 수를 의미하는 정수 n이 주어진다. n은 3 이상 10000이하이다. 다음 줄에는 n개의 정수가 주어진다. 이 수는 선수들의 평소 실력이다. 실력이 같다면 앞에 달리는 선수를 앞지를 수 없다.

> 출력

각 선수들의 최선의 숫자를 입력하라.

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  vector <int> player, rank;
  int N, input;
  int i, j;
  
  cin >> N;
  
  for(i=0; i<N; i++){
    cin >> input;
    player.push_back(input);
    rank.push_back(0);
  }
  
  for(i=0; i<N; i++){
    rank[i] = 1;
    for(j=0; j<i; j++){
      if(player[j] > player[i])
        rank[i]++;
    }
  }
  
  for(i=0; i < rank.size(); i++){
    cout << rank[i] << " ";
  }
  
  
  return 0;
}
```


## 27장. N! 표현법

임의의 n에 대하여 n!은 1부터 n가지의 곱을 의미한다. 이는 n이 커짐에 따라 급격하게 커진다. 이러한 큰 수를 표현하는 방법으로 소수들의 곱으로 표현하는 방법이 있다. 먼저 소수는 2, 3, 5, 7, 11, 13순으로 증가함을 알아야 한다. 예를 들며 825sms 0 1 2 0 로 표현이 가능한데 이는 2는 없고 3은 1번, 5는 2번, 7은 없고 11은 1번의 곱이라는 의미이다. 101보다 작은 임의의 n에 대하여 n 팩토리얼을 이와 같은 표기법으로 변환하는 프로그램을 작성해보자. 출력은 아래 예제와 같이 하도록 한다.


진~~~ 짜 못풀겟따!!!! 너무너무 어려움. 선생님 코드를 참고해야 겠다.

재귀함수를 이용해서 풀려고 했는데, 쉽지가 않다. 계속 segmentation fault 에러가 난다.




## 28장. 

자연수 n이 입력되면 n! 값에서 일의 자리부터 연속적으로 0이 몇 개 있는지 구하는 프로그램을 작성하세요.
만약 5! = 5 x 4 x 3 x 2 x 1 = 120으로 일의자리부터 연속된 0의 개수는 1입니다.
만약 12! = 479001600 으로 일의자리부터 연속된 0의 개수는 2다.

> 입력
첫 줄에 자연수 n이 입력된다.

> 출력
일의 자리부터 연속된 0의 개수를 출력한다.

```c++
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int get5 (int n);

int main(){
  int N;
  int numOf5 = 0;
  
  cin >> N;
  
  for(int i=1; i<=N; i++){
    if(i%5 == 0){
      int how_many_5 = get5(i);
      numOf5 += how_many_5;
    }
  }
  
  cout << numOf5;

}

int get5 (int n){
  if(n%5 == 0){
    return 1 + get5(n/5);
  }else{
    return 0;
  }
}

```

이 문제는 일의자리부터 연속이어서 매우 다행인 문제!! 10의 배수가 얼마나 있는지를 찾는 건데, 대충 5의 배수가 몇번 반복하고 샬라샬라하는지를 확인해주면 된다.



## 29. 3의 개수

아 코드 쓴거 날라감
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 하,,,
그래도 저거 필기한대로 풀면 된다.... 



---
layout : post
title : "[Algorithm] 따라하며 배우는 인프런 강좌! 26장 ~ 30장"
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


### 선생님 코드

나랑 거의 비슷함. 크게 다른 것 같지는 않다... 흠!!

```c
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  freopen("input.txt", "rt", stdin);
  int i, j, n, cnt=0;
  scnaf("%d", &n);
  vector<int> a(n+1);

  for(i = 1; i<= n; i++){
    scanf("%d", &a[i]);
  }

  printf("1 ");

  for(i=2; i<= n; i++){
    cnt = 0;
    for(j = i; j >= 1; j--){
      if(a[j] >= a[i]) cnt++;
    }
    print("%d", cnt+1);
  }

  return 0;
}
```

나는 이중for문 안에 j를 돌 때 앞에서부터 도는 것을 생각했는데, 선생님은 뒤에서부터 도는 것을 생각했다. 훔.. 근데 별 차이는 없을 것 같음?!

나랑 코드가 거의 비슷하긴 한데.. 난 배열을 두개 사용해야 했는데 선생님은 안그래도 괜찮으셨다. 선생님 코드가 훨씬 공간을 적게 차지할듯!

> P.S

병합정렬을 사용해서 더.. 삐르게 어쩌구하게 풀 수 있는 방법이 있다고 하셨다. 그거는 나중에 고급 알고리즘 배우는 시간에 하실 계획이신 듯!


---


## 27장. N! 표현법

임의의 n에 대하여 n!은 1부터 n가지의 곱을 의미한다. 이는 n이 커짐에 따라 급격하게 커진다. 이러한 큰 수를 표현하는 방법으로 소수들의 곱으로 표현하는 방법이 있다. 먼저 소수는 2, 3, 5, 7, 11, 13순으로 증가함을 알아야 한다. 예를 들며 825sms 0 1 2 0 로 표현이 가능한데 이는 2는 없고 3은 1번, 5는 2번, 7은 없고 11은 1번의 곱이라는 의미이다. 101보다 작은 임의의 n에 대하여 n 팩토리얼을 이와 같은 표기법으로 변환하는 프로그램을 작성해보자. 출력은 아래 예제와 같이 하도록 한다.


진~~~ 짜 못풀겟따!!!! 너무너무 어려움. 선생님 코드를 참고해야 겠다.

재귀함수를 이용해서 풀려고 했는데, 쉽지가 않다. 계속 segmentation fault 에러가 난다.

## 선생님 코드

선생님은 천재다!! 완전 쉽게 푸셨다.

```c++
#include <iostream>
#include <algorihtm>
#include <vector>

using namespace std;

int main(){
  freopen("input.txt", "rt", stdin);
  int i, j, n, tmp;

  scanf("%d", &n);
  
  vector<int> ch(n+1);

  for(i=2; i<=n; i++){
    tmp = i;
    j = 2;
    while(1){
      if(tmp%j == 0){
        tmp = tmp/j;
        ch[j]++;
      }else j++;
      if(tmp==1) break;
    }
  }

  printf("%d! = ", n);
  for(i=2; i<=n; i++){
    if(ch[i] != 0)
      printf("%d ", ch[i]);
  }

  return 0;
}
```



---

## 28장. N!에서 0의 개수

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

나는 `int get5(int n)`이라는 함수를 사용했는데, 여기서 재귀함수를 사용했다. 


### 선생님 코드

소인수분해 위에 했던 코드를 구하면 된다능. 

```c++
int n, i, j, tmp, cnt1=0, cnt2=0; //cnt1은 2의 배수 갯수, cnt2는 5의 배수 갯수

scanf("%d", &n);

for(i = 2; i<= n; i++){
  tmp = i;
  j = 2;
  while(1){
    if(tmp%j == 0){
      if(j==2) cnt1++;
      else if (j==5) cnt2++;
      else{
        //do nothing
      }
      tmp = tmp/j;
    }
    else j++;
    if(tmp == 1) break;
  }
}

if(cnt1<cnt2)
  printf("%d", cnt1);
else
  printf("%d", cnt2);

```



---

## 29. 3의 개수 (small : 구글 인터뷰)

```
잡담.. 아 코드 쓴거 날라감 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 하,,, 그래도 저거 필기한대로 풀면 된다.... 
```

와 구글 인터뷰 문제라고 한다!! 

> 문제

자연수 n이 입력되면 1부터 n까지의 자연수를 종이에 적을 때 각 숫자 중 3의 개수가 몇 개 있는지 구하려고 한다.
예를 들어 1부터 15까지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5으로 3의 개수는 2개다.
자연수 n이 입력되면 1부터 n까지의 숫자를 적을 때, 3의 개수가 몇 개인지 구하여 출력하는 프로그램을 작성하세요.

> 입력
첫 줄에 자연수의 개수 N(3<=N<=100,000)이 주어진다.

> 출력
3의 개수를 출력하세요

```c++
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    int N, i;
    int count = 0;
    
    cin >> N;
    
    string str = to_string(N);
    int length = str.length();
    
    if(N < 3){
        cout << "0" << endl;
        exit(0);
    }else if (N >= 3 && N < 10){
        cout << "1" << endl;
        exit(0);
    }else{
        //해당 자리수일때
        for(i = pow(10, length-1); i<=N; i++){
            string s = to_string(i);
            for(int j=0; j < s.length(); j++){
                if(s[j] == '3'){
                    count++;
                    break;
                }
            }
        }
        
        //해당 자리수보다 작을 때
        for(i = 1; i <= length-1; i++){
            if(i == 1){
                count++;
            }else{
                int total = 9 * pow(10, i-1);
                int sub = 8 * pow(9, i-1);
                count = count + (total - sub);
            }
        }
        cout << count << endl;
    }
    
    return 0;
}
```

### 선생님 코드 

왕간단... 왕간단하다. 약간 위에 소인수분해 했던 코드랑 비슷한 것 같기도 하다.

```c++
int main(){
  int n, tmp, i, cnt=0, digit;
  scanf("%d", &n);

  for(i=1; i<=n; i++){
    tmp = i;
    while(tmp > 0){
      digit = tmp%10;
      if(digit == 3) cnt++;
      tmp = tmp/10;
    }
  }
  printf("%d\n", cnt);
  return 0;
}
```
이거는 그냥 진짜 그냥 푼거다. 내가 위에서 푼 방식이 large인 수에서는 잘 작동될 것 같은데 여기서는 잘 안될 것 같은 느낌임.!
(핵 오래 걸림)

---

## 30장. 3의 개수는? (large)

위의 문제랑 동일.
대신 여기서는 입력이 엄청 크면 어떻게 풀거냐는 문제다.

딱히 생각나는게 없어서 29장이랑 같은 방식으로 생각함.. ㅠㅠ 선생님 강좌를 보면서 확인해봐야겠다.

### 선생님 코드

나랑 같은 내용.... 인 줄 알았으나 뭔가를 다르게 품
아니 선생님
그렇게 풀면 중복이 있잖아여 ;
어칼거임 ;; 

---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 11장 ~ 15장"
date : 2020-06-10 20:00
category : algorithm
---

오늘도 열심히 따라하는 인프런 강좌!!

## 11장. 숫자의 총 개수 (small)

문제 요약 : 숫자 하나를 입력받는데 자릿수 하나하나까지 계산하면 숫자 몇개 쓰이는가??

### 나의 코드

```c++
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
  string input;
  int res = 0;
  
  cin >> input;
  
  for(int i = 1; i <= input.length(); i++){
    if(i == input.length()){
      //cout << i << " : " << stoi(input) << " - " << pow(10, i-1) << " * " << i << endl;
      res += (stoi(input) - pow(10, i-1) + 1) * i;
    }else if (i == 1){
      res += (pow(10, i) - pow(10, i-1)) * i;
      //cout << i << "의 자리 결과 : " << res << endl;
    }else{
      res += (pow(10, i) - pow(10, i-1) + 1) * i;
    }
  }
  
  cout << res << endl;
  
  return 0;
}
```

> Key Point! : 규칙을 찾아야 한다 (수식으로 그걸 정리해야 하는 문제)



## 12장. 숫자의 총 개수 (large)

위와 동일한 문제. 근데 여기서는 입력이 100,000,000까지 옴. (호달달..) 

근데 생각한 코드 다른게 없음.. 똑같음.. 그래도 잘 움직이겠죠 님아
repl.it에서는 아주 빨리빨리 잘만 돌아감!!! 

> key point

선생님 코드도 뭐 나랑 또이또이 한거같음. ㅎ 근데 선생님 코드가 더 직관적인듯.


## 13장. 가장 많이 사용된 자릿수

요약 : n자리의 자연수가 입력되면 입력된 자연수의 자릿수 중 가장 많이 사용된 숫자를 출력하는 프로그램을 작성하세요

```c++
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

int cnt[100];

int main() {
  string input;
  int res = 0;
  int max = -2147000000;
  
  cin >> input;
  
  for(int i=0; i < input.length(); i++){
    cnt[input[i]-'0']++;
    if(max < cnt[input[i]-'0'])
      max = input[i] - '0';
  }
  
  cout << max << endl;
  
}
```

내 코드가 잘못되었었다... 선생님 코드가 맞음. 여기서 max값은 인덱스랑 그 반복된 값이랑 구분해서 사용을 해줘야했다.

```c++
int max_index = 0; //max값의 인덱스
for(int i=0; i < input.length(); i++){
  digit = input[i] - '0';
  cnt[input[digit]]++;
  
  if(cnt[max_inex] < cnt[digit]){
    max_index = digit;
  }
  else if(cnt[max_index] == cnt[digit]){
    if(max_index < digit)
      max_index = digit;
  }else{
    continue;
  }
}
```

아 머야 맞는건가? 변수를 그냥 max라고 해놓으니 이게 값인지 index인지 헷갈린다. 제대로!!하기!!!

> Key Point : 글쎄.. 배열로 생각하기?!



## 14장. 뒤집은 소수

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 예를들어 32를 뒤집으면 23이고, 23은 소수다. 
뒤집는 함수인 int reverse(int x)와 소수인자를 확인하는 함수 bool isPrime(int x)를 반드시 작성하여 프로그래밍한다.

```c++
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

int reverse(int x);
bool isPrime(int x);

int main() {
  int numOfCase;
  
  cin >> numOfCase;
  
  for(int i=0; i < numOfCase; i++){
    int input;
    cin >> input;
    int rev = reverse(input);
    
    if(isPrime(rev)){
      cout << rev << " ";
    }else{
      continue;
    }
  }
  
  return 0;
}

int reverse(int x){
  string str = to_string(x);
  reverse(str.begin(), str.end());
  return stoi(str);
}

bool isPrime(int x){
  int count = 0;
  
  for(int i = 1 ; i <= x; i++){
    if(x%i == 0)
      count++;
    
    if(count > 2)
      return false;
  }
  return true;
}

```

> Key Point : string의 reverse 함수! (얘는 헤더파일 algorithm이 필요하다)

`reverse(str.begin(), str.end())` 을 사용하면 왕빨라진다. 


근데 선생님은 c로 풀어서 그런지 다르게 `int reverse(int x)`함수를 사용하셨는데, 내용은 아래와 같다.


```c++
int reverse(int x){
  int tmp;
  int res = 0;
  while(x > 0){
    tmp = x % 10;
    res = res * 10 + tmp;
    x = x / 10;
  }
  resturn res;
}
```


선생님의 `isPrime`함수도 아래와 같다.


```c++
bool isPrime(int x){
  for(int i=2; i < x; i++){
    if(x%i == 0)
      return false;
  }
  return true;
}
```




## 15. 소수의 개수

자연수 n이 입력되면 1부터 n가지의 소수의 개수를 출력하는 프로그램을 작성하세요. 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초


```c++
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

int cnt[200001];

int main() {
  int N;
  
  cin >> N;
  
  for(int i=2; i <= N; i++){
    for(int j=i; j<=N; j = j + i){
      cnt[j]++;
    }
  }
  
  int count = 0;
  for(int i=2; cnt[i] != '\0'; i++){
    if(cnt[i]==1){
      count++;
    }
  }
  
  cout << count << endl;
  
  return 0;
}
```

> Key Point : 런타임에러 나니까 소수 구할때 배열로 생각해서 해야함!! 배수를 ~~ 해주는 것이 좋다.


선생님 코드는.. 뭔가 신기한데 사실 아직 이해하지 못했다.

선생님 코드는 아래와 같다.

```c++
int main(){
  int n, i, j, flag, cnt=0;
  scanf("%d", &n);
  for(i = 2; i <= n; i++){
    flag = 1;
    for(j=2; j*j <= i; j++){
      if(i%j==0){
        flag = 0;
        break;
      }
    }
    if(flag==1) cnt++;
  }
  printf("%d\n", cnt);
  return 0;
}
```

> Key Point! : `Flag`를 사용!!

여기서 `j * j <= i` 이부분을 이해하질 못하겠다.. 하지만 그냥 포기함. ㅎ 


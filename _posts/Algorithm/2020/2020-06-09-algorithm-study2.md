---
layout : post
title : "[Algorithm] 따라하며 배우는 알고리즘 인프런 강좌!! 6장~10장"
category : algorithm
date : 2020-06-09 20:00
---

## 6강. 숫자만 추출

요약 : 여러가지 문자열 입력받아서 그 중 숫자만 출력하는 함수를 만들어라

```c
#include <iostream>
#include <string>
using namespace std;

int main(){
  string input;
  string result = "";
  int sum;
  
  cin >> input;
  
  for(int i=0; i < input.length(); i++){
    if(input[i] >= '0' && input[i] <= '9')
      result.push_back(input[i]);
  }
  
  cout << result;
  
  int count = 0;
  for(int i=1; i <= stoi(result); i++){
    if(stoi(result)%i == 0)
      count++;
  }
  cout << " " << count;
  
  return 0;
  
}
```


## 7강. 영어 단어 복구

요약 : 빈칸도 있고 대소문자 섞인 문자열을 입력받음. 입력받은걸 공백을 없애고 전부 소문자로 바꿔버림

```c++
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int main() {
  string input;
  string result = "";
  
  getline(cin, input);
  
  for(int i=0; i < input.length(); i++){
    if(input[i] == ' '){
      continue;
    }else if(input[i] >= 'A' && input[i] <= 'Z'){
      result.push_back(input[i] - 'A' + 'a');
    }else{
      result.push_back(input[i]);
    }
    
  }
  
  cout << result << endl;
  
  return 0;
  
}

```

> Key Point : 아스키코드, getline(cin, \<string 변수명\>)


선생님의 코드에서는 for문을


```c++
for(i=0; a[i] != '\0'; i++){
  //이하생략
}
```

이렇게 표현하셨다. 왕신기..



## 8강. 올바른 괄호

문제 요약 : 대충 괄호 잘 열고 닫았는지 확인하는 것.


```c++
  #include <iostream>
  #include <string>
  #include <stdlib.h>
  #include <vector>
  using namespace std;
  
  int main() {
    string input;
    vector<char> st;
    
    cin >> input;
    
    for(int i=0; i < input.length(); i++){
      if(input[i] == '(')
        st.push_back('(');
      else if(input[i] == ')')
        st.pop_back();
      else
        cout << "Error!" << endl;
    }
    
    if(st.size() == 0)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
      
    
    return 0;
    
  }

```

> Key Point : vector 함수를 사용함! 


## 9강. 모두의 약수

숫자 하나 입력받으면 그 수 까지의 모든 수들에 대해서 약수 구하기. 이건 껌!

```c++
int main(){
  int input;
  
  cin >> input;
  
  for(int i=1; i <= input; i++){
    int count = 0;
    for(int j = 1; j <= i; j++){
      if(i%j == 0)
        count++;
    }
    cout << count << " ";    
  }  
}
```

> 쉬운 문제인줄 알았는데 아니었다!! 시간복잡도를 고려해주어야 하는 문제.

선생님의 코드에서는..

```c++
int cnt[50001];

for(int i = 1; i <= N ; i++){
  for(int j = i; j <= N; j = j + i){
    cnt[j]++;
  }
}
```

> Key Point! : j = j + i 만큼! 훨씬 조금 돌게 된다. 


## 10강. 자릿수의 합

요약 -> (1)케이스 입력 (2)케이스 수만큼 입력 -> 자릿수의 합이 가장 큰 수를 출력. 자릿수의 합이 같을 경우에는 값이 큰 수 출력

```c++
  #include <iostream>
  #include <string>
  #include <stdlib.h>
  #include <vector>
  using namespace std;
  
  int digit_sum(int x);
  
  int main() {
    int numOfInput;
    int max = 0;
    int result;
    
    cin >> numOfInput;
    
    for(int i = 0; i < numOfInput; i++){
      int input;
      cin >> input;
      int digitsum = digit_sum(input);
      if(max < digitsum){
        max = digitsum;
        result = input;
      }else if(max == digitsum){
        result = (result > input) ? result : input;
      }else{
        continue;
      }
    }
    
    cout << result << endl;
    
  }
  
  int digit_sum(int x){
    int sum = 0;
    
    while(true){
      if(x/10 == 0){
        sum += x%10;
        break;
      }else{
        sum += x%10;
        x = x * 0.1;
      }
    }
    
    return sum;
  }

```

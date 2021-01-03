---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 54장 ~ 55장 "
date : 2020-06-22 19:00
category : algorithm
---

## 54장. 올바른 괄호 (stack)

괄호가 입력되면 올바른 괄호이면 "YES", 올바르지 않으면 "NO"를 출력합니다.
(())() 이것은 괄호의 쌍이 올바르게 위치하는 거지만, (()()))은 올바른 괄호가 아니다.

> 입력

첫 번째 줄에 괄호 문자열이 입력된다. 문자열의 최대 길이는 30이다.

> 출력

첫 번째 줄에 YES, NO를 출력한다.


```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    string input;
    vector<char> st;
    
    cin >> input;
    
    for(int i=0; i<input.size(); i++){
        if(input[i]=='('){
            st.push_back('(');
        }else{
            st.pop_back();
        }
    }
    
    if(st.size()==0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    
    return 0;
}
```

껌!! 예전에 구글 면접볼 때 이 문제 풀었었는데.. (아련...)


## 55장. 기차 운행(stack 응용)

A도시에서 출발한 기차는 B도시로 도착한다. 그런데 도로 중간에 T자형 교차로가 있어 출발한 기차의 도착 순서를 조정할 수 있다. 

교차로에서는 다음과 같은 두 개의 작업을 한다.

P(push) 작업 : A도시에서 오는 기차를 교차로에 넣는다.
O(out) 작업 : 교차로에 들어온 가장 최근 기차를 B도시로 보낸다.

만약 2 1 3 기차 번호 순으로 A도시에서 출발하더라도 B도시에는 T교차로를 이용하여 1 2 3 순으로 도착하게 할 수 있다.

그 작업 P, P, O, O, P, O t순으로 작업을 하면 B 도시에 1, 2, 3 순으로 도착한다.

1부터 N까지 번호를 가진 기차가 A도시에서 어떤 순으로 출발하든 B도시에 번호순으로 도착하도록 하는 교차로 작업을 출력한다. 모든 기차는 교차로에 들어가야만 B도시로 갈 수 있다. 번호 순서대로 도착이 불가능하면 impossible이라고 출력한다.

> 입력

첫 번째 줄에 자연수 N(3<=N<=30)가 주어진다.
두 번째 줄에 A도시에서 출발하는 기차 번호 순의 차례대로 입력된다.

> 출력

교차로 작업을 순서대로 P와 O를 출력한다.

```c++
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    int N;
    vector <int> input;
    string str = "";
    vector<int> result;
    
    cin >> N;
    
    //이걸 string으로 받으면 안되는구나!!
    for(int i=0; i<N; i++){
        int t;
        cin >> t;
        input.push_back(t);
    }
    
    int i = 0;
    /*
    while(true){
        if(i == input.size())
            break;
        cout << i << "번째 반복" << endl;
        if(result.size() == 0){
            result.push_back(input[i]);
            str += 'P';
        }else{
            if(input[i] > result[result.back()]){
                cout << "ch2" << endl;
                result.pop_back();
                str += 'O';
                result.push_back(input[i]);
                str += 'P';
            }else{
                cout << "ch3" << endl;
                result.push_back(input[i]);
                str += 'P';
            }
        }
        cout << "input[" << i << "] : " << input[i] << ", str : " << str << endl;
        
        i++;
    }
    
    */
    
    for(int i=0; i<input.size(); i++){
        if(result.size() == 0){
            result.push_back(input[i]);
            str += 'P';
        }else{
            if(result.back() < input[i]){
                while(result.back() < input[i]){
                    result.pop_back();
                    str += 'O';
                    //cout << "result 마지막 : "<< result.back() << endl;
                    if (result.size() == 0) break;
                }
                result.push_back(input[i]);
                str += 'P';
            }else{
                result.push_back(input[i]);
                str += 'P';
            }
        }
        //cout << "input[" << i << "] : " << input[i] << ", str : " << str << endl;
    }
    
    while(result.size() != 0){
        result.pop_back();
        str += 'O';
    }
    
    cout << str << endl;
    
    return 0;
}
```

너무 오래걸린다... 이렇게 오래걸리면 안되는건데!!!
풀기는 어떻게 푼 것 같으나..!!!! 으아악~ㅎㅎ

여기서 포인트!!

`v.back()` 이거는 vector의 마지막 원소를 가리키는 것이다!!

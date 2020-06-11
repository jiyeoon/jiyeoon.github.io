---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 16장 ~ 20장"
date : 2020-06-11 20:00
category : algorithm
---

오늘도 꾸준하게 하는 알고리즘 공부~

## 16강 Anagram (아나그램 : 구글 인터뷰 문제)

문제 : Anagram이란 두 문자열이 알파벳의 나열 순서가 다르지만 구성이 일치하면 같은 단어를 말한다.
애너그램이 맞는지 아닌지를 출력하는 프로그램을 짜라!

> Key Point : 나는 여기서 a~z, A~Z를 배열로 생각하고 그 해당 문자가 나오면 해당 문자의 부분을 ++하는 형식으로 했다.

```c++
#include <iostream>
#include <string>
using namespace std;

int main(){
    string input1, input2;
    int digit;
    
    int input1_alphabet_lower[26] = {0};
    int input1_alphabet_upper[26] = {0};
    int input2_alphabet_lower[26] = {0};
    int input2_alphabet_upper[26] = {0};
    
    
    cin >> input1 >> input2;
    
    if(input1.size() != input2.size()){
        cout << "NO" << endl;
        return 0;
    }
    
    for(int i=0; i< input1.size(); i++){
        if(input1[i] >= 'A' && input1[i] <= 'Z'){
            digit = input1[i] - 'A';
            //cout << "digit : " << digit << endl;
            input1_alphabet_upper[digit]++;
        }else if (input1[i] >= 'a' && input1[i] <= 'z'){ //소문자면
            digit = input1[i] - 'a';
            input1_alphabet_lower[digit]++;
        }else{
            cout << "Error!" << endl;
        }
    }
    
    for(int i=0; i<input2.size(); i++){
        if(input2[i] >= 'A' && input2[i] <= 'Z'){
            digit = input2[i] - 'A';
            input2_alphabet_upper[digit]++;
        }else if (input2[i] >= 'a' && input2[i] <= 'z'){
            digit = input2[i] - 'a';
            input2_alphabet_lower[digit]++;
        }else{
            cout << "Error!" << endl;
        }
    }
    
    
    for(int i=0; i < 26 ; i++){
        if(input1_alphabet_lower[i] != input2_alphabet_lower[i]){
            cout << "NO" << endl;
            return 0;
            //break;
        }
        if(input1_alphabet_upper[i] != input2_alphabet_upper[i]){
            cout << "NO" << endl;
            return 0;
            //break;
        }
    }
    
    cout << "YES" << endl;
    
    
    return 0;
}

```


## 17강. 선생님 퀴즈

현수네 반은 학생이 N명 있다. 수업도중 선생님이 잠깐 자리를 비워야 하는데 그동안 학생들이 떠들거나 놀지 않도록 각 학생들에게 퀴즈를 냈다. 선생님은 각 학생들에게 숫자가 적힌 카드를 줬는데, 각 학생들은  1부터 자기 카드에 적힌 숫자까지의 합을 구하는 퀴즈다.

첫줄에 반 학생수인 자연수 N이 주어진다.
두번째 줄부터는 1번 학생부터의 카드에 적힌 수와 학생이 구한 정답이 공백을 사이에 두고 입력된다.

```c++
#include <iostream>
#include <string>
using namespace std;

int main(){
    int N;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        int num, sum;
        cin >> num >> sum;
        
        if(sum != num*(num+1)/2)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
    
    return 0;
}
```

그냥 1부터 N까지의 합을 구하는 수학 공식을 사용하면 매우 쉽다!


## 18강. 층간소음

T편한 세상 아파트는 층간소음 발생시 윗집의 발뺌을 방지하기 위해 애초에 아파트를 지을 때 바닥에 진동센서를 설치했다. 이 센서는 각 세대의 층간 진동 소음 측정치를 초단위로 아파트 관리실에 실시간으로 전송한다. 한 세대의 측정치가 M값을 넘으면  세대 호수와 작은 경보음이 관리실 모니터에서 울린다. 한 세대의 N초동안의 실시간 측정치가 주어지면 최대 연속으로 경보음이 울린시간을 구하세요. 경보음이 없으면 -1이 출력된다.

> 입력

첫번째 줄에는 자연수 N과 M이 주어짐
두번째 줄에는 N개의 측정치값이 초 순서대로 입력된다.

```c++
#include <iostream>
#include <string>
using namespace std;

int main(){
    int N, M;
    
    cin >> N >> M;
    
    int count = 0;
    int max = -1;
    int input;
    
    int flag = 0; //flag가 1이면 연속중. 0이면 연속 아니라는 뜻.
    for(int i=0; i<N; i++){
        cin >> input;
        
        if(input > M){
            if(flag == 0){
                flag = 1;
                count++;
            }else{
                count++;
            }
        } else{
            flag = 0;
            count = 0;
        }
        
        if(max < count){
            max = count;
        }
    }
    
    if(max == 0){
        cout << "-1" << endl;
    }else
        cout << max << endl;
    
    return 0;
}
```

껌이군 후후후후

## 19. 분노 유발자

한줄에 앉은키 정보가 주어지면 뒷사람 모두의 시야를 가리는 사람이 몇명 있는지 출력하는 프로그램

> 입력
첫 줄에 앉은 학생수 N이 주어짐
두번째 줄에 N명의 앉은키 정보가 앞자리 학생부터 차례대로 주어진다.

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int N, input;
    vector<int> st;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        st.push_back(input);
    }
    
    int cnt = 0;
    
    for(int i=0; i < st.size() - 1 ; i++){
        int flag = 0; //flag가 0이면 뒤에 큰 수가 없다 1이면 뒤에 큰 수가 있다
        for(int j = i+1; j < st.size(); j++){
            if(st[j] > st[i]){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            cnt++;
        }
    }
    
    cout << cnt << endl;
    return 0;
}
```

여기서 포인트는 `flag`와 `st.size()-1` 부분이었다. 반복문을 한번 더 잘 생각해줘야 했던 문제!!

## 20. 가위 바위 보

A, B 두사람이 가위바위보를 한다. A가 이기면 A를 출력, B가 이기면 B를 출력하고 비기면 D를 출력한다.

> 입력
첫번째 줄에는 게임 횟수 N를 입력.
두번째 줄에는 A가 낸 가위, 바위, 보 정보 N개가 주어짐.
세번재 줄에는 B가 낸 가위, 바위, 보 정보 N개가 주어짐.

```c++
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void match(int a, int b);

int main(){
    int N, input;
    
    vector <int> A;
    vector <int> B;
    
    cin >> N;
    
    for(int i=0; i<N; i++){
        cin >> input;
        A.push_back(input);
    }
    
    for(int i=0; i<N; i++){
        cin >> input;
        B.push_back(input);
    }
    
    for(int i=0; i<N; i++){
        match(A[i], B[i]);
    }
    
    
    return 0;
}

void match(int a, int b){
    if(a==b){
        cout << "D" << endl;
        return;
    }
    
    if(a==1){
        if(b==2) cout << "B" << endl;
        else cout << "A" << endl; //b==3
    }else if (a==2){
        if(b==1) cout << "A" << endl;
        else cout << "B" << endl;
    }else{ //a==3
        if(b==1) cout <<"B" << endl;
        else cout << "A" << endl;
    }
}
```

껌이라능 선생님은 어떻게 푸셨으려나?
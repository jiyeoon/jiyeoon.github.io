---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 47장 ~ 48장"
date : 2020-06-19 19:00
category : algorithm
---

오늘도~~ 나는~~ 알고리즘 존버를 한다네~
요즘 면접 준비에 한창인데, (3일만에 데이터 사이언티스트되기?) 하루에 하나라도 이렇게 하려고 노력하고 있다. ㅠ 화이팅!!! 할수있다!!!!
꿈은!!!!! 이루어진다!!!!!! Work Hard! Think Big!! Achieve Goal!!!

## 47장. 봉우리

지도 정보가 N*N 격자판에 주어진다. 각 격자에는 그 지역의 높이가 씌여 있다. 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역이다. 봉우리 지역이 몇 개 있는지 알아내는 프로그램을 작성하시오.

격자의 가장자리는 0으로 초기화 되어있다고 가정한다.

> 입력

첫 줄에 자연수 N이 주어진다. (1<= N <= 50)
두번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

> 출력

봉우리의 개수를 출력하시오.

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int a[51][51];

bool isTop(int i, int j);

int main(){
    int cnt=0;
    int N;
    
    cin >> N;
    
    cout << endl;
    for(int i=0; i<N+2; i++){
        for(int j=0; j <N+2; j++){
            if(i==0 || i == N+1 || j==0 || j==N+1){
                a[i][j] = 0;
            }else{
                cin >> a[i][j];
            }
            //cout << a[i][j];
        }
        //cout << endl;
    }
    
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(isTop(i, j)){
                //cout << "[" << i << ", " << j << "]" << endl;
                cnt++;
            }
        }
    }
    
    cout << cnt << endl;
    
    return 0;
}

bool isTop(int i, int j){
    if(a[i][j] > a[i-1][j] &&
       a[i][j] > a[i][j-1] &&
       a[i][j] > a[i+1][j] &&
       a[i][j] > a[i][j+1])
        return true;
    else
        return false;
}

/* input
 5
 5 3 7 2 3
 3 7 1 6 1
 7 2 5 3 4
 4 3 6 4 1
 8 7 3 5 2
 
 */
```

굳! 잘 돌아간다.
이차원 배열을 활용해야 했던 문제인데, 여기서 포인트는 `전역변수`를 활용하는 것!! (근데 굳이 안써도 될 것 같기는 하지만..?!)



---

## 48장. 각 행의 평균과 가장 가까운 값

9x9 격자판에 쓰여진 81개의 자연수가 주어질 때, 각 행의 평균을 구하고 그 평균과 가장 가까운 값을 출력하는 프로그램을 작성하세요. 평균은 소수점 첫째 자리에서 반올림 한다. 평균과 가까운 값이 두개이면 그 중 큰 값을 출력하세요

> 입력

첫째 줄부터 아홉번째 줄까지 한 줄에 아홉개씩 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

> 출력

첫째 줄에 첫번째 줄부터 각 줄에 각 행의 평균과 그 행에서 평균과 가장 가까운 수를 출력한다.

```c++
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int a[9][9];
int avg[9];


int main(){
    int close_value[9];
    int sum;
    int tmp;
    
    for(int i=0; i<9; i++){
        sum = 0;
        for(int j=0; j<9; j++){
            cin >> a[i][j];
            sum += a[i][j];
        }
        avg[i] = round(sum/9.0);
    }
    
    for(int i=0; i<9; i++){
        int min = avg[i] - a[i][0];
        if(min < 0) min = -min;
        close_value[i] = a[i][0];
        
        for(int j=1; j<9; j++){
            tmp = avg[i] - a[i][j];
            if(tmp<0) tmp = -tmp;
            if(tmp < min){
                min = tmp;
                close_value[i] = a[i][j];
            }else if (tmp == min){
                if(close_value[i] < a[i][j])
                    close_value[i] = a[i][j];
            }else{
                continue;
            }
        }
        
        //cout << endl << i+1 << "번째 끝!" << close_value[i] << " " << endl;
    }
    
    for(int i=0; i<9; i++){
        cout << avg[i] << " " << close_value[i] << endl;
    }
    
    return 0;
}


/* input
 
 3 23 85 34 17 74 25 52 65
 10 7 39 42 88 52 14 72 63
 87 42 18 78 53 45 18 84 53
 34 28 64 85 12 16 75 36 55
 21 77 45 35 28 75 90 76 1
 25 87 65 15 28 11 37 28 74
 65 27 75 41 7 89 78 64 39
 47 47 70 45 23 65 3 41 44
 87 13 82 38 50 12 48 29 80
 
 */
```

입력이 매우 큼..


여기서 포인트!!!

1. 반올림 함수는 `round(float f)` !!!
2. 논리를 잘 생각해야 했다. 쉬운 문제인데 조금 오래 걸림.
---
layout : post
title : "Recap Coding Test"
cateogry : algorithm
date : 2020-08-01 23:00
---

Recap Coding Test!

### [DE-3] 달팽이 출력제출완료

자연수 k와 n을 입력받아, 1부터 n^2 까지의 수가 달팽이 등껍질 모양(시계 방향)으로 출력되는 프로그램을 작성해주십시오.

자연수 k는 1부터 4까지의 자연수이며, k에 따라 출발 지점이 변경됩니다.

- k가 1이면, 왼쪽 위에서 출발
- k가 2이면, 오른쪽 위에서 출발
- k가 3이면, 오른쪽 아래에서 출발
- k가 4이면, 왼쪽 아래에서 출발

예를 들어 k=1, n=5가 입력되었을 때, 1부터 25까지의 수가 5 × 5 형태의 2차원 배열에 달팽이 등껍질 모양으로 정렬되어 다음과 같은 형태로 출력되어야 합니다.

```
	1    2    3    4    5
   16   17   18   19    6
   15   24   25   20    7
   14   23   22   21    8
   13   12   11   10    9
```

만약 k=2, n=5 이면,

```
   13   14   15   16    1
   12   23   24   17    2
   11   22   25   18    3
   10   21   20   19    4
    9    8    7    6    5
```

만약 k=3, n=5 이면,

```
    9   10   11   12   13
    8   21   22   23   14
    7   20   25   24   15
    6   19   18   17   16
    5    4    3    2    1
```

만약 k=4, n=5 이면,

```
5    6    7    8    9
4   19   20   21   10
3   18   25   22   11
2   17   24   23   12
1   16   15   14   13

```

> 입력 설명

두 정수 k, n 
(k는 1이상 4 이하의 자연수, n은 15 이하의 자연수)

> 출력 설명

k에 따라 달라지는 출발점에서 1부터 n2 까지의 수를 달팽이 등껍질 모양으로 정렬한 2차원 배열 (n × n) 출력

```python
def f(x, y, vec, n):
    m = []
    res = [[0]*n for _ in range(n)] #0으로 초기화
    for i in range(n*n):
        res[x][y] = i+1 #m[0]
        #print("res[", x, "][", y,"] : ", res[x][y], " vec : ", vec)
        if vec == 1: # right
            y = y + 1
            if y == n-1 or res[x][y] != 0:
                vec = vec + 1
            if res[x][y] != 0:
                y = y - 1
                x = x + 1
        elif vec == 2: #down
            x = x + 1
            if x == n-1 or res[x][y] != 0:
                vec = vec + 1
            if res[x][y] != 0:
                x = x - 1
                y = y - 1
        elif vec == 3: #left
            y = y - 1
            if y == 0 or res[x][y] != 0:
                vec = vec + 1
            if res[x][y] != 0:
                y = y + 1
                x = x - 1
        else: #up
            x = x - 1
            if x == 0 or res[x][y] != 0:
                vec = vec + 1
            if res[x][y] != 0:
                x = x + 1
                y = y + 1
        if vec >= 5:
            vec = vec - 4
    return res

k, n = list(map(int, input().split()))

# vec : 방향 / right = 1, down = 2, left = 3, up = 4
if k == 1: # 왼쪽 위에서 출발
    x = 0
    y = 0
    vec = 1                
elif k == 2: # 오른쪽 위에서 출발 down -> left -> up -> right
    x = 0
    y = n-1
    vec = 2
elif k == 3: # 오른쪽 아래에서 출발 left -> up -> right -> down
    x = n-1
    y = n-1
    vec = 3
elif k == 4: # 왼쪽 아래에서 출발
    x = n-1
    y = 0
    vec = 4
else:
    print("-1")

res = f(x, y, vec, n)
    
for i in range(n):
    for j in range(n):
        print("%5d" %res[i][j], end =' ')
    print("")
```

> 해설

처음 start point를 입력받고, 방향을 입력받으면 그대로 달팽이 출력을 수행할 수 있도록 했다.  달팽이 출력은 알고보면 크게 어렵지 않았는데, 달팽이는 항상 `right -> down -> left -> up` 의 순서를 유지했어서 항상 방향을 순차적으로 늘려주면 괜찮았다. 마지막에 `print("%5d")`를 쓰면서 빈칸을 일정하게 출력할 수 있도록 맞춰주면서 마무리.

---

### [DE-2] 괄호 짝 맞추기제출완료

대괄호 , 중괄호 \{ \}, 소괄호 \( \)가 짝이 맞게 적절히 배치되어 있는지를 판별하는 프로그램을 작성하십시오.

각 괄호의 우선순위는 상관하지 않습니다. 예를 들어, \{\[\]\} 와 같이 중괄호 안에 대괄호가 들어있어도 적절히 배치되어 있는 것으로 판별합니다.

괄호 외에도 -,+ 문자가 존재 할 수 있으며,

- \- 가 입력될 경우, 왼쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 왼쪽에는 -가 입력되지 않습니다.)
- \+ 가 입력될 경우, 오른쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 오른쪽에는 +가 입력되지 않습니다.)

ex. \[\(\-\)\)\] , \(\(\-\+\+\) , \{\{\-\(\-\+\)\}\+\}는 짝이 맞게 배치되어 있다고 판별합니다.

> 입력 설명

임의의 괄호와 +,- 배치

> 출력 설명

짝이 맞는 적절한 배치의 경우 True 출력, 그렇지 않을 경우 False 출력

> 입/출력 예시

예시 1

입력

```
()((({}})({}[]]
```

출력

```python
False
```

예시 2

입력

```python
((((--+++))){[]}
```

출력

```python
True
```

> 나의 코드

```python
k = input()
new_str = ""
st = []

for i in range(len(k)):
    if k[i] == "+":
        #print("i : ", i, end = '')
        for j in range(i+1, len(k)):
            if k[j] != "+" and k[j] != "-":
                #print(" k[j] : ", k[j])
                new_str += str(k[j])
                break
    elif k[i] == "-":
        for j in range(i, -1, -1):
            if k[j] != "+" and k[j] != "-":
                new_str += str(k[j])
                break
    else:
        new_str += str(k[i])

#print("")
#print(new_str)

k = new_str
for i in range(len(k)):
    ch = k[i]
    if ch == "+":
        for j in range(i, n+1, 1):
            if k[j] != "+" and k[j] != '-':
                ch = k[j]
                break
    elif ch == "-":
        for j in range(i, -1, -1):
            if k[j] != "+" and k[j] != '-':
                ch = k[j]
                break
    else:
        ch = ch
    
    if ch == ")":
        if st[-1] == "(":
            st.pop(-1)
        else:
            st.append(ch)
    elif ch == "}":
        if st[-1] == "{":
            st.pop(-1)
        else:
            st.append(ch)
    elif ch == "]":
        if st[-1] == '[':
            st.pop(-1)
        else:
            st.append(ch)
    elif ch == "(" or ch == "[" or ch == "{":
        st.append(ch)
    else:
        continue
    
if len(st) == 0:
    print("True")
else:
    print("False")
```

> 해설

+와 - 를 괄호로 처리해주는 부분이 포인트! 

---

### [DE-4] 유저 세그먼트 송금액 분석하기

어떤 특성을 가진 유저들에 대한 송금액을 분석해보고자 합니다.

'20대 이면서, IOS' 인 유저들의 '2020년 7월 1일'에 송금﻿한 은행별 송금액의 합을 출력하십시오.

송금액의 합 내림차순으로 정렬합니다.

테이블 구조

1. USERS

|ID|NAME|
|:---:|:---:|
|INT|VARCHAR(20|

2. SEGMENTS

|ID|NAME|
|:---:|:---:|
|INT|VARCHAR(20)|

3. USER_SEGMENT

|ID|USER_ID(USERS.ID)|SEGMENT_ID(SEGMENTS.ID)
|:---:|:---:|:---:|
|INT|INT|INT|

4. BANKS

|ID|NAME|
|:---:|:---:|
|INT|VARCHAR(20)|

5. TRANSFER

|ID|SEND_USER_ID (USERS.ID) | SEND_BANK_ID (BANKS.ID) | RECEIVE_USER_ID (UESRS.ID)|RECEIVE_BANK_ID(BANKS.ID)|TRANSFER_AMOUNT(송금액)|
|:---:|:---:|:---:|:---:|:---:|:---:|
|INT|INT|INT|INT|INT|DATETIME|


```sql
SELECT BANKS.NAME, SUM(TRANSFER_AMOUNT)
	FROM BANKS, TRANSFER
	WHERE TRANSFER_DATE >= '2020-07-01' AND BANKS.ID = SEND_BANK_ID 
	AND SEND_USER_ID IN (
		SELECT USER_ID FROM USER_SEGMENT
		WHERE SEGMENT_ID = 1 OR SEGMENT_ID = 5 
		GROUP BY USER_ID
		HAVING COUNT(USER_ID) > 1
	)
	GROUP BY SEND_BANK_ID
	ORDER BY SUM(TRANSFER_AMOUNT) DESC;
```

---

### 후기 아닌 후기

- SQL은 처음이었는데 나름 열심히 잘 푼 것 같다. 정보처리기사의 힘.. 근데 저렇게 푸는게 좋은 방법은 아닌 느낌이다. `WHEN TRANSFER_DATE ~` 이부분이 잘못되었는데 `=` 을 사용하면 잘 듣지가 않아서.. 그냥 써버림.
- 파이썬을 이번주에 조금 해서 다행이다. 안했으면 정말 한참 헤맸을 것 같은 느낌이다.
- 왜이렇게 코드가 길고 가독성이 떨어지는지 모르겠다.
- 첫번째 문제는 너무 쉬웠는데, 모든 case에서 정답이 나오질 않았다. 왜인지는 나도 잘 모르겠다.
    - 뭔가 경계값에서 이상이 있을 것 같은 느낌이었다.
- 마지막 두 문제는 쳐다도 못보고 끝내버렸다. 사실 시간이 있었으면 풀었을 것 같지만 10분 남겨놓고 풀자니 못풀겠었다. (ㅠㅠ)
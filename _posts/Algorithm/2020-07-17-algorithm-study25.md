---
layout : post
title : "[Algorithm] 인프런 강좌 따라하며 배우는 알고리즘! 80장"
category : algorithm
date : 2020-07-17 23:00
---

## 80장. 다익스트라 알고리즘

> Before we go, 다익스트라란?

![img](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

Dijkstra, 다익스트라 알고리즘은 도로 교통망 같은 곳에서 나타날 수 있는 그래프에서 꼭짓점 간의 **최단경로**를 찾는 알고리즘이다.

다이나믹 프로그래밍을 이용해 최단 경로를 찾는 알고리즘으로, 하나의 최단 거리를 구할 때 그 이전에 구했던 최단 거리 정보를 그대로 사용한다.

#### 원리

특정한 하나의 정점을 잡고, 그 정점과 이웃한 정점들의 비용을 각각 확인한다.

그 후, 이웃한 정점들 중 가장 비용이 적게 드는 정점을 기준으로 다시 한번 확인한다.

이걸 반복하면서 현재까지 알고있던 최단 경로를 계속 갱신해나간다.

즉, 다음과 같은 과정을 거친다.

1. 출발 노드 설정
2. 출발 노드를 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중에서 가장 비용이 적게 드는 노드 선택
4. 해당 노드를 거쳐 특정한 노드로 가는 경우를 고려하여 최소 비용 갱신
5. 3번 4번 과정 반족

#### 구현

구현할 때는 **이차원 배열**을 이용한다. 각 배열의 값은 특정 행에서 특정 열로 가는 비용이다.

```c++
// 선형 탐색 방법
// 시간복잡도: O(n^2)

#include <stdio.h>

int number = 6; // 정점의 개수
int INF = 1000000000; // 무한대 표현 

// 전체 그래프 초기화
int a[6][6] = {
    {0, 2, 5, 1, INF, INF},
    {2, 0, 3, 2, INF, INF},
    {5, 3, 0, 3, 1, 5},
    {1, 2, 3, 0, 1, INF},
    {INF, INF, 1, 1, 0, 2},
    {INF, INF, 5, INF, 2, 0}
};

bool visited[6]; // 방문한 노드인지 여부 기록 
int distance[6]; // 최단 거리(비용) 저장

// 가장 최소 거리를 가지는 정점 반환(방문하지 않았던 노드 중)
int getSmallIndex() { 
    int min = INF;
    int index = 0;

    for(int i=0;i<number;i++) {
        // 방문하지 않았고, 현재 최솟값보다 더 작은 비용을 가지는 거리가 존재한다면,
        // 최솟값 갱신
        if(distance[i] < min && !visited[i]) {
            min = distance[i];
            index = i; // 최소 비용의 위치 기억 
        }
    }
    return index;  
}

// 다익스트라 수행(특정 정점에서 다른 모든 정점으로 가는 최소비용 구하는 함수)
void dijkstra(int start) {
    for(int i=0;i<number;i++) {
        distance[i] = a[start][i]; // 시작점에서 출발했을 때, 모든 경로까지의 비용 담아줌 
    }
    visited[start] = true; // 시작점 방문

    for(int i=0;i<number-2;i++) { // 첫 노드, 마지막 노드 제외(-2)
        int current = getSmallIndex(); // 현재 방문하지 않은 노드 중, 가장 비용이 적게드는 인덱스를 가져오고,
        visited[current] = true; // 방문처리
        
        // 그 노드에 인접한 모든 노드 확인
        for(int j=0;j<number;j++) {
            if(!visited[j]) {
                if(distance[current] + a[current][j] < distance[j]) {
                    distance[j] = distance[current] + a[current][j];
                }
            }
        }
    }
}

int main(void) {
    dijkstra(0);
    for(int i=0;i<number;i++) {
        printf("%d ", distance[i]);
    } 
}
```

우선순위 큐(heap)을 사용하면 시간을 훨씬 줄일 수 있다.

```c++
// 우선순위 큐(heap구조)
// O(N * logN)
// pair 비교는 첫번째 -> 두 번째 순이다.. pair를<거리,노드>로 바꿔야할듯..?

#include <iostream>
#include <vector>
#include <queue> // 힙 구조를 사용하기 위함(우선순위 큐)

using namespace std;

int number = 6;
int INF = 1000000000;

vector<pair<int, int> > a[7]; // 간선 정보(pair 형태로 자신과 연결된 노드 정보 저장)

int d[7]; // 최소 비용

void dijkstra(int start) {
    d[start] = 0; // 탐색 시작하는 노드의 최소비용은 0

    priority_queue<pair<int, int> > pq; // 힙구조 유지

    pq.push(make_pair(start, 0));
    
    // 가까운 순서대로 처리 -> 큐 사용
    while(!pq.empty()) { // 우선순위 큐가 비어있지 않다면 
        int current = pq.top().first; // 큐의 가장 위에는 가장 적은 비용을 가진 node의 정보가 들어있다.

        // 짧은 것이 먼저 오도록 음수화
        int distance = -pq.top().second;

        pq.pop();

        // 최단 거리가 아닌 경우 스킵
        if(d[current] < distance) continue;

        for(int i=0;i<a[current].size();i++) {
            // 선택된 노드의 인접노드를 담아줌 
            int next = a[current][i].first;

            // 선택된 노드를 거쳐서 인접노드로 가는 비용 계산
            int nextDistance = distance + a[current][i].second;

            // 기존의 비용과 비교
            if(nextDistance < d[next]) {
                d[next] = nextDistance;
                pq.push(make_pair(next, -nextDistance));
            }
        }

    }

}

int main(void) {
    for(int i=1;i<=number;i++) {
        d[i] = INF;
    }

    a[1].push_back(make_pair(2,2)); // 1번 노드에서 2번 노드로 가는 비용은 2
    a[1].push_back(make_pair(3,5)); // 1번 노드에서 3번 노드로 가는 비용은 5
    a[1].push_back(make_pair(4,1));

    a[2].push_back(make_pair(1,2));
    a[2].push_back(make_pair(3,3));
    a[2].push_back(make_pair(4,2));

    a[3].push_back(make_pair(1,5));
    a[3].push_back(make_pair(2,3));
    a[3].push_back(make_pair(4,3));
    a[3].push_back(make_pair(5,1));
    a[3].push_back(make_pair(6,5));

    a[4].push_back(make_pair(1,1));
    a[4].push_back(make_pair(2,2));
    a[4].push_back(make_pair(3,3));
    a[4].push_back(make_pair(5,1));

    a[5].push_back(make_pair(3,1));
    a[5].push_back(make_pair(4,1)); 
    a[5].push_back(make_pair(6,2));

    a[6].push_back(make_pair(3,5));
    a[6].push_back(make_pair(5,2));

    dijkstra(1);

    for(int i=1;i<=number;i++) {
        printf("%d ", d[i]);
    }
}
```
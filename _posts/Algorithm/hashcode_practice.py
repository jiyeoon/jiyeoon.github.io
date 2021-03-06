from itertools import combinations
import argparse

def get_xyz_list(n, a, b, c):
    for z in range(c, -1, -1):
        for y in range(b, -1, -1):
            for x in range(a, -1, -1):
                if 2*x + 3*y + 4*z <= n:
                    yield [x, y, z]

# 그다음에 해야할 것이 combination 만들기.. 
def get_combination_list(pizza):
    comb_list = {
        2: [], 
        3: [],
        4: []
    }
    # 2개일 때
    for i in combinations(range(len(pizza)), 2):
        # 여기서.. 잘해야한다... 
        tmp = []
        for j in range(2):
            tmp += pizza[i[j]]
        comb_list[2].append([i, len(set(tmp))])
    
    # 3개일때
    for i in combinations(range(len(pizza)), 3):
        # 여기서.. 잘해야한다... 
        tmp = []
        for j in range(3):
            tmp += pizza[i[j]]
        comb_list[3].append([i, len(set(tmp))])
        
    # 4개일때
    for i in combinations(range(len(pizza)), 4):
        # 여기서.. 잘해야한다... 
        tmp = []
        for j in range(4):
            tmp += pizza[i[j]]
        comb_list[4].append([i, len(set(tmp))])
    
    # 정렬하기
    comb_list[2].sort(key=lambda x : -x[1])
    comb_list[3].sort(key=lambda x : -x[1])
    comb_list[4].sort(key=lambda x : -x[1])
    
    return comb_list
    # 여기에 2개일때는 어떤피자 어떤피자, 몇개인지 #[[0, 1], 3] => 0번피자 1번피자, 3개 이런식으로. 
    # 3개일 때는 어떤피자 어떤피자 어떤피자, 몇개인지 이렇게.. 

def solution(n, a, b, c, pizza):
    comb = get_combination_list(pizza) # combination을 받아서..
    val = 0 # 여기에 값.. 
    score = 0 # 얻게될 점수
    # res 형식이 첫번째 줄에는 팀 수, 두번째 줄에는 몇명인 팀에서 몇번 피자를 배달할 것인지
    prev_res = []
    prev_score = 0
    
    for x, y, z in get_xyz_list(n, a, b, c):
        score = 0
        res = []
        used_pizza = set()
        
        idx = 0
        for i in range(z):
            while idx < len(comb[4]):
                if set(comb[4][idx][0]).isdisjoint(used_pizza):
                    score += comb[4][idx][1]**2
                    res.append([4] + list(comb[4][idx][0]))
                    used_pizza.update(set(comb[4][idx][0]))
                    break
                else:
                    idx += 1
        
        idx = 0
        for i in range(y):
            while idx < len(comb[3]):
                if set(comb[3][idx][0]).isdisjoint(used_pizza):
                    score += comb[3][idx][1]**2
                    res.append([3] + list(comb[3][idx][0]))
                    used_pizza.update(set(comb[3][idx][0]))
                    break
                else:
                    idx += 1
        
        idx = 0
        for i in range(x):
            while idx < len(comb[2]):
                if set(comb[2][idx][0]).isdisjoint(used_pizza):
                    score += comb[2][idx][1]**2
                    res.append([2] + list(comb[2][idx][0]))
                    used_pizza.update(set(comb[2][idx][0]))
                    break
                else:
                    idx += 1

        if prev_score >= score:
            break
        else:
            prev_score = score
            prev_res = res
    
    return [len(prev_res)] + prev_res[:]
            
def main(file_path):
    f = open(file_path, "r")
    line = f.readline()
    n, a, b, c = list(map(int, line.split()))
    pizza = []
    while True:
        line = f.readline()
        if line:
            pizza.append(line.split()[1:])
        else:
            break
    f.close()

    res = solution(n, a, b, c, pizza)
    f = open(file_path + "_submission", 'w')
    for one_res in res:
        try :
            data = ' '.join([str(s) for s in one_res]) + '\n'
        except:
            data = str(one_res) + '\n'
        f.write(data)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    args = parser.parse_args()

    file_path = args.file_path
    main(file_path)

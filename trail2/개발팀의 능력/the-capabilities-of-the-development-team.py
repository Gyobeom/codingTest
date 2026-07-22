team_values = list(map(int, input().split()))

# 2 / 2 / 1
# 모든 팀의 능력치는 달라야 함
# 만약 다 동일할 경우에는 -1 반환

min_val = 5000
used_team = [False] * len(team_values)
team_scores = []
all_score_check = 0

for i_1 in range(len(team_values)):
    used_team[i_1] = True
    for i_2 in range(len(team_values)):
        if used_team[i_2] == True:
            continue
        used_team[i_2] = True
        team_scores.append(team_values[i_1] + team_values[i_2])

        for j_1 in range(len(team_values)):
            if used_team[j_1] == True:
                continue
            used_team[j_1] = True
            for j_2 in range(len(team_values)):
                if used_team[j_2] == True:
                    continue
                used_team[j_2] = True
                team_scores.append(team_values[j_1] + team_values[j_2])

                for k_1 in range(len(team_values)): # 오타 수정 (team_valuds -> team_values)
                    if used_team[k_1] == True:
                        continue
                    used_team[k_1] = True
                    team_scores.append(team_values[k_1])

                    # 능력치 다른 여부 확인
                    if team_scores[0] != team_scores[1] and team_scores[1] != team_scores[2] and team_scores[0] != team_scores[2]:
                        all_score_check += 1
                    
                    # 로직 계산 최소 값 넣기
                    max_s = max(team_scores)
                    min_s = min(team_scores)

                    if max_s != min_s:
                        min_val = min(min_val, max_s - min_s)

                    team_scores.pop()
                    used_team[k_1] = False

                team_scores.pop()
                used_team[j_2] = False
            
            used_team[j_1] = False
        
        used_team[i_2] = False
        team_scores.pop()
    
    used_team[i_1] = False

if all_score_check == 0:
    print(-1)
else:
    print(min_val)
def solution():
    input_list = list(map(int, input().split()))
    used = [False] * 6
    team_value = []
    min_val = 1_000_000

    for i in range(6):
        used[i] = True

        for i_2 in range(6):
            if used[i_2]:
                continue

            used[i_2] = True
            team_value.append(input_list[i] + input_list[i_2])

            for k in range(6):
                if used[k]:
                    continue

                used[k] = True

                for k_2 in range(6):
                    if used[k_2]:
                        continue

                    used[k_2] = True
                    team_value.append(input_list[k] + input_list[k_2])

                    for j in range(6):
                        if used[j]:
                            continue

                        used[j] = True

                        for j_2 in range(6):
                            if used[j_2]:
                                continue

                            used[j_2] = True
                            team_value.append(input_list[j] + input_list[j_2])

                            result = max(team_value) - min(team_value)
                            min_val = min(min_val, result)

                            # 세 번째 팀 원상 복구
                            team_value.pop()
                            used[j_2] = False

                        used[j] = False

                    # 두 번째 팀 원상 복구
                    team_value.pop()
                    used[k_2] = False

                used[k] = False

            # 첫 번째 팀 원상 복구
            team_value.pop()
            used[i_2] = False

        used[i] = False

    print(min_val)


solution()
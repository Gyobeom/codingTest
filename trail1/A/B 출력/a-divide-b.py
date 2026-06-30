A, B = map(int,input().split())

def truncate_division_manual(a, b, decimal_places=21):
    # 1. 정수 부분 계산
    integer_part = a // b
    remainder = a % b
    
    # 2. 소수점 이하 자리들을 담을 리스트
    decimals = []
    
    # 3. 21번 반복하며 한 자리씩 계산
    for _ in range(decimal_places):
        remainder *= 10        # 나머지에 10을 곱함
        digit = remainder // b  # 그 상태에서의 몫(0~9 사이)이 다음 소수점 자리수
        decimals.append(str(digit))
        remainder %= b         # 다시 나머지를 구함
        
    return f"{integer_part}.{''.join(decimals)}"

# 실행
print(truncate_division_manual(A, B, 20))
# 결과: 0.333333333333333333333
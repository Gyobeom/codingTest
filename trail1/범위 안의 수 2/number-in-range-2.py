sum_val = 0
cnt_val = 0

data_list = []
for _ in range(10):
    input_num = int(input())
    if input_num >= 0 and input_num <= 200:
        sum_val += input_num
        cnt_val += 1

print(f'{sum_val} {sum_val/cnt_val:.1f}')


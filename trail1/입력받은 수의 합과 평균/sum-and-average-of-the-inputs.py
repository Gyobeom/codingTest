n = int(input())
data_arr = []

for _ in range(n):
    data_arr.append(int(input()))
sum_val = sum(data_arr)
print(f"{sum_val} {sum_val/n:.1f}")

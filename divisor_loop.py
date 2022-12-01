n = int(input())
new_list=[i for i in range(1, int(n / 2+1)) if n % i == 0]
print(new_list)
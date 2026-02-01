for number in range(1, 20, 2):
    print(number)
    # pass

million = list(range(1, 1000001))
for number in million:
    # print(number)
    pass

print(min(million))
print(max(million))
print(sum(million))

mult_3 = []
for num in range(3, 30):
    if num%3 == 0:
        mult_3.append(num)
        for i in mult_3:
            print(i)

for cube in range(1, 11):
    print(cube**3)

cube = [cub**3 for cub in range(1, 11)]
print(cube)
total = 0
print(list(range(1, 100)))
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        total +=i
print(total)
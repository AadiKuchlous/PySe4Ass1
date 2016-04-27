s = input("Enter numbers with commas")
l = s.split(",")
l1 = []
for i in l:
    l1.append(i)
    if (int(i) % 5 == 0 and int(i) % 7 == 0):
        l1.remove(i)
print(l1)

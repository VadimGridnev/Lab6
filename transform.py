data = input().split()
original = [int(x) for x in data]
transformed = [abs(x) for x in original]
print("Исходный:",original)
print("Новый: ",transformed)
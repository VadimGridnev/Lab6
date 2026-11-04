data = input().split()
nums = [int(x) for x in data]
selected = [x for x in nums if x < 0 and x % 2 != 0]
print("Выборка:", selected)
print("Количество:", len(selected))
print("Сумма:", sum(selected))
print("Отсортированная копия:", sorted(selected))
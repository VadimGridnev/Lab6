data = input().split()
if not data:
    print("Нет данных")
else:
    nums = [int(x) for x in data]
    count = len(nums)
    total = sum(nums)
    minimum = min(nums)
    maximum = max(nums)
    average = total / count
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.2f}")
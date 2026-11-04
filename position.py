data = input().split()
if not data:
    print("Нет данных")
else:
    nums = [int(x) for x in data]
    maximum = max(nums)
    positions = [i for i, x in enumerate(nums) if x == maximum]
    print(positions)
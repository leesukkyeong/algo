nums = set()
for _ in range(10):
    i = int(input())
    nums.add(i%42)
print(len(nums))
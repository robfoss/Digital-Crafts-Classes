nums = [1, 2, 3, 4, 5, 6, 7, 8]
summed = sum(nums)
print(summed)

large = max(nums)
print(large)

small = min(nums)
print(small)

evens = list(range(2, 11, 2))
print(evens)

print('\n')

more_nums = [-1, -2, -3, 0, 1, 2, 3, 4]
for num in more_nums:
    if num >= 0:
        print(num)

print('\n')
new_nums = []
for num in more_nums:
    if num >= 0:
        new_nums.append(num)

print(new_nums)
print('\n')
multiples = list(range(10))
factor = 2
final = []

for num in multiples:
    final.append(num * factor)

print(final)    

line = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]
nums = [int(el) for el in line[0].split(',')]

spoken = []

for i in range(2020):
    if i < len(nums):
        spoken.append(nums[i])
        continue

    if spoken.count(spoken[-1]) == 1:
        spoken.append(0)
    else:
        this_pos = i - 1
        last_pos = i - spoken[:-1][::-1].index(spoken[-1]) - 2
        spoken.append(this_pos - last_pos)

print(spoken[-1])

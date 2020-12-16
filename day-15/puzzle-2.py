line = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]
nums = [int(el) for el in line[0].split(',')]

spoken = {}
last_spoken = 0

for i in range(30000000):
    print(i)
    if i < len(nums):
        spoken[nums[i]] = [i]
        last_spoken = nums[i]
        continue

    if len(spoken[last_spoken]) == 1:
        if 0 in spoken:
            spoken[0] = spoken[0][-2:] + [i]
        else:
            spoken[0] = [i]
        last_spoken = 0
    else:
        this_pos = i - 1
        last_pos = spoken[last_spoken][-2]
        if this_pos - last_pos in spoken:
            spoken[this_pos - last_pos] = spoken[this_pos - last_pos][-2:] + [i]
        else:
            spoken[this_pos - last_pos] = [i]
        last_spoken = this_pos - last_pos

print(last_spoken)

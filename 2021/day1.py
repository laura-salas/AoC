# problem link: https://adventofcode.com/2021/day/1
lines_unparsed = """input_here"""
lines_unparsed = lines_unparsed.split("\n")
nums = []
for line in lines_unparsed:
    line.replace(" ", "")
    if line:
        nums.append(int(line))

increases = 0
window_A = 2
window_B = 3

while window_B < len(nums):
    sum_a = nums[window_A - 1] + nums[window_A - 1] + nums[window_A]
    sum_b = nums[window_B - 2] + nums[window_B - 1] + nums[window_B]
    if sum_b > sum_a:
        increases += 1
    window_A += 1
    window_B += 1
print(increases)


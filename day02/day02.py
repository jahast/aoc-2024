import re

with open("input.txt", "r") as f:
    lines = f.readlines()

reps = []

for line in lines:
    nums = [int(num) for num in re.findall(r"\d+", line)]
    reps.append(nums)

ans1 = []

def is_legit(rep):
    diffs = [rep[i] - rep[i + 1] for i in range(0, len(rep) - 1)]
    positive = [d > 0 for d in diffs]
    negative = [d < 0 for d in diffs]
    is_gradual = all(positive) or all(negative)
    is_gentle = all([1 <= abs(d) <= 3 for d in diffs])

    return is_gradual and is_gentle

for i, rep in enumerate(reps):
    if is_legit(rep):
        ans1.append(i)

print(len(ans1))

ans2 = []

def drop_nth(lst, n):
    return [item for i, item in enumerate(lst) if i != n]

for i, rep in enumerate(reps):
    for j in range(0, len(rep)):
        to_check = drop_nth(rep, j)
        if is_legit(to_check):
            ans2.append(i)
            break

print(len(ans2))

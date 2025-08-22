import re

with open("input.txt", "r") as f:
    lines = f.readlines()

not_allowed_after = {}

for line in lines:
    if "|" in line:
        m = re.match(r"(\d+)\|(\d+)", line)
        must_be_before, must_be_after = int(m.group(1)), int(m.group(2))

        if must_be_after not in not_allowed_after:
            not_allowed_after[must_be_after] = []
        not_allowed_after[must_be_after].append(must_be_before)

updates = []

for line in lines:
    if "," in line:
        update = []
        for p in re.finditer(r"\d+", line):
            update.append(int(p.group()))
        updates.append(update)

ans1 = 0
ans2 = 0

for update in updates:
    for i, p in enumerate(update):

        if p in not_allowed_after:
            tail = update[i:]
            not_allowed = not_allowed_after[p]
            rule_breaks = set(tail).intersection(not_allowed)
            if len(rule_breaks) > 0:
                break

    else:
        ans1 += update[int(len(update) / 2)]
        continue

    n_update = len(update)
    for round in range(0, n_update):
        for i in range(0, n_update):
            for k in range(i + 1, n_update):
                cur, comp = update[i], update[k]
                if cur in not_allowed_after and comp in not_allowed_after[cur]:
                    temp = update[i]
                    update[i] = update[i + 1]
                    update[i + 1] = temp
    ans2 += update[int(len(update) / 2)]

print(ans1)
print(ans2)

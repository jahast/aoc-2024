import re
import sys

with open("input.txt", "r") as f:
    lines = f.readlines()

text = "".join(lines)

ans1 = 0

for ins in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text):
    fst, snd = int(ins.group(1)), int(ins.group(2))
    print((fst,snd))
    ans1 = ans1 + fst * snd

print(ans1)

mults = []

for ins in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text):
    fst, snd = int(ins.group(1)), int(ins.group(2))
    idx = ins.start()
    mults.append((idx, fst, snd))

dos = [0]
for ins in re.finditer(r"do\(\)", text):
    dos.append(ins.start())

donts = []
for ins in re.finditer(r"don't\(\)", text):
    donts.append(ins.start())

valid_ranges = []

for do in dos:
    end_of_range = next(iter([d for d in donts if d > do]), 1000000000000)
    valid_ranges.append((do, end_of_range))

ans2 = 0

for mult in mults:
    for valid_range in valid_ranges:
        if valid_range[0] < mult[0] < valid_range[1]:
            break
    else:
        continue
    ans2 = ans2 + mult[1] * mult[2]

print(ans2)

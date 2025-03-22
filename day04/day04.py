import re
import sys

with open("input.txt", "r") as f:
    lines = f.readlines()

array = "".join(lines)
array_len = len(array)
valid_idx = lambda x: 0 <= x < array_len
len_row = len(lines[0])
make_str = lambda x: "".join([array[k] for k in x])
is_hit = lambda x: make_str(x) == "MAS"
ans1 = 0

for i in range(0, len(array)):
    if array[i] == "X":
        right = [k for k in [i+1, i+2, i+3] if valid_idx(k)]
        left = [k for k in [i-1, i-2, i-3] if valid_idx(k)]
        up = [k for k in [i - 1*len_row, i - 2*len_row, i - 3*len_row] if valid_idx(k)]
        down = [k for k in [i + 1*len_row, i + 2*len_row, i + 3*len_row] if valid_idx(k)]

        nw = [k for k in [i - 1*len_row - 1, i - 2*len_row - 2, i - 3*len_row - 3] if valid_idx(k)]
        ne = [k for k in [i - 1*len_row + 1, i - 2*len_row + 2, i - 3*len_row + 3] if valid_idx(k)]
        sw = [k for k in [i + 1*len_row - 1, i + 2*len_row - 2, i + 3*len_row - 3] if valid_idx(k)]
        se = [k for k in [i + 1*len_row + 1, i + 2*len_row + 2, i + 3*len_row + 3] if valid_idx(k)]

        ans1 += is_hit(right) + is_hit(left) + is_hit(up) + is_hit(down)\
        + is_hit(nw) + is_hit(ne) + is_hit(sw) + is_hit(se)

print(ans1)

ans2 = 0

for i in range(0, len(array)):
    if array[i] == "A":

        nw = [k for k in [i - 1*len_row - 1, i, i + len_row + 1] if valid_idx(k)]
        ne = [k for k in [i - 1*len_row + 1, i, i + len_row - 1] if valid_idx(k)]
        sw = [k for k in [i + 1*len_row - 1, i, i - len_row + 1] if valid_idx(k)]
        se = [k for k in [i + 1*len_row + 1, i, i - len_row - 1] if valid_idx(k)]

        if (is_hit(nw) or is_hit(se)) and (is_hit(ne) or is_hit(sw)):
            ans2 += 1

print(ans2)


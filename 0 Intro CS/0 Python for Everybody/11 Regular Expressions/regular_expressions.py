import re

f_0 = "regex_sum_42.txt"  #sample
f_1 = "regex_sum_1483534.txt"

file_body = open(f_1)

sum = float()
for line in file_body:
    snum = re.findall("[0-9]+", line)
    if len(snum) < 1:
        continue
    else:
        for i in snum:
            num = float(i)
            sum += num

print(int(sum))
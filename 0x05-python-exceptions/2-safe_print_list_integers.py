#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
count = 0
length = 0
for i in my_list:
length += 1
for j in range(0, x):
try:
print("{:d}".format(my_list[j]), end='')
count += 1
except (TypeError, ValueError):
pass
print()
return count

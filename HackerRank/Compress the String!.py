# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

s = input()
group_list = [(len(list(j)), int(i)) for i, j in itertools.groupby(s)]
for group in group_list:
    print(group, end = ' ')
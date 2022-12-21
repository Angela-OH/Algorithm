n = int(input())
s = input().strip()
leftB, leftR = 0, 0
isLeftB, isLeftR = 0, 0
for i in range(len(s)):
    if isLeftB == 0 and s[i] == 'B':
        isLeftB = 1
    if isLeftR == 0 and s[i] == 'R':
        isLeftR = 1
    if isLeftR == 1 and s[i] == 'B':
        leftB += 1
    if isLeftB == 1 and s[i] == 'R':
        leftR += 1
rightB, rightR = 0, 0
isRightB, isRightR = 0, 0
for i in range(len(s) - 1, -1, -1):
    if isRightB == 0 and s[i] == 'B':
        isRightB = 1
    if isRightR == 0 and s[i] == 'R':
        isRightR = 1
    if isRightR == 1 and s[i] == 'B':
        rightB += 1
    if isRightB == 1 and s[i] == 'R':
        rightR += 1

print(min(leftB, leftR, rightB, rightR))
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = float(input())
bc = float(input())
print(str(round(math.degrees(math.atan((ab/bc))))) + '\u00B0')
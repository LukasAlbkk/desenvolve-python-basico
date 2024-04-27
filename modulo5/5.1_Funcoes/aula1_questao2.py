import math
import random

sum = 0
n = int(input("Digite n: "))
for n in range(1,n+1):
    num = random.randint(1,100)
    sum += num
print(f"{math.sqrt(sum):.4f}")
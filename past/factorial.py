# 5! - факториал числа 5
# 5! = 1*2*3*4*5
# fact = 1
# n = int(input())
# for i in range(1, n + 1):
#   fact *= i
# print(fact)

n = int(input())
fact = 1
while n >= 1:
  fact *= n
  n -= 1
print(fact)
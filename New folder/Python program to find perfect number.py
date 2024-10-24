my_list=[]
for x in range(1, 1000000):
  sum_divisor = 0
  for y in range(1,x):
    if x % y == 0:
      sum_divisor += y
  if sum_divisor == x:
      my_list.append(x)
print(my_list)

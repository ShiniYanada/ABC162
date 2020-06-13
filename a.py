n = input()
flag = 0
for i in n:
  if i == '7':
    flag = 1
    break
if flag:
  print('Yes')
else:
  print('No')

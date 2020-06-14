def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)
ans = 0
k = int(input())
for i in range(1, k + 1):
  for j in range(i, k + 1):
    for l in range(j, k + 1):
      if i == j == l:
        ans += i
      elif i == j or j == l or i == l:
        a = gcd(i, j)
        a = gcd(a, l) 
        ans = ans + a * 3
      else:
        a = gcd(i, j)
        a = gcd(a, l)
        ans = ans + a * 6
print(ans)


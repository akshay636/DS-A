def interger_break(n):
  if n<=2:
    return 1
  ar =[0]*(n+1)
  
  for i in range(3,n+1):
    for j in range(1,i):
      print(i,j,ar)
      ar[i] = max(ar[i], j*max(i-j, ar[i-j]))
  return ar

print(interger_break(10))
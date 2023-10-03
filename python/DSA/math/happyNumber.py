def happyNumber(n,sum=0, seen=set()):
  if n ==1:
    return True
  if n in seen:
    return False
  
  temp=n
  sum=0
  while temp!=0:
    digit = temp%10
    sum += digit*digit
    temp //= 10
  seen.add(n)
  return happyNumber(sum,sum,seen)

print(happyNumber(19))
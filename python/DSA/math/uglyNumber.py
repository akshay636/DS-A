def is_ugly(number):
    if number <= 0:
        return False
    while number % 2 == 0:
        number //= 2
    while number % 3 == 0:
        number //= 3
    while number % 5 == 0:
        number //= 5
    return number == 1


def opt(n):
  if n<=0:
    return False
  for fact in [2,3,5]:
    while n%fact==0:
      n //=  fact
  return n==1
print(opt(6))
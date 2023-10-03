import re
def valid_palindrone(s):
  valid =[':',',','-']
  s = s.lower()
  s =re.sub(r'[^a-zA-Z0-9\s]', '', s)
  s1=''
  for i in s:
      if i!=" ":
        s1 += i
  revs1 =s1[::-1]
  for i in range(0,len(s1)):
    if revs1[i]!=s1[i]:
      return False
  return True
    
print(valid_palindrone('A man, a plan, a canal: Panama'))
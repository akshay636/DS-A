def world_patter(pattern, s):
  s = s.split(' ')
  if len(s)!=len(pattern):
    return False
  obj = dict()
  for i in range(len(pattern)):
    obj[pattern[i]] = s[i]
  st=''
  for j in pattern:
    print(j)
    st += obj[j]
    st += ' '
  print(obj)
  return st.strip() == " ".join(s)
print(world_patter('abba', 'dog dog dog dog'))
def minimum_len_after_remove(s):
  a =''
  s1= s
  for i in range(0,len(s)):
    if s[i]=='A' and s[i+1] =='B' or s[i]=='C' and s[i+1] =='D':
      a += s[i]+s[i+1]
    if a =='AB' or a =='CD':
      s = s.replace(a,'')
      a =''
      break
  return s
  
print(minimum_len_after_remove('ABFCACDB'))
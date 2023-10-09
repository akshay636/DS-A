def isomorphic(s,t):
  s_obj={}
  t_obj={}
  for i in range(len(s)):
    s_char, t_char = s[i], t[i]
    print(s_char,t_char)
    if s_char in s_obj:
      if s_obj[s_char]!=t_char:
        return False
    else:
        s_obj[s_char]= t_char
    if t_char in t_obj:
      if t_obj[t_char]!=s_char:
        return False
    else:
        t_obj[t_char]= s_char
  return True
    
print(isomorphic('egg','add'))
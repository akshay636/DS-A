def sub_sequence(s,t):
  if len(s)==0:
    return True
  s_in , t_in = 0, 0
  while t_in <len(t):
    if s[s_in] ==t[t_in]:
      s_in += 1
      if s_in ==len(s):
        return True
    t_in += 1
  return False
  
    
    

print(sub_sequence('ab','baab'))
def reverseStr(s):
  strg = s.split(' ')
  print(strg)
  revStr =''
  for i in range(len(strg)-1,-1,-1):
    if strg[i]!='':
      if i!=0:
        print('call')
        revStr += strg[i] + ' '
      else:
        revStr += strg[i]
  return ''.join(revStr)

a ='blue is sky the'    
print(reverseStr("  hello world  "))

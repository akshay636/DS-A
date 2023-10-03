parans =['(', ')', '{', '}', '[',']']
def validParans(str):
  obj={
  '(':')',
  '{':'}',
  '[':']'
  }
  stack=[]
  for i in str:
    if i in obj:
      stack.append(i)
    else:
      if not stack:
        return False
      top = stack.pop()
      if obj[top]!=i:
        return False
  return len(stack)==0

print(validParans('()[]{a-b}'))
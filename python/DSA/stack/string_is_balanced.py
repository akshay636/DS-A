from index import DeStack
def is_match(ch1, ch2):
    print(ch1,ch2)
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    print(match_dict[ch1] == ch2)
    return match_dict[ch1] == ch2
def str_balanced(s):
  stack = DeStack()
  for ch in s:
      if ch=='(' or ch=='{' or ch == '[':
          stack.push(ch)
      if ch==')' or ch=='}' or ch == ']':
          if stack.size()==0:
              return False
          if not is_match(ch,stack.pop()):
              return False

  return stack.size()==0

print(str_balanced('()[]{a=b}'))
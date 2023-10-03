def zigzag(s,numRows):
  if numRows==1 or numRows >= len(s):
    return s
  rows = ['' for _ in range(numRows)]
  c_r=0
  dir =-1
  for i in s:
    rows[c_r] += i
    if c_r ==0 or c_r == numRows-1:
      dir *=-1
    c_r += dir
  return ''.join(rows)
print(zigzag('PAYPALISHIRING',4))
# def reArrange(ar):
#   ar.sort()
#   for i in range(0, len(ar)):
#       if i not in ar:
#           ar[i] = -1
#       else:
#           ar[i] = i
#   return ar
# ar =[19, 7, 0, 3, 18, 15, 12, 6, 1, 8,11, 10, 9, 5, 13, 16, 2, 14, 17, 4]        
# print(reArrange(ar))
def reArrange(ar):
    n = len(ar)
    for i in range(n):
        if ar[i] != -1 and ar[i] != i:
            # Swap elements until ar[i] = i or ar[i] == -1
            while ar[i] != -1 and ar[i] != i:
                ar[ar[i]], ar[i] = ar[i], ar[ar[i]]
    
    # Replace remaining -1's with -1 at their respective positions
    for i in range(n):
        if ar[i] == -1:
            ar[i] = -1
    
    return ar

ar = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
print(reArrange(ar))

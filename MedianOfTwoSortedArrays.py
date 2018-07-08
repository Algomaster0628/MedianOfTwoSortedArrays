def MedianArray(m,n):
  Array = m + n
  Array = sorted(Array)
  i = len(Array)
  if i % 2 == 1:
    x = (i + 1)//2 - 1 
    return Array[x]
  elif i % 2 == 0:
    x = i//2 - 1
    y = x + 1
    return (Array[x] + Array[y])/2
z = MedianArray([1,3,5],[4,5])
print(z)

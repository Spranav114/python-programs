def chkprime(x):
  #num = 0
  sum = 0
  for num in x:
      p = 1
      for i in range(2,num):
          if(num % i == 0):
             p = 0
             break
          i = i + 1
      if(p == 1):
         sum = sum + num
  return sum








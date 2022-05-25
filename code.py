def recur_fibo(a):
   if a <= 1:
       return a
   else:
       return(recur_fibo(a-1) + recur_fibo(a-2))
aterms = 12
if aterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(aterms):
       print(recur_fibo(i))

import time
import math

n=int(input())
start_time=time.process_time()
count=0
n1=int(math.sqrt(n))
for i in range (2,n1):
    if (n%i==0):
        count=count+1
        break
if count>0:
    print("NOT PRIME")
else:
    print("PRIME")
print(time.process_time()-start_time,"seconds")
numm=int(input())
sum=0
temps=numm
while temps>0:
    digit=temps%10
    sum+=digit**3
    temps //=10
if numm==sum:
   print("yes")
else:
   print("no")

a=int(input ("enter a num:"))
ans=0
while a>1:
    ans+=1
    if(a%2==0):
      a/=2
    else:
        a=a-1
print("no of times execution",ans)
name=input("enter your name:")
n=0
a=0
for i in name:
    n+=1
    if i==' ':
        print(name[a].upper(),".",end="",flush=True)
        a=n
print(name[a:])

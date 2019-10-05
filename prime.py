flag=0
for i in range(200,1000000,1):
    for j in range(2,(i//2)+1,1):
        if i%j==0:
            flag=10
            break
    if flag==0:
        print(i)
    flag=0

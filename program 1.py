n = int(input("Enter an integer:"))
temp = n
cnt = 0
while temp !=0 :
    cnt = cnt+1
    temp = temp // 10
temp = n
for i in range(cnt -1, -1, -1):
    firstdigit = temp //(10**i)
    temp = temp %(10**i)
    print(firstdigit,end='*')
    

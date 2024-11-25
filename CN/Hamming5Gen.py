d9=input("Enter ")
p8=''
d7=input("Enter ")
d6=input("Enter ")
d5=input("Enter ")
p4=''
d3=input("Enter ")
p2=''
p1=''

def iseven(a):
    if int(a)%2==0:
        return '0'
    return '1'

p1=iseven(int(d3)+int(d5)+int(d7)+int(d9))
p2=iseven(int(d3)+int(d6)+int(d7))
p4=iseven(int(d5)+int(d6)+int(d7))
p8=iseven(int(d9))

ans=d9+p8+d7+d6+d5+p4+d3+p2+p1
print(ans)




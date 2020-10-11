#s = [[4,9,2],[3,5,7],[8,1,5]]

s = [[4,9,2],[3,5,7],[8,1,5]]

r1 = s[0][0]+s[0][1]+s[0][2]
r2 = s[1][0]+s[1][1]+s[1][2]
r3 = s[2][0]+s[2][1]+s[2][2]

c1 = s[0][0]+s[1][0]+s[2][0]
c2 = s[0][1]+s[1][1]+s[2][1]
c3 = s[0][2]+s[1][2]+s[2][2]

d1 = s[0][0]+s[1][1]+s[2][2]
d2 = s[2][0]+s[1][1]+s[0][2]

clist = [r1,r2,r3,c1,c2,c3,d1,d2]

print(clist)

squaremax = int(max(clist,key=clist.count))

print(squaremax)

lista = [abs(x-squaremax) for x in clist]
print(sum(lista))
#!/usr/bin/env python3

x = 1
y = 1
z = 1
n = 2

#coordinate = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x+y+z != N]
ans=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(ans)


def foo(x,y,z,n):
    ret = [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k==n ]
    return ret

print(foo(1,1,2,3))

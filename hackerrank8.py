platform: hackerrank
problem type: list comprehensions
program:
x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i,j,k=x+1,y+1,z+1
    result=[ ]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                    result.append([i,j,k])
    print(result)
